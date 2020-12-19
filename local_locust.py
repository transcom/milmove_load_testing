# -*- coding: utf-8 -*-
"""
This script updates the /etc/hosts file from within a Docker container to contain the hostnames used in the MilMove
project. ** It should only be run from within a container. **

This script also executes a locust command immediately after updating the hosts file. All locust arguments and flags can
be passed in as a string, but otherwise written with the usual syntax. Ex:

$ python local_locust.py "-f /app/locustfiles/prime.py --host local"
"""
import os
import socket
import argparse

# NOTE: we cannot use the constants file in this project for these values because this script must be able to run
# independently.
MILMOVE_HOSTNAMES = [
    "milmovelocal",
    "officelocal",
    "primelocal",
]


def update_docker_hosts():
    """
    Grabs the Docker internal IP address using host.docker.internal, then adds lines to the /etc/hosts file with each of
    the MilMove hostnames pointing towards this IP address.
    :return: None
    """
    docker_internal_ip = socket.gethostbyname("host.docker.internal")

    with open("/etc/hosts", "a") as docker_hosts:
        docker_hosts.write("\n# MilMove Hosts added by local_locust.py\n")

        for hostname in MILMOVE_HOSTNAMES:
            docker_hosts.write(f"{docker_internal_ip} {hostname}\n")


if __name__ == "__main__":
    command = argparse.ArgumentParser(description="todo")
    command.add_argument("locust_flags", type=str, help="todo arg")

    args = command.parse_args()
    locust_flags = args.locust_flags.split()  # We will need the locust arguments as a list so we can invoke it later
    locust_flags.insert(0, "locust")

    update_docker_hosts()

    # Calls locust with the split arguments and stops execution of this (local_locust.py) command:
    os.execvp("locust", locust_flags)
