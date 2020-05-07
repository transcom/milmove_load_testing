import datetime
import os
import sys
import random

from urllib.parse import urljoin

from locust import TaskSet
from locust import seq_task
import bravado_core
from bravado.swagger_model import load_file
from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient

# petstore = SwaggerClient.from_url('./swagger/pet.yaml')

petstore = SwaggerClient.from_spec(load_file('./swagger/pet.yaml'))

pet_response = petstore.pet.getPetById(petId=42).response()
http_response = pet_response.incoming_response
assert isinstance(http_response, bravado_core.response.IncomingResponse)
print (http_response.headers)
print (http_response.status_code)
print (pet_response.result.name)





