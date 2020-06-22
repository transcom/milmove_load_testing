# MilMove Load Testing

This repository contains code written to run load testing for the [MilMove](https://github.com/transcom/mymove) application.
Load testing is accomplished via the [Locust](https://docs.locust.io/en/stable/) framework.

## License Information

Works created by U.S. Federal employees as part of their jobs typically are not eligible for copyright in the United
States. In places where the contributions of U.S. Federal employees are not eligible for copyright, this work is in
the public domain. In places where it is eligible for copyright, such as some foreign jurisdictions, the remainder of
this work is licensed under [the MIT License](https://opensource.org/licenses/MIT), the full text of which is included
in the [LICENSE.txt](./LICENSE.txt) file in this repository.

## Overview

MilMove is a system to help service members (and other authorized personnel) move their gear and possessions from one
place to another. This codebase has been written to perform load tests on the MilMove app for the purpose of gathering
data about responses times, finding breakpoints, and assessing the overall health of the system.

### `locustfiles/`

[Locust](https://docs.locust.io/en/stable/) uses a python file called a "locustfile" as the base for running a load
test. This directory contains all of the locustfiles for this repo. This file must contain at least one class
definition that inherits from the locust `User` class. Locust will dynamically create instances of these `User` classes
to simulate the request load desired.

Each of these files can be thought of as a different test case for the system, although locust also provides a number of
[config options](https://docs.locust.io/en/stable/configuration.html) to allow you to manipulate which users and/or
tasks run from any given locustfile.

### `tasks/`

Each `User` class needs a set of tasks to complete to be able to run a load test. All tasks are callables that can be
manually set into the `tasks` attribute of the user, or they can be organized into instances of the locust class
`TaskSet` and then associated with a user. This directory contains all of the tasks used in our load tests.

To read more about users and tasks and how they interact, refer to [Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html).

### `utils/`

This directory contains python code and utilities that are do not rely on the locust package. Mixin classes and
constants are located here.

## Getting Started

To create the python virtual environment and install the dependencies from `requirements.txt`, run:

```sh
make setup
```

### Setting up the local environment

To run load tests against a local server, you will need to check out and set up the [MilMove](https://github.com/transcom/mymove)
project. Once you have completed this process, run the following commands to spin up your local environment:

```sh
make db_dev_e2e_populate  ## populates the development database with test data
make server_run
make client_run
```

### Running preset tests

Default tests commands for each locustfile are added to the Makefile to make rerunning common preset tests either. These
commands include:

* `make load_test_prime`

  Runs the load tests for `locustfiles/prime.py`, which test the endpoints in the Prime and Support APIs.

* `make load_test_office`

  Runs the load tests for `locustfiles/office.py`, which tests the MilMove Office interface.

Each of these commands opens the Locust interface for initiating and monitoring the tests, set to [http://localhost:8089](http://localhost:8089).
Using this interface, you can set the number of users to simulate and their hatch rate, then start and stop the test at
will. For the host, you can enter a full URL address, or you can simply enter "local", "staging", or "experimental", and
let the system set the URL as appropriate.

**NOTE: Currently the system only functions in the local environment. You may try the other settings for fun, but don't
expect them to work.**

### Running custom tests

If you need more control over the parameters for a load test, you will need to run a custom locust command. To do so,
you must first activate the virtual environment:

```sh
. .venv/bin/activate
```

Then run a locust command like so:

```sh
locust -f locustfiles/<file_to_test>.py --host <local/staging/experimental>
```

Ex:

```sh
locust -f locustfiles/prime.py --host local
```

To run the test without the web interface, add the `--headless` tag and some guidelines for the test (such as number of
users, their hatch rate, and the time limit for the test):

```sh
locust -f locustfiles/prime.py --headless --host local --users 50 --hatch-rate 5 --run-time 60s
```

To control which tasks run during the test, you can filter using tags:

```sh
locust -f locustfiles/prime.py --tags prime --exclude-tags support
```

To specify which `User` classes are spawned from locustfile, add the class name to the end of the command:

```sh
locust -f locustfiles/prime.py PrimeUser
```

For more CLI config options, refer to the Locust docs for [Configuration](https://docs.locust.io/en/stable/configuration.html).

To deactivate your virtual environment once you have completed testing, enter:

```sh
deactivate
```

## Adding Load Tests

### Starting from scratch

If you are developing load testing for a new MilMove application, or perhaps just designing a new suite of tests, the
first step will be to create a new locustfile in the `locustfiles/` directory.

This where you will define all of the `User` classes for your load tests. A common user might look like:

```python
from locust import HttpUser, between

from utils.constants import MilMoveDomain
from utils.mixins import MilMoveHostMixin


# Use MilMoveHostMixin to easily switch between local, experimental, and staging environments
# HttpUser is the Locust user class we want to use to hit endpoint paths
class MyUser(MilMoveHostMixin, HttpUser):
    """ Here's a short description of what my user does. """

    wait_time = between(1, 9)  # Wait time in between tasks
    tasks = []  # You can define a list of tasks here, add a TaskSet, or define tasks in your MyUser class itself

    # MilMoveHostMixin attributes:
    local_protocol = "http"  # Some local hosts for MilMove don't use HTTPS - you can override the default here
    local_port = "3000"  # The default port you want to use for local testing
    domain = MilMoveDomain.OFFICE  # The domain for the host, if it's one of the default options (MILMOVE, OFFICE, PRIME)
    # NOTE: The domain corresponds to whatever you use in local - so <domain>local
    is_api = True  # Are you testing an API endpoint or path in the interface? This changes the host.
```

This is the bare minimum that you need to have a functional load test. The `MilMoveHostMixin` class is designed to make set up faster and running tests an easier, simpler process. You don't
have to use this structure, however. If it makes sense to create a custom user for your test case, please do so! Please
note that it may be easier to add your customization to the `TaskSet` instead of the `User`, however.

## Load Testing against AWS Experimental Environment

To load test against the AWS Experimental Environment you must modify the
[`DEVLOCAL_AUTH` environment variable](https://github.com/transcom/mymove/blob/master/config/env/experimental.env#L15)
and [deploy the code to the experimental environment](https://github.com/transcom/mymove/blob/master/docs/how-to/deploy-to-experimental.md).

Then you can use the same steps as the development as above as long as you change the `host` parameter in the
`locustfile.py` test classes and point them to the experimental domains:

* [https://my.experimental.move.mil](https://my.experimental.move.mil)
* [https://office.experimental.move.mil](https://office.experimental.move.mil)

### Handling Rate Limiting

Each environment is set to limit the number of requests from a single IP in a 5 minute period. That limit
is usually 2000. For load testing it's likely you'll want a much higher limit, perhaps even 10 times as high. Work
with infrastructure to modify the limit. Here is the diff to apply:

```diff
diff --git a/transcom-ppp/app-experimental/main.tf b/transcom-ppp/app-experimental/main.tf
index 4ef1a29..bac3cf7 100644
--- a/transcom-ppp/app-experimental/main.tf
+++ b/transcom-ppp/app-experimental/main.tf
@@ -65,6 +65,7 @@ module "app" {

   waf_regex_path_disallow_pattern_strings = []
   waf_regex_host_allow_pattern_strings    = [".move.mil$", ".dp3.us$", "^mymove-experimental.sddc.army.mil$"]
+  waf_ip_rate_limit                       = 20000
   wafregional_rule_id                     = "d0ad0bb7-434b-4112-bde0-b5e84b718733"
 }
```

### Metrics

You will want to see metrics from your runs:

* [app-experimental cluster metrics](https://us-west-2.console.aws.amazon.com/ecs/home?region=us-west-2#/clusters/app-experimental/services/app/metrics)
* [app-experimental CloudWatch dashboard](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=mil-experimental)

## References

* [Original Load Testing PR](https://github.com/transcom/mymove/pull/1597)
