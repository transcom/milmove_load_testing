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

    # Required attributes:

    # The time (in seconds) Locust waits in between tasks. Can use decimals.
    wait_time = between(1, 9)
    # The list of tasks for this user. You can use a TaskSet or define tasks in your MyUser class itself.
    tasks = []

    # MilMoveHostMixin attributes:

    # Some local hosts for MilMove don't use HTTPS - you can override that default here:
    local_protocol = "http"
    # The default port you want to use for local testing:
    local_port = "3000"
    # The domain for the host, if it's one of the default options (MILMOVE, OFFICE, PRIME)
    # NOTE: The domain corresponds to whatever you use in local - so <domain>local
    domain = MilMoveDomain.OFFICE
    # Are you testing an API endpoint or path in the interface? This changes the host:
    is_api = True

    # If not using MilMoveHostMixin:

    # Can set the host on the class directly. Useful if it never changes based on env.
    host = "https://primelocal:9443"
```

This is the bare minimum that you need to have a functional load test. The `MilMoveHostMixin` class is designed to make set up faster and running tests an easier, simpler process. You don't
have to use this structure, however. If it makes sense to create a custom user for your test case, please do so! Please
note that it may be easier to add your customization to the `TaskSet` instead of the `User`, however.

### Creating TaskSets

Tasks are distinct functions, or callables, that tell Locust what to do during load testing. `TaskSet` classes are a
clean way to link tasks together and keep the code organized. You can link a `User` class with a task set using the
following syntax in the `tasks` attribute:

```python
tasks = {MyMainTaskSet: 5, MyOtherTaskSet: 1}
```

The number next to the task set indicates its relative _weight_ - so in this example, tasks from `MyMainTaskSet` would
be 5 times more likely than tasks from `MyOtherTaskSet`. Task sets and functions should all be defined in python files
in the `tasks/` directory. An example `TaskSet` for this project might be:

```python
import logging
import json

from locust import TaskSet, task

logger = logging.getLogger(__name__)


class MyTasks(TaskSet):
    """
    Description of the flow for these tasks here.
    """

    def on_start(self):
        """
        Description of functionality that runs whenever the task set is initialized.
        """
        # Set up tasks might go here, like:
        # - logging in
        # - grabbing cookies
        # - setting shared headers

    @task
    def do_something(self):
        """
        Do a task! Tasks generally have three steps: Set-up, make a request, validate/log results
        """
        # First, complete any set up you need:
        request_body = {
            "userName": "squidGirl1992",
            "email": "actual-squid-scientist@marinebiology.edu"
        }
        headers = {"content-type": "application/json"}

        # Next, make the request:
        resp = self.client.post("/my-path-here/update-user", data=json.dumps(request_body), headers=headers)

        # Lastly, validate the response and/or log any relevant info:
        logger.info(f"ℹ️ Status code: {resp.status_code}")

        try:
            json_body = json.loads(resp.content)
        except (json.JSONDecodeError, TypeError):
            logger.exception("Non-JSON response")
        else:
            logger.info(f"ℹ️ User's most liked post: {json_body['best_post']}")
```

There are a couple of base `TaskSet` classes that you may also want to take advantage of:

* `SequentialTaskSet` - Locust base class, asserts that all of the tasks in the `TaskSet` are executed in the order in
which they are defined (instead of randomly)
* `CertTaskSet` - in `tasks/base.py`, accounts for the use of a `cert_kwargs` attribute defined on the `User`-level that
can then be passed in as validation during the request. Ex:

Add this as an attribute to your user:

```python
# MyUser
cert_kwargs = {'cert': ("path_to_my_cert", "path_to_my_key"), "verify": True}
```

Then in your task, write your request like so:

```python
# MyTasks.get_something
self.client.get("/path", **self.user.cert_kwargs)
```

* `LoginTaskSet` - in `tasks/base.py`, adds code for logging into the MilMove Office and MyMove interfaces. To use it,
you can add an `on_start` definition to your `TaskSet` like so:

```python
class MyLoggedInTasks(LoginTaskSet):

    def on_start(self):
        """
        Creates a login right at the start of the TaskSet and stops task execution if the login fails.
        """
        super().on_start()  # sets the csrf token

        resp = self._create_login(user_type="my_user_type", session_token_name="my_token_name")
        if resp.status_code != 200:
            self.interrupt()  # if we didn't successfully log in, there's no point attempting the other tasks
```

There are multiple other ways to organize and link tasks together, but using `TaskSet` classes is the main recommendation
in this repo. If you need to do something different, however, Locust's documentation is a great place to get started:
[https://docs.locust.io/en/stable/writing-a-locustfile.html#tasks](https://docs.locust.io/en/stable/writing-a-locustfile.html#tasks)

### Adding tasks to existing load tests

Adding a task to an existing load test is thankfully a fairly straight-forward processs that requires just a bit of
research and just a bit of coding. Here are the general steps:

* Locate the locust file your test needs to be run from.
* Figure out which user class (if multiple) that will run your task.
  * Generally a `HttpUser` only has one host to use as the base for its tasks, so find the one with the right host for
  your endpoint.
* Pick a `TaskSet` used by the user for your task.
  * This should make sense thematically, but using clues like if the tasks in a `TaskSet` use the same login or certificates
  that you need for your task, then that's probably the place to be.
  * But keep in mind that it may not make sense in any of the current task sets - or maybe the `TaskSet` is used in multiple
  places and you don't want to affect other load tests in the system. In that case, you should create a new one.
* Add a function with the code for your task to the `TaskSet`. Make sure to decorate it with `@task`.
  * You should also decorate it with any tags you think are relevant to this task. Look at some of the other tags for this
  user to give you an idea of what you have to work with. This should look like `@tag('tag1', 'tag2')` either directly
  above or below the `@task` decorator.
* Run the load test and check that your task is working properly.
  * If it is, you're good to go!

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

* [Locust Documentation](https://docs.locust.io/en/stable/index.html)
* [Prance Documentation](https://jfinkhaeuser.github.io/prance/index.html#)
* [Faker Documentation](https://faker.readthedocs.io/en/stable/index.html)
* [Original Load Testing PR](https://github.com/transcom/mymove/pull/1597)
