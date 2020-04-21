# -*- coding: utf-8 -*-
import datetime
import os
import sys
import random

from urllib.parse import urljoin

from locust import TaskSet
from locust import seq_task
from bravado.swagger_model import load_file
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

from .base import BaseTaskSequence
from .base import PrimeAPIMixin
from .base import get_swagger_config
from .base import swagger_request






# import json
# import os
from bravado_core.spec import Spec
from bravado_core.validate import validate_object
# from yaml import load, Loader, dump, Dumper


# def validate_address(Address):
#     validate_object(spec, address, Address)


# def get_swagger_spec():
#     with open(spec_path,'r') as spec:
#         return load(spec.read(), Loader)


bravado_config = {
    'validate_swagger_spec': False,
    'validate_requests': False,
    'validate_responses': False,
    'use_models': True,
}


# dir_path = os.path.dirname(os.path.abspath(__file__))
# spec_path = os.path.join(dir_path, "prime.yaml")
# spec_dict = get_swagger_spec()
# spec = Spec.from_dict(spec_dict, config=bravado_config)

# Address = spec_dict['definitions']['Address']



# import warnings
# warnings.filterwarnings("ignore")


class PrimeEndpoints(BaseTaskSequence):
    # print(BaseTaskSequence)
    # print(BaseTaskSequence)

    login_gov_user = None
    session_token = None

    fixtures_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "fixtures"
    )

    # User is the LoggedInUserPayload
    user = {}
    duty_stations = []
    new_duty_stations = []
    move = None
    ppm = None
    entitlements = None
    rank = None
    allotment = None
    zip_origin = "32168"
    zip_destination = "78626"

    def update_user(self):
        self.user = swagger_request(self.swagger_prime.users.showLoggedInUser)

    @seq_task(1)
    def login(self):

        local_cert = (
            "./config/tls/devlocal-mtls.cer",
            "./config/tls/devlocal-mtls.key",
        )
        
        self.requests_client = RequestsClient(ssl_verify=False, ssl_cert=local_cert)
        # Set the session to be the same session as locust uses
        # self.requests_client.session = self.client
        print("&&&&& client")
        print (self.client)
        print("&&&&& client end")

        try:
            self.swagger_prime = SwaggerClient.from_url(
                "https://primelocal:9443/prime/v1/move-task-orders",
                http_client=self.requests_client,
                config=get_swagger_config(),
            )
            if not self.swagger_prime:
                self.kill("prime swagger client failure")
        except Exception as e:
            print("**************")
            print(e)
            print("error!!")
            sys.exit(0)
            return self.kill("unknown swagger client failure")


    @seq_task(2)
    def retrieve_user(self):
        self.update_user()

class PrimeClientBehavior(TaskSet):
    tasks = {PrimeEndpoints: 1}
