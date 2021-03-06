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
         * [static/](#static)
      * [Getting Started](#getting-started)
         * [Requirements](#requirements)
         * [Setup: pre-commit](#setup-pre-commit)
         * [Setup: pyenv](#setup-pyenv)
         * [Setup: virtualenv](#setup-virtualenv)
         * [Alternative Setup: Docker](#alternative-setup-docker)
         * [Troubleshooting](#troubleshooting)
         * [Testing](#testing)
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
         * [Prime API](#prime-api)
         * [MilMove/Office domains](#milmoveoffice-domains)
         * [Handling Rate Limiting](#handling-rate-limiting)
         * [Metrics](#metrics)
      * [References](#references)

<!-- Added by: sandy, at: Fri Jan 15 00:40:16 CST 2021 -->

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

### `static/`

This folder is for static files (certificates, PDFs, etc.) that will be used during load testing.

## Getting Started

### Requirements

* [Homebrew](https://brew.sh)
  * Install with:
  `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* `pre-commit`
* [`pyenv`](https://github.com/pyenv/pyenv) or Docker + `docker-compose` (See: [Alternative Setup: Docker](#alternative-setup-docker))

*Note: These instructions include the relevant commands for MacOS only. Please keep this in mind and be prepared to
search for alternatives if you are running a different OS.*

### Setup: `pre-commit`

Once you have successfully installed Homebrew, you can install `pre-commit` with the command: `brew install pre-commit`.

If you complete the rest of the project's setup as written, installing the required pre-commit hooks and hook libraries
will happen for you automatically. To manually install and test them, you can use the project's Makefile commands:

```shell script
make ensure_pre_commit pre_commit_tests
```

You may also run the equivalent `pre-commit` commands yourself:

```shell script
pre-commit install
pre-commit install-hooks
pre-commit run --all-files
```

### Setup: `pyenv`

This project uses [pyenv](https://github.com/pyenv/pyenv) to manage Python versions. This makes it much easier for devs
to contribute without having to spend hours navigating the spiderweb that is Python versions on MacOS (which most of us
are using).

To ensure that you have all the dependencies for `pyenv` installed, first run:

```shell script
brew install openssl readline sqlite3 xz zlib
```

Once that has completed, you may download and install `pyenv` with the command:

```shell script
curl https://pyenv.run | bash
```

In order to enable `pyenv` to switch which version of Python you are using at any given time (and to enable other neat features),
you will need to paste the following code to your shell's profile file (`~/.bash_profile`, `~/.bashrc`, `~/.zshrc`, etc):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Once you have modified and saved your profile file, you will need to resource your profile:

```shell script
source <profile_file>  # Or just restart your terminal
```

Don't worry about installing or setting specific Python versions at this point - our Makefile commands will do that for
you in the next section.

### Setup: `virtualenv`

To run load testing, you must create and activate a Python virtual environment with all the relevant dependencies installed.
We have several `make` commands that aim to simplify this process for you, but you will need to activate your virtual
environment manually so that the changes are properly pushed to the shell.

First, install and set our required Python version (currently 3.8.3), and create the virtual environment using:

```shell script
make venv
```

You should only need to run this command once. After the initial set up, you should only need to activate your virtual
environment to run any of the other commands for the app. To activate the virtual environment, run:

```shell script
pyenv activate locust-venv
```

Or, to make the virtual environment auto-activate whenever you `cd` into the project folder:

```shell script
pyenv local locust-venv
```

Our default name for the virtual environment is `locust-venv`. You may change this by setting the environment variable
`VENV_NAME` to any name of your choice prior to running `make venv`. Ex:

```shell script
export VENV_NAME=myenv
make venv
pyenv activate myenv
```

Once you have activated your virtual environment using the method of your choice, install requirements and complete the
rest of the setup using:

```shell script
make setup
```

*Note: The requirements are indicated in the `requirements.txt` and `requirements-dev.txt` files. `requirements.txt`
contains the pip-installed requirements needed to run the project. `requirements-dev.txt` contains the requirements to
lint and format our code if you wish to contribute - they are not functional requirements to run the code.*

Once you are done with your virtual environment, you may deactivate it using:

```shell script
pyenv deactivate
```

You do not need to worry about this step if you set your virtual environment as default with `pyenv local`.

If you ever feel the need to completely teardown your virtual environment (uninstalling requirements and deleting all
its files), you may run:

```sh
make teardown
```

Remember to recreate your virtual environment with `make venv` before attempting to continue development on the project.

### Alternative Setup: Docker

It is also possible to run load tests from within a Docker container, eliminating the need to set up a valid python
environment. This requires Docker and `docker-compose` to be installed on your machine. Get them here:

* [Get Docker](https://docs.docker.com/get-docker/)
* [Install Docker Compose](https://docs.docker.com/compose/install/)

To get your load testing Docker container up and running for the local environment, use the following commands:

* `docker-compose -f docker-compose.local.yaml build`
* `docker-compose -f docker-compose.local.yaml up`

And when you are done with testing:

* `docker-compose -f docker-compose.local.yaml build`

You can also use the Makefile equivalents of these commands:

* `make local_docker_build`
* `make local_docker_up`
* `make local_docker_down`

As long as your local MilMove server is up and running, you are ready to run your tests!

### Troubleshooting

If you already had `pyenv` installed on your machine with Homebrew, you may find that your installation doesn't include
the `pyenv-virtualenv` plugin. To fix this, try:

```shell script
brew install pyenv-virtualenv
```

If you encounter compiler issues while installing the required Python version, try:

```shell script
brew unlink binutils
```

### Testing

This project uses [`pytest`](https://docs.pytest.org/en/stable/) as its testing framework. To run the tests, activate
your virtual environment and use the command:

```shell
pytest
```

To see verbose output and any print statments in the tests, use:

```shell
pytest -v -s
```

To run a specific test, use:

```shell
pytest /utils/tests/test_parsers.py
```

If you have a pre-existing installation of `pytest` on your machine, you may need to invoke your system's version of
`python`/`python3` in the command:

```shell
python3 -m pytest -v
```

For more instructions and examples, please read [pytest's documentation](https://docs.pytest.org/en/stable/).

## Running Load Tests

### Setting up the local environment

To run load tests against a local server, you will need to check out and set up the [MilMove](https://github.com/transcom/mymove)
project. Once you have completed this process, run the following commands in the `mymove` directory to spin up your
local environment:

```shell script
make db_dev_e2e_populate  ## populates the development database with test data
make server_run
make client_run
```

Back in `milmove_load_testing`, make sure you activate your virtual environment before attempting to run tests:

```shell script
pyenv activate locust-env
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
will. For the host, you can enter a full URL address, or you can simply enter "local" or "exp" (for experimental), and
let the system set the URL as appropriate.

**NOTE: Currently the system only functions in the local environment. You may try the other settings for fun, but don't
expect them to work.**

### Running custom tests

If you need more control over the parameters for a load test, you will need to run a custom locust command. This will
look something like:

```sh
locust -f locustfiles/<file_to_test>.py --host <local/exp>
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
pyenv deactivate
```

## Adding Load Tests

### Starting from scratch

If you are developing load testing for a new MilMove application, or perhaps just designing a new suite of tests, the
first step will be to create a new locustfile in the `locustfiles/` directory.

This where you will define all of the `User` classes for your load tests. A common user might look like:

```python
from locust import HttpUser, between

from utils.hosts import MilMoveHostMixin, MilMoveDomain


# Use MilMoveHostMixin to easily switch between local and experimental environments
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
  # You can set the host on the class directly. Useful if it never changes based on env.
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
`overrides` for any fields that need to have specific values set, or a boolean `require_all` that indicates that all
fields should be filled, even if not required.

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

### Prime API

To load test against the Prime API in experimental, you will need to install and set up `direnv`, `chamber`, and
`aws-vault`. If you have already set up these tools in order to run the `mymove` project, you do not need to repeat
these steps. Otherwise, please follow the instructions in the `mymove` repo to complete this setup:

* [Setup: `direnv` and `chamber`](https://github.com/transcom/mymove#setup-direnv)
* [Setup: AWS credentials and `aws-vault`](https://github.com/transcom/mymove#setup-aws-services-optional)

Once you have loaded the secrets from `chamber`, which will include the experimental certificate and private key, you
may run your load tests using "exp" as the host value. It is strongly recommended that you set up your `User` classes to
subclass `MilMoveHostMixin` so that your TLS settings are automatically updated when you switch from "local" to "exp."

### MilMove/Office domains

To load test against the AWS Experimental Environment you must modify the
[`DEVLOCAL_AUTH` environment variable](https://github.com/transcom/mymove/blob/master/config/env/exp.app.env#L8)
and [deploy the code to the experimental environment](https://github.com/transcom/mymove/wiki/deploy-to-experimental).

Then, if you have `User` classes that take advantage of the `MilMoveHostMixin` class, you may run your load tests using
"exp" as the host value. If not, make sure to use the experimental domains as your host:

* [https://my.exp.move.mil](https://my.exp.move.mil)
* [https://office.exp.move.mil](https://office.exp.move.mil)

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
