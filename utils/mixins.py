# -*- coding: utf-8 -*-
import logging
from .base import ImplementationError, MilMoveEnv, MilMoveDomain

logger = logging.getLogger(__name__)


class MilMoveHostMixin:
    """
    Mixin for Locust's HttpUser to set a host value based on the environment passed in as the --host flag.
    """

    local_port = "8080"
    domain = MilMoveDomain.MILMOVE  # any MilMoveDomain value
    is_api = False  # if True, defaults to using the api.<env>.move.mil domain for deployed envs

    def __init__(self, *args, **kwargs):
        """
        Sets host based on environment value from --host flag in command.
        """
        if MilMoveEnv.validate(self.host):
            self.host = self.set_host_name()

        super().__init__(*args, **kwargs)

    def set_host_name(self):
        """
        Gets the host name based on the domain, environment, and API status.
        """
        if not MilMoveDomain.validate(self.domain):
            logger.debug(f"Bad domain value: {self.domain}")
            raise ImplementationError("Domain for MilMoveUser must be one of the values in MilMoveDomain.")

        return self.domain.host_name(self.host, self.is_api, self.local_port)
