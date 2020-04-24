import os
from swagger_spec_validator import validate_spec_url



# validate_spec_url('http://milmovelocal:8080/internal/swagger.yaml')

# validate_spec_url('http://milmovelocal:8080/prime/v1/swagger.yaml')

validate_spec_url('file:///Users/lynzt/coding/tw/milmove_load_testing/swagger/prime.yaml')
# validate_spec_url('file:///Users/lynzt/coding/tw/milmove_load_testing/swagger/test.yaml')
