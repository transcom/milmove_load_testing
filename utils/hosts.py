# -*- coding: utf-8 -*-
""" utils/mixins.py is for classes that get inherited in conjunction with others, likely Locust classes. """
import logging

from .base import ImplementationError
from .constants import MilMoveEnv, MilMoveDomain

logger = logging.getLogger(__name__)


class MilMoveHostMixin:
    """
    Mixin for Locust's HttpUser to set a host value based on the environment passed in as the --host flag.
    """

    local_protocol = "https"
    local_port = "8080"
    domain = MilMoveDomain.MILMOVE  # any MilMoveDomain value
    is_api = False  # if True, defaults to using the api.<env>.move.mil domain for deployed envs

    def __init__(self, *args, **kwargs):
        """
        Sets host based on environment value from --host flag in command.
        """
        if MilMoveEnv.validate(self.host):
            self.env = self.host  # preserve the original value that was passed in on the command line
            self.host = self.set_host_name()  # set the actual host based on the env

        super().__init__(*args, **kwargs)

    def set_host_name(self):
        """
        Gets the host name based on the domain, environment, and API status.
        """
        if not MilMoveDomain.validate(self.domain):
            logger.debug(f"Bad domain value: {self.domain}")
            raise ImplementationError("Domain for MilMoveUser must be one of the values in MilMoveDomain.")

        return MilMoveDomain.match(self.domain).host_name(self.env, self.is_api, self.local_port, self.local_protocol)
