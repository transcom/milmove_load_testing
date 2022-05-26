# -*- coding: utf-8 -*-
from .milmove import MilMoveTasks  # noqa

import warnings

import requests

# Sets warning to trigger once rather than on each instance
warnings.simplefilter("once", requests.packages.urllib3.exceptions.InsecureRequestWarning)
