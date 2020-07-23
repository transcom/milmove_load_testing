# MilMove Load Testing

This repository contains code written to run load testing for the [MilMove](https://github.com/transcom/mymove) application.
Load testing is accomplished via the [Locust](https://docs.locust.io/en/stable/) framework.

## License Information

Works created by U.S. Federal employees as part of their jobs typically are not eligible for copyright in the United
States. In places where the contributions of U.S. Federal employees are not eligible for copyright, this work is in
the public domain. In places where it is eligible for copyright, such as some foreign jurisdictions, the remainder of
this work is licensed under [the MIT License](https://opensource.org/licenses/MIT), the full text of which is included
in the [LICENSE.txt](./LICENSE.txt) file in this repository.

## Table of Contents

<!-- Uses gh-md-toc to generate Table of Contents: https://github.com/ekalinin/github-markdown-toc -->
<!-- markdownlint-disable -->
<!--ts-->
   * [MilMove Load Testing](#milmove-load-testing)
      * [License Information](#license-information)
      * [Table of Contents](#table-of-contents)
      * [Overview](#overview)
         * [locustfiles/](#locustfiles)
         * [tasks/](#tasks)
         * [utils/](#utils)
      * [Getting Started](#getting-started)
         * [Requirements](#requirements)
         * [Alternate Setup](#alternate-setup)
      * [Running Load Tests](#running-load-tests)
         * [Setting up the local environment](#setting-up-the-local-environment)
         * [Running preset tests](#running-preset-tests)
         * [Running custom tests](#running-custom-tests)
      * [Adding Load Tests](#adding-load-tests)
         * [Starting from scratch](#starting-from-scratch)
         * [Creating TaskSets](#creating-tasksets)
         * [Adding tasks to existing load tests](#adding-tasks-to-existing-load-tests)
      * [Fake Data Generation](#fake-data-generation)
         * [Creating a custom parser](#creating-a-custom-parser)
      * [Load Testing against AWS Experimental Environment](#load-testing-against-aws-experimental-environment)
         * [Handling Rate Limiting](#handling-rate-limiting)
         * [Metrics](#metrics)
      * [References](#references)

<!-- Added by: sandy, at: Tue Jul 14 14:09:41 CDT 2020 -->

<!--te-->
<!-- markdownlint-restore -->

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

### Requirements

If you wish to use the custom setup commands in our Makefile, you will need to install:

* Homebrew
* Python 3.8
* `pip`
* `pre-commit`

These may be installed using the method of your choice, although we strongly recommend using `brew install`. Note that
`brew install python3` will also install `pip3` (the Py3 version of `pip`). If you use `pip3` instead of `pip`, you may
need to create an alias before running our setup commands:

```shell script
alias pip="pip3"
```

To create the python virtual environment and install the dependencies from `requirements.txt` and
`requirements-dev.txt`, run:

```sh
make setup
```

NOTE: `requirements.txt` contains the pip-installed requirements needed to run the project. `requirements-dev.txt`
contains the requirements to lint and format our code if you wish to contribute. They are not functional requirements to
run the code.

Once you are done with your virtual environment, you may want to remove all environment files. To do this, run:

```sh
make teardown
```

To quickly teardown and setup a project when switching branches, run:

```sh
make rebuild
```

### Alternate Setup

You can run this project with a custom setup that doesn't make use of our Makefile commands. **If you encounter any issues
with the Makefile `make setup` command, you will want to use this method.** To do so, you need the following tools:

* Python 3.8
* `pip`
* `virtualenv` -> installed via `pip install virtualenv`

To setup your virtual environment and install the `requirements.txt` dependencies:

```shell script
$ virtualenv --python=python3.8 .venv
$ . .venv/bin/activate
(venv) $ pip install -r requirements.txt
```

Once you have done this, you will be able to interact with the system the same way as with the `make setup` command. You
may want to default to using the locust CLI instead of the `make` commands, however.

## Running Load Tests

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

* `make load_test_milmove`

    Runs the load tests for `locustfiles/milmove.py`, which tests the MilMove Customer interface.

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

* `CertTaskMixin` - in `tasks/base.py`, accounts for the use of a `cert_kwargs` attribute defined on the `User`-level that
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

## Fake Data Generation

This repo also contains a tool to generate fake data for creating dynamic request bodies and simulating more varied user
behavior, the `APIParser` class. It parses an API `.yaml` file using a path or URL using the `prance` library to create
a fully-resolved dictionary of its Swagger specification. The main methods are:

* `get_request_body`: Returns the full Swagger specification of the request body for a given endpoint. Requires the
`path` and the `method` (post, get, etc) to be passed in. Returns an empty dictionary if no matching request found.

```python
from utils.parsers import APIParser

parser = APIParser(api_file="https://raw.githubusercontent.com/transcom/mymove/master/swagger/prime.yaml")
parser.get_request_body(path="/mto-shipments", method="post")
```

* `get_response_body`: Returns the full Swagger specification of the response for a given endpoint. Requires the
`path` and the `method` (post, get, etc). Optionally accepts the `status` code for the response, which defaults to
`"200"`. Returns an empty dictionary if no matching response is found.

```python
parser.get_response_body(path="/mto-service-items", method="post", status="201")
```

* `get_definition`: Returns the full Swagger specification for a specific definition. Requires the `name` of the
definition to be passed in. Returns `None` if no matching definition is found.

```python
parser.get_definition(name="MoveTaskOrder")
```

* `generate_fake_request`: Takes in the endpoint `path` and `method` and returns a JSON-ready dictionary with the fields
and fake data for the request. Uses the `faker` library to generate the data. Can optionally accept a dictionary of
`overrides` for top-level fields that should have specific fields, a dictionary of `nested_overrides` for fields in
child objects that should have specific data, or a boolean `require_all` that indicates that all fields should be
filled, even if not required.

```python
parser.generate_fake_request(path="/mto-service-items", method="post", overrides={"modelType": "MTOServiceItemDDSFIT"})
```

### Creating a custom parser

The `APIParser` class is designed to be inherited and customized for specific APIs. To start, go to the bottom of the
`utils/parsers.py` file and create a new class with the link to your API YAML file:

```python
class GHCAPIParser(APIParser):
    """ Parsing the GHC API as an example: """

    api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/ghc.yaml"
```

The `APIParser` has three built-in hook methods that are designed to make it easier to implement custom data
manipulation in your parser class:

```python
class GHCAPIParser(APIParser):
    ...

    def _custom_field_validation(self, field, object_def):
        """
        This hook is for changes you want to make to a specific field, regardless of which endpoint it is used in.
        These are PRE-DATA changes and will be used to generate the data you want for this field whenever you call the
        generate_fake_data method.
        """
        # Example:
        if field.name == "agents":
            try:
                field.max_items == 2  # let's say we never want more than two agents, regardless of what the YAML says
            except AttributeError:
                pass  # this wasn't the field type we were expecting -- should log as well

    def _custom_body_validation(self, body):
        """
        This hook is for changes you want to make to a specific APIEndpointBody class (defined in utils/fields.py).
        These are PRE-DATA changes and will be used to generate the data you want for this endpoint whenever you call
        the generate_fake_data method.
        """
        # Example:
        if body.path.endswith("status") and body.method == "patch":
            if body.body_field.object_fields:  # make sure we have the right BaseAPIField type
                status_field = body.body_field.get_field("status")
                if status_field and status_field.options:  # check that we have the field and it is an EnumField
                    try:
                        # status will already be SUBMITTED and can't be changed back, so let's just remove that option:
                        status_field.options.remove("SUBMITTED")
                    except ValueError:
                        pass  # it's not in the list, so we're good

    def _custom_request_validation(self, path, method, request_data):
        """
        This hook is for changes you want to make to the data for a specific endpoint AFTER generation. This code
        manipulates actual data and may not apply to every request.
        """
        # Example:
        if path == "/move-task-orders/{moveTaskOrderID}" and method == "patch":
            if request_data.get("isCanceled"):  # check if this value was set and if it's True
                request_data["availableToPrimeAt"] = None
```

Next, instantiate the parser in your `locustfile` and reference it in the `parser` attribute on your `User` class:

```python
from utils.parsers import GHCAPIParser

ghc_parser = GHCAPIParser()


GHCUser(...):
    ...

    parser = ghc_parser
```

Instantiating it once at the beginning of the `locustfile` keeps the API from being reparsed over and over, saving you
valuable processing time.

Next, navigate to your `TaskSet` class and add the `ParserTaskMixin` to its inheritance:

```python
from tasks.base import ParserTaskMixin


GHCTaskSet(ParserTaskMixin, ...):  # ParserTaskMixin needs to be BEFORE the other classes in the MRO
```

This gives you access to the `self.fake_request` method, and now you can generate a request body filled with fake data:

```python
GHCTaskSet(ParserTaskMixin, ...):
    ...

    @task
    def update_move_task_order(self):
        mtoID = "5d4b25bb-eb04-4c03-9a81-ee0398cb779e"
        payload = self.fake_request(path="/move-task-orders/{moveTaskOrderID}", method="patch")

        response = self.client.patch(
            f"/ghc/v1/move-task-orders/{mtoID}",
            name="/ghc/v1/move-task-orders/{moveTaskOrderID}",
            data=json.dumps(payload),
            headers={"content-type": "application/json"},
        )

        # Now process the response however you like:
        print(response.status_code, response.content)
```

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
