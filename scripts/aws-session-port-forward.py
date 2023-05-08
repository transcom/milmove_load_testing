#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import subprocess
import sys

cluster = "loadtesting"
port_number = "4000"

result = subprocess.run(["aws", "ecs", "list-tasks", "--cluster", cluster], stdout=subprocess.PIPE)

tasks = json.loads(result.stdout)
if "taskArns" not in tasks or len(tasks["taskArns"]) == 0:
    print(f"Cannot find any running tasks in cluster: {cluster}", file=sys.stderr)
    sys.exit(1)

if len(tasks["taskArns"]) != 1:
    print(f"More than one task running in cluster: {cluster}", file=sys.stderr)
    sys.exit(1)

task_arn = tasks["taskArns"][0]

result = subprocess.run(
    ["aws", "ecs", "describe-tasks", "--cluster", cluster, "--tasks", task_arn], stdout=subprocess.PIPE
)

try:
    task_details = json.loads(result.stdout)
except Exception as e:
    print(f"Cannot parse describe tasks for taskArn: {task_arn}", file=sys.stderr)
    print(sys.exc_info()[0], file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)

if "tasks" not in task_details or len(task_details["tasks"]) == 0:
    print(f"Cannot find task detail for taskArn: {task_arn}", file=sys.stderr)
    sys.exit(1)

if len(task_details["tasks"]) != 1:
    print(f"More than one task detail for taskArn: {task_arn}", file=sys.stderr)
    sys.exit(1)

task = task_details["tasks"][0]

if "containers" not in task or len(task["containers"]) == 0:
    print(f"Cannot find containers for taskArn: {task_arn}", file=sys.stderr)
    sys.exit(1)

# if len(task["containers"]) != 1:
#     print("More than one container for taskArn: {}", task_arn, file=sys.stderr)
#     sys.exit(1)

container = task["containers"][0]

task_id = task_arn.split("/")[-1]
container_id = container["runtimeId"]

target = "ecs:{cluster}_{task_id}_{container_id}".format(cluster=cluster, task_id=task_id, container_id=container_id)

parameters = json.dumps({"portNumber": [port_number], "localPortNumber": [port_number]})

print("Hit 'Control-C' to exit")
# replace this process with the session
os.execlp(
    "aws",
    "aws",
    "ssm",
    "start-session",
    "--target",
    target,
    "--document-name",
    "AWS-StartPortForwardingSession",
    "--parameters",
    parameters,
)
