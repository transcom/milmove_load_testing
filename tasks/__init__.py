# -*- coding: utf-8 -*-
from .milmove import MilMoveTasks  # noqa
from .office import ServicesCounselorTasks, TOOTasks  # noqa
from .prime import PrimeTasks, SupportTasks  # noqa
from .prime_endpoint_workflows import PrimeEndpointWorkflowsTasks  # noqa
from .prime_hhg_workflow import PrimeWorkflowTasks  # noqa

import warnings

import requests

# Sets warning to trigger once rather than on each instance
warnings.simplefilter("once", requests.packages.urllib3.exceptions.InsecureRequestWarning)
