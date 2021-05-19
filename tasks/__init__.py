# -*- coding: utf-8 -*-
from .office import ServicesCounselorTasks, TOOTasks  # noqa
from .milmove import MilMoveTasks  # noqa
from .prime import PrimeTasks, SupportTasks  # noqa
from .prime_hhg_workflow import PrimeWorkflowTasks  # noqa
from .prime_endpoint_workflows import PrimeEndpointWorkflowsTasks  # noqa
import warnings
import requests

# Sets warning to trigger once rather than on each instance
warnings.simplefilter("once", requests.packages.urllib3.exceptions.InsecureRequestWarning)
