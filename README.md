# MilMove Load Testing

This repository contains code written to run load testing for the
[MilMove](https://github.com/transcom/mymove) application. Load testing is accomplished via the
[Locust](https://docs.locust.io/en/stable/) framework.

## License Information

Works created by U.S. Federal employees as part of their jobs typically are not eligible for
copyright in the United States. In places where the contributions of U.S. Federal employees are not
eligible for copyright, this work is in the public domain. In places where it is eligible for
copyright, such as some foreign jurisdictions, the remainder of this work is licensed
under [the MIT License](https://opensource.org/licenses/MIT), the full text of which is included in
the [LICENSE.txt](./LICENSE.txt) file in this repository.

## Table of Contents

<!-- Table of Contents auto-generated with a `pre-commit` hook, `markdown-toc` -->

<!-- toc -->

* [Overview](#overview)
* [Project Directories](#project-directories)
  * [`ecs/`](#ecs)
  * [`locustfiles/`](#locustfiles)
  * [`scripts`](#scripts)
  * [`static/`](#static)
  * [`tasks/`](#tasks)
  * [`utils/`](#utils)
* [Getting Started](#getting-started)
  * [Base Installation](#base-installation)
    * [Setup: Pyenv and Pipenv](#setup-pyenv-and-pipenv)
    * [Setup: Nix](#setup-nix)
      * [Nix: Dependency Updates](#nix-dependency-updates)
      * [Nix: Disabling Nix](#nix-disabling-nix)
  * [Unsupported Setup](#unsupported-setup)
  * [Troubleshooting](#troubleshooting)
* [Running Tests](#running-tests)
  * [Unit Tests](#unit-tests)
  * [Load Tests](#load-tests)
    * [Load Tests: Local Locust Setup](#load-tests-local-locust-setup)
      * [Local Server Data](#local-server-data)
    * [Load Tests: Running Locust Locally](#load-tests-running-locust-locally)
      * [Running Locust Command](#running-locust-command)
        * [Workflows](#workflows)
      * [Running Preset Load Tests](#running-preset-load-tests)
    * [Load Tests: Running Locust from AWS](#load-tests-running-locust-from-aws)
      * [Troubleshooting: Running Locust from AWS](#troubleshooting-running-locust-from-aws)
* [Adding Load Tests](#adding-load-tests)
  * [Starting from scratch](#starting-from-scratch)
  * [Creating TaskSets](#creating-tasksets)
  * [Adding tasks to existing load tests](#adding-tasks-to-existing-load-tests)
* [AWS Deployed Environment Setup](#aws-deployed-environment-setup)
  * [Deploying to the Load Testing Environment](#deploying-to-the-load-testing-environment)
  * [Resetting the DB After a Load Test](#resetting-the-db-after-a-load-test)
  * [Deploying New Tests](#deploying-new-tests)
* [Fake Data Generation](#fake-data-generation)
  * [Creating a custom parser](#creating-a-custom-parser)
* [Load Testing against the AWS Loadtest Environment](#load-testing-against-the-aws-loadtest-environment)
  * [Prime API](#prime-api)
  * [Handling Rate Limiting](#handling-rate-limiting)
  * [Metrics](#metrics)
* [References](#references)

<!-- Regenerate with "pre-commit run -a markdown-toc" -->

<!-- tocstop -->

## Overview

MilMove is a system to help service members (and other authorized personnel) move their gear and
possessions from one place to another.

This codebase has been written to perform load tests on the MilMove app for the purpose of gathering
data about responses times, finding breakpoints, and assessing the overall health of the system.

## Project Directories

This section covers some high-level notes for some directories included in this repo.

### `ecs/`

This directory contains a representation of the task definition for running the docker container in
AWS. To make changes to the task definition will require changing the terraform in
`transcom/transcom-infrasec-gov-nonato/transcom-gov-dev/app-dev/loadtesting.tf`. This file is
updated manually to reflect the current state.

### `locustfiles/`

[Locust](https://docs.locust.io/en/stable/) uses a python file called a "locustfile" as the base for
running a load test. This directory contains all locustfiles for this repo. This file must contain
at least one class definition that inherits from a locust `User` class (or more likely a subclass).
Locust will dynamically create instances of these `User` classes to simulate the request load
desired.

Each of these files can be thought of as a different test case for the system, although locust also
provides a number of [config options](https://docs.locust.io/en/stable/configuration.html) to allow
you to manipulate which users and/or tasks run from any given locustfile.

In particular, our `locustfiles/all.py` combines all our `User` classes into a single run.

### `scripts`

`aws-session-port-forward.py` - This is the script used to access the deployed locust load testing
container and forward to your local port 4000 accessible
at [http://localhost:4000](http://localhost:4000).

`codebuild` - This script is invoked when making a new build/deployment using the AWS CodeBuild
service. It builds a new docker image and publishes it to ECR so the service can pull down the new
image. It also controls updating the service if there is a new task definition from updating the
Terraform code.

`install_tools` - This script is used in the local set up for this repository if you aren't using
`nix`.

### `static/`

This folder is for static files (certificates, PDFs, etc.) that will be used during load testing.

### `tasks/`

Each `User` class needs a set of tasks to complete to be able to run a load test. All tasks are
callables that can be manually set into the `tasks` attribute of the user, or they can be organized
into instances of the locust class `TaskSet` and then associated with a user. This directory
contains all the tasks used in our load tests.

To read more about users and tasks and how they interact, refer
to [Writing a locustfile](https://docs.locust.io/en/stable/writing-a-locustfile.html).

### `utils/`

This directory contains python code and utilities that help us run our load tests. For example, the
code we use to manage authenticating to the Prime API. Mixin classes, helper functions, and
constants are located here.

## Getting Started

*Note: These instructions include the relevant commands for MacOS only. Please keep this in mind and
be prepared to search for alternatives if you are running a different OS.*

### Base Installation

We have two supported installation methods, `pyenv` and `nix`. Pick which you prefer and proceed to
that section.

#### Setup: Pyenv and Pipenv

1. When setting up for the first time, before you run `direnv allow`, run

    ```shell
    make install_tools
    ```

    1. This will install `pyenv` and `pipenv` along with other tools like `pre-commit`.

2. Restart your terminal.
3. Now run

    ```shell
    direnv allow
    ```

   1. This should install the dependencies via `pipenv` automatically.
   2. If the base dependencies change, you can always re-run this command.

4. Install `pre-commit` hooks:

    ```shell
    make ensure_pre_commit
    ```

#### Setup: Nix

If you need help with this setup, you can ask for help in the
[Truss slack #code-nix channel](https://trussworks.slack.com/archives/C01KTH6HP7D).

1. First read the overview in the
   [Truss Engineering Playbook](https://github.com/trussworks/Engineering-Playbook/tree/main/developing/nix)
   .
2. Follow the installation instructions in the playbook.
3. Ensure you have `direnv` and a modern `bash` installed. To install globally with nix, run:

    ```shell
    nix-env -i direnv bash
    ```

4. To set up the appropriate nix environment variables run:

    ```shell
    direnv allow
    ```

5. Run

    ```shell
    ./nix/update.sh
    ```

6. Install `pre-commit` hooks:

    ```shell
    make ensure_pre_commit
    ```

##### Nix: Dependency Updates

If the nix dependencies change, you should see a warning from direnv:

```text
direnv: WARNING: nix packages out of date. Run nix/update.sh
```

##### Nix: Disabling Nix

Note that if you would like to disable `nix` for this repo, you can do so by creating
a `.nix-disable` file at the top level of this repo and reload your shell.

### Unsupported Setup

Maintaining many ways to set up locally can be time-consuming, which is why we removed the `asdf`
and docker setups.

The `asdf` end set-up was similar to the `pyenv` setup, but required many commands to have tweaks to
work the same as the `pyenv` commands which made them harder to maintain.

As for docker, we had a few reasons for dropping support:

* Locust is a tool that needs to reach the target host and running it from inside docker makes it
  harder to reach a server that is managed outside of docker.
* Docker adds yet another layer for possible issues. We've experienced some problems in the past
  with docker network problems that were masked as locust errors. Errors like this are a pain to
  debug.
* Our current setup using `direnv` and `pipenv` is fairly quick to set up using either `nix` or
  the `make install_tools`
  command, decreasing the "quick setup" case for using docker.

Setups were removed in the following PRs:

* [PR #74](https://github.com/transcom/milmove_load_testing/pull/74)
* [PR #78](https://github.com/transcom/milmove_load_testing/pull/78)
* [PR #89](https://github.com/transcom/milmove_load_testing/pull/89)

### Troubleshooting

If you encounter compiler issues while installing the required Python version, try:

```shell script
brew unlink binutils
```

## Running Tests

There are two types of tests in this repository:

* Load tests which run against the mymove server, whether local or deployed. For more info on these,
  see [Running Load Tests](#load-tests).
* Unit tests which test the helper code we have in this repository. For more info on these, see
  [Running Unit Tests](#unit-tests).

### Unit Tests

These are located is `tests/` directories within the corresponding python package, e.g.
`utils/tests/`. They are mainly here to ensure our setup code is doing what we expect, e.g. testing
that our Prime auth code is setting up certs the way we expect.

This project uses [`pytest`](https://docs.pytest.org/en/stable/) as its testing framework. To run
the tests use the command:

```shell
pytest
```

To see verbose output and any print statements in the tests, use:

```shell
pytest -v -s
```

To run a specific test, use:

```shell
pytest /utils/tests/test_parsers.py
```

For more instructions and examples, please
read [pytest's documentation](https://docs.pytest.org/en/stable/).

### Load Tests

There are several ways you can run load tests. You can run `locust` locally or use the deployed
version. You can also use a local mymove server or the one deployed in the load test environment.
This means you have three possible combinations:

* Run `locust` locally against local mymove server
* Run `locust` locally against load test env mymove server
* Run `locust` from AWS against the load test env mymove server

If you run `locust` locally, you have the option of running with or without the `locust` UI. If you
run `locust` from AWS, you will only have the option of running with the UI. The instructions in the
following sections will cover how to get `locust` started (with or without the UI), but won't cover
much about the UI since the
[locust web interface docs](https://docs.locust.io/en/stable/quickstart.html#locust-s-web-interface)
cover a decent amount of helpful information.

#### Load Tests: Local Locust Setup

You only need to do this section if you plan on running against a local mymove server. If you are
going to run against the load test env mymove server, then you can skip to the
[Running Locust Locally](#load-tests-running-locust-locally) section.

You will need to check out and set up the [MilMove](https://github.com/transcom/mymove) project.

Follow the setup instructions in the mymove README, all the way through running the local server
(`make server_run`). You don't need to run the user interface in order to run load tests (so you can
skip the `make client_run` step), unless you would like to be able to log in and look at data using
the mymove UI.

##### Local Server Data

Our goal is to eventually have all the data we need set up by the load tests, but until that's done,
you should populate the mymove server with data using this command (in the mymove repo directory):

```shell
make db_dev_e2e_populate  ## populates the development database with test data
```

#### Load Tests: Running Locust Locally

This section covers running `locust` locally, whether pointing at a local mymove server or the load
test env mymove server. We specify which we want to point at by defining the `host`. So if you want
to run locally, you'll use `local`, while the load test env will use the `dp3` value. You can define
the host either in the UI in the appropriate field, or via the command line using the `--host`
option, e.g. `--host local`.

You can invoke the `locust` command directly to run the load tests, or you can use some presets we
have defined in the `Makefile`.

##### Running Locust Command

If you want more control over the parameters for a load test, you will need to invoke the `locust`
command directly. This will look something like:

```sh
locust -f <path_to_locustfile>.py --host <local/dp3>
```

Ex:

```sh
locust -f locustfiles/prime.py --host local
```

To run the test without the web interface you will need to specify a few things that would otherwise
have been input via the interface.

* Add the `--headless` tag to turn off the UI
* Add the `-u` (or `--users`) option to specify the total number of users.
* Add the `-r` (or `--spawn-rate`) option to specify the number of users that should be added per
  second.
* Add the `-t` (or `--run-time`) option to specify how long the tests should run for, e.g. (300s,
  20m, 3h, 1h30m, etc.)

There are other options that can be useful such as:

* `-T` (or `--tags`) to specify which load tests to run based on their tags.
  * You can see a load test's tag by looking at the task definition and looking for `@tag("myTag")`
    * So in this case you would use `-T myTag`
* `-E` (or `--exclude-tags`) to specify which load tests to exclude based on their tags.

The command will also take a list (or single one) of `User` classes at the end.

So a full command could look like:

```shell
locust -f locustfiles/prime.py --host local --headless -u 1000 -r 50 -t 30s -T listMoves PrimeUser
```

You can see more information on the
[locust running without the web UI docs](https://docs.locust.io/en/stable/running-without-web-ui.html#running-without-web-ui).

For more CLI config options, refer to the
[locust configuration docs](https://docs.locust.io/en/stable/configuration.html).

###### Workflows

There are several workflows defined as tags, so you can use those tags in the `locust` command as
shown above. Listed below are the available workflows tags to test.

Prime API Workflow Tags

* `hhgMove`
  * This workflow simulates how an HHG move would flow through the PrimeAPI. This workflow
    utilizes both PrimeAPI and SupportAPI tasks.
* `createMTOShipmentWorkflow`
  * This work flow tests the PrimeAPI create_mto_shipment endpoint. It creates or selects an
    existing move, then creates shipments on the selected move.

##### Running Preset Load Tests

Default tests commands for each locustfile are available in the Makefile to make rerunning common
preset tests easier. These all use the UI and default to the `local` host (but the host can be
changed in the UI). These commands include:

* Prime and Support API load tests - runs the load tests for `locustfiles/prime.py`:

  ```shell
  make load_test_prime
  ```

* Office/GHC API load tests - runs the load tests for `locustfiles/office.py`

  ```shell
  make load_test_office
  ```

* Customer/Internal API load tests - runs load tests for `locustfiles/milmove.py`

  ```shell
  make load_test_milmove
  ```

Each of these commands opens the Locust interface for initiating and monitoring the tests, set
to <http://localhost:8089>. Using this interface, you can set the number of users to simulate, their
spawn rate, and the host to target. Then start and stop the test at will.

#### Load Tests: Running Locust from AWS

1. Run the port-forwarding script:

    ```sh
    aws-vault exec $AWS_PROFILE -- ./scripts/aws-session-port-forward.py
    ```

2. You can then visit <http://localhost:4000> and run tests from AWS.

##### Troubleshooting: Running Locust from AWS

You may see the following errors:

* `SessionManagerPlugin is not found`. If you do please follow the link and the instructions to
  install the Session Manager plugin or reference
  [the Session Manager plugin installation guide](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html#install-plugin-macos)
  directly.

* An error mentioning `credentials missing`.
  * If there is an additional reference to a specific profile. If this is the case please add the
    corresponding entry from
    [this AWS config template](https://dp3.atlassian.net/wiki/spaces/MT/pages/1348927493/AWS+GovCloud+Config+Templates)
    to your `~/.aws/config` file.
  * If you only see an error mentioning `credentials missing` without an additional reference to a
    specific profile, please ensure that your $AWS_PROFILE variable is not blank. This can be set by
    running:

    ```shell
    direnv allow
    ```

## Adding Load Tests

### Starting from scratch

If you are developing load testing for a new MilMove application, or perhaps just designing a new
suite of tests, the first step will be to create a new locustfile in the `locustfiles/` directory.

This where you will define all of the `User` classes for your load tests. A common user might look
like:

```python
from locust import HttpUser, between

from utils.hosts import MilMoveHostMixin, MilMoveDomain


# Use MilMoveHostMixin to easily switch between local and dp3 environments
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

  # If not using MilMoveHostMixin:
  # You can set the host on the class directly. Useful if it never changes based on env.
  host = "https://primelocal:9443"
```

This is the bare minimum that you need to have a functional load test. The `MilMoveHostMixin` class
is designed to make set up faster and running tests an easier, simpler process. You don't have to
use this structure, however. If it makes sense to create a custom user for your test case, please do
so! Please note that it may be easier to add your customization to the `TaskSet` instead of
the `User`, however.

### Creating TaskSets

Tasks are distinct functions, or callables, that tell Locust what to do during load
testing. `TaskSet` classes are a clean way to link tasks together and keep the code organized. You
can link a `User` class with a task set using the following syntax in the `tasks` attribute:

```python
tasks = {MyMainTaskSet: 5, MyOtherTaskSet: 1}
```

The number next to the task set indicates its relative _weight_ - so in this example, tasks
from `MyMainTaskSet` would be 5 times more likely than tasks from `MyOtherTaskSet`. Task sets and
functions should all be defined in python files in the `tasks/` directory. An example `TaskSet` for
this project might be:

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
    resp = self.client.post("/my-path-here/update-user", data=json.dumps(request_body),
                            headers=headers)

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

* `SequentialTaskSet` - Locust base class, asserts that all of the tasks in the `TaskSet` are
  executed in the order in which they are defined (instead of randomly)

* `LoginTaskSet` - in `tasks/base.py`, adds code for logging into the MilMove Office and MyMove
  interfaces. To use it, you can add an `on_start` definition to your `TaskSet` like so:

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

* `CertTaskMixin` - in `tasks/base.py`, accounts for the use of a `cert_kwargs` attribute defined on
  the `User`-level that can then be passed in as validation during the request. Ex:

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

There are multiple other ways to organize and link tasks together, but using `TaskSet` classes is
the main recommendation in this repo. If you need to do something different, however, Locust's
documentation is a great place to get started:
[https://docs.locust.io/en/stable/writing-a-locustfile.html#tasks](https://docs.locust.io/en/stable/writing-a-locustfile.html#tasks)

### Adding tasks to existing load tests

Adding a task to an existing load test is thankfully a fairly straight-forward process that requires
just a bit of research and just a bit of coding. Here are the general steps:

* Locate the locust file your test needs to be run from.
* Figure out which user class (if multiple) that will run your task.
  * Generally a `HttpUser` only has one host to use as the base for its tasks, so find the one with
    the right host for your endpoint.
* Pick a `TaskSet` used by the user for your task.
  * This should make sense thematically, but using clues like if the tasks in a `TaskSet` use the
    same login or certificates that you need for your task, then that's probably the place to be.
  * But keep in mind that it may not make sense in any of the current task sets - or maybe
    the `TaskSet` is used in multiple places and you don't want to affect other load tests in the
    system. In that case, you should create a new one.
* Add a function with the code for your task to the `TaskSet`. Make sure to decorate it with `@task`
  .
  * You should also decorate it with any tags you think are relevant to this task. Look at some of
    the other tags for this user to give you an idea of what you have to work with. This should look
    like `@tag('tag1', 'tag2')` either directly above or below the `@task` decorator.
* Run the load test and check that your task is working properly.
  * If it is, you're good to go!

## AWS Deployed Environment Setup

### Deploying to the Load Testing Environment

Refer to
these [instructions](https://dp3.atlassian.net/wiki/spaces/MT/pages/1470922798/How+to+deploy+to+Experimental+or+Demo+or+Loadest)

### Resetting the DB After a Load Test

Refer to
these [instructions](https://dp3.atlassian.net/wiki/spaces/MT/pages/1469284356/Atlantis+Restore+Post-Load+Testing)

### Deploying New Tests

Refer to
these [instructions](https://dp3.atlassian.net/wiki/spaces/MT/pages/1512603655/Deploying+load-tests+to+AWS#Instructions)

## Fake Data Generation

This repo also contains a tool to generate fake data for creating dynamic request bodies and
simulating more varied user behavior, the `APIParser` class. It parses an API `.yaml` file using a
path or URL using the `prance` library to create a fully-resolved dictionary of its Swagger
specification. The main methods are:

* `get_request_body`: Returns the full Swagger specification of the request body for a given
  endpoint. Requires the
  `path` and the `method` (post, get, etc) to be passed in. Returns an empty dictionary if no
  matching request found.

```python
from utils.parsers import APIParser


parser = APIParser(
  api_file="https://raw.githubusercontent.com/transcom/mymove/master/swagger/prime.yaml")
parser.get_request_body(path="/mto-shipments", method="post")
```

* `get_response_body`: Returns the full Swagger specification of the response for a given endpoint.
  Requires the
  `path` and the `method` (post, get, etc). Optionally accepts the `status` code for the response,
  which defaults to
  `"200"`. Returns an empty dictionary if no matching response is found.

```python
parser.get_response_body(path="/mto-service-items", method="post", status="201")
```

* `get_definition`: Returns the full Swagger specification for a specific definition. Requires
  the `name` of the definition to be passed in. Returns `None` if no matching definition is found.

```python
parser.get_definition(name="MoveTaskOrder")
```

* `generate_fake_request`: Takes in the endpoint `path` and `method` and returns a JSON-ready
  dictionary with the fields and fake data for the request. Uses the `faker` library to generate the
  data. Can optionally accept a dictionary of
  `overrides` for any fields that need to have specific values set, or a boolean `require_all` that
  indicates that all fields should be filled, even if not required.

```python
parser.generate_fake_request(path="/mto-service-items", method="post",
                             overrides={"modelType": "MTOServiceItemDDSFIT"})
```

### Creating a custom parser

The `APIParser` class is designed to be inherited and customized for specific APIs. To start, go to
the bottom of the
`utils/parsers.py` file and create a new class with the link to your API YAML file:

```python
class GHCAPIParser(APIParser):
  """ Parsing the GHC API as an example: """

  api_file = "https://raw.githubusercontent.com/transcom/mymove/master/swagger/ghc.yaml"
```

The `APIParser` has three built-in hook methods that are designed to make it easier to implement
custom data manipulation in your parser class:

```python
class GHCAPIParser(APIParser):
  ...

  def _custom_field_validation(self, api_field, object_def):
    """
    This hook is for changes you want to make to a specific field, regardless of which endpoint it is used in.
    These are PRE-DATA changes and will be used to generate the data you want for this field whenever you call the
    generate_fake_data method.
    """
    # Example:
    if api_field.name == "agents":
      try:
        api_field.max_items == 2  # let's say we never want more than two agents, regardless of what the YAML says
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

Next, instantiate the parser in your `locustfile` and reference it in the `parser` attribute on
your `User` class:

```python
from utils.parsers import GHCAPIParser


ghc_parser = GHCAPIParser()

GHCUser(...):
...

parser = ghc_parser
```

Instantiating it once at the beginning of the `locustfile` keeps the API from being reparsed over
and over, saving you valuable processing time.

## Load Testing against the AWS Loadtest Environment

### Prime API

To load test against the Prime API in the load test environment, you will need to install and set
up `direnv`, `chamber`, and
`aws-vault`. If you have already set up these tools in order to run the `mymove` project, you do not
need to repeat these steps. Otherwise, please follow the instructions in the `mymove` repo to
complete this setup:

* [Setup: `direnv` and `chamber`](https://github.com/transcom/mymove#setup-direnv)
* [Setup: AWS credentials and `aws-vault`](https://github.com/transcom/mymove#setup-aws-services-optional)

Once you have loaded the secrets from `chamber`, which will include the dp3 certificate and private
key, you may run your load tests using "dp3" as the host value. It is strongly recommended that you
set up your `User` classes to subclass `MilMoveHostMixin` so that your TLS settings are
automatically updated when you switch from "local" to "dp3"

### Handling Rate Limiting

Each environment is set to limit the number of requests from a single IP in a 5 minute period. The
limit for the load testing environment is 2000. If this ever needs to be updated, work with
infrastructure to modify the limit. The limit is set
in [transcom-infrasec-gov-nonato/transcom-gov-milmove-loadtest/app-loadtest/main.tf](https://github.com/transcom/transcom-infrasec-gov-nonato/blob/main/transcom-gov-milmove-loadtest/app-loadtest/main.tf)
by this code:

```sh
 waf_ip_rate_limit   = 20000
```

### Metrics

To view metrics follow documentation
for [Viewing OTel logs in Load Test Environment](https://dp3.atlassian.net/wiki/spaces/MT/pages/1520533505/Viewing+Otel+Logs+in+Load+Testing+Environment)

## References

* [Locust Documentation](https://docs.locust.io/en/stable/index.html)
* [Prance Documentation](https://pypi.org/project/prance/)
* [Faker Documentation](https://faker.readthedocs.io/en/stable/index.html)
* [Original Load Testing PR](https://github.com/transcom/mymove/pull/1597)
