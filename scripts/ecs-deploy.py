#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import os

sts = boto3.client("sts")

response = sts.get_caller_identity()
print("A", response["Account"], response["Arn"])

ecs = boto3.client("ecs")

task_family = os.getenv("ECS_TASK_DEFINITION_FAMILY", "exp-web-loadtesting")
# use os.environ.get so this will explode if the env var isn't set
task_image = os.environ.get("ECS_TASK_IMAGE")

definitions = ecs.describe_task_definition(taskDefinition=task_family)
current_task_def = definitions["taskDefinition"]

# LOCUSTFILE can be set in the build overrides of the CodeBuild config
# The leading colon indicates this line only modifies the LOCUSTFILE
# environment variable and has no other effects
locustfile = os.getenv("LOCUSTFILE", "/app/locustfiles/queue.py")

container_defs = [
    {
        "name": "exp-web-loadtesting",
        "image": task_image,
        "essential": True,
        "entryPoint": ["locust"],
        "command": ["-f", locustfile, "--host", "dp3", "--web-port", "4000"],
        "environment": [{"name": "DEVLOCAL_AUTH", "value": "true"}],
        "secrets": [
            {
                "name": "MOVE_MIL_DP3_TLS_CERT",
                "valueFrom": "arn:aws-us-gov:ssm:us-gov-west-1:021081706899:parameter/app-load-testing/move_mil_dp3_tls_cert",
            },
            {
                "name": "MOVE_MIL_DP3_TLS_KEY",
                "valueFrom": "arn:aws-us-gov:ssm:us-gov-west-1:021081706899:parameter/app-load-testing/move_mil_dp3_tls_key",
            },
        ],
        "ulimits": [{"name": "nofile", "softLimit": 10000, "hardLimit": 10000}],
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "/ecs/loadtesting/exp-web",
                "awslogs-region": "us-gov-west-1",
                "awslogs-stream-prefix": "exp-web",
            },
        },
        "portMappings": [{"containerPort": 4000, "hostPort": 4000, "protocol": "tcp"}],
        "readonlyRootFilesystem": False,
        "healthCheck": {
            "command": [
                "CMD",
                "/usr/bin/curl",
                "-sSf",
                "http://localhost:4000",
            ],
        },
    },
    {
        "name": "otel-exp-web-loadtesting",
        "image": "amazon/aws-otel-collector:v0.29.0",
        "essential": True,
        "command": ["--config=/etc/ecs/container-insights/otel-task-metrics-config.yaml"],
        "environment": [],
        "logConfiguration": {
            "logDriver": "awslogs",
            "options": {
                "awslogs-group": "/ecs/loadtesting/exp-web",
                "awslogs-region": "us-gov-west-1",
                "awslogs-stream-prefix": "otel-exp-web",
            },
        },
        "portMappings": [],
        "healthCheck": {
            "command": [
                "CMD",
                "/healthcheck",
            ],
        },
    },
]

response = ecs.register_task_definition(
    family=task_family,
    taskRoleArn=current_task_def["taskRoleArn"],
    executionRoleArn=current_task_def["executionRoleArn"],
    networkMode=current_task_def["networkMode"],
    containerDefinitions=container_defs,
    cpu="2048",
    memory="8192",
    requiresCompatibilities=["FARGATE"],
)

print(response)

# use forceNewDeployment in case we are re-running the build and the
# image isn't changing

response = ecs.update_service(
    cluster="loadtesting",
    service="exp-web",
    desiredCount=1,
    # this uses the latest ACTIVE revision of the task_definition
    taskDefinition=task_family,
    forceNewDeployment=True,
)

print(response)
