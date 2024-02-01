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
  * [`scripts/`](#scripts)
  * [`static/`](#static)
  * [`tasks/`](#tasks)
  * [`utils/`](#utils)
  * [`utils/flows/`](#utilsflows)
  * [`utils/flows/steps`](#utilsflowssteps)
* [Getting Started](#getting-started)
  * [Base Installation](#base-installation)
    * [Setup: Pyenv and Pipenv](#setup-pyenv-and-pipenv)
    * [Setup: Nix](#setup-nix)
      * [Nix: Dependency Updates](#nix-dependency-updates)
      * [Nix: Disabling Nix](#nix-disabling-nix)
  * [Updating Python Dependencies](#updating-python-dependencies)
  * [Unsupported Setup](#unsupported-setup)
  * [Troubleshooting](#troubleshooting)
* [Updating Python Version](#updating-python-version)
* [Updating Pipenv Version](#updating-pipenv-version)
* [OpenAPI Generator](#openapi-generator)
  * [Regenerating the client code as the server API evolves](#regenerating-the-client-code-as-the-server-api-evolves)
* [Running Locust Locally](#running-locust-locally)
* [Running Tests](#running-tests)
  * [Unit Tests](#unit-tests)
* [Reports](#reports)

<!-- Regenerate with "pre-commit run -a markdown-toc" -->

<!-- tocstop -->

## Overview

MilMove is a system to help service members (and other authorized personnel) move their gear and
possessions from one place to another.

This codebase has been written to perform load tests on the MilMove app for the purpose of gathering
data about responses times, finding breakpoints, and assessing the overall health of the system.

The documentation in this README is focused on the repo structure, setting up your local environment,
and running unit tests. Documentation on `locust`, how we use it, and running the load tests can be
found in the [mymove locust docs](https://transcom.github.io/mymove-docs/docs/tools/locust/locust).

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

As of 2022-05-25, the `locustfiles/queue.py` is the recommended way to
run the load tests.

### `scripts/`

`aws-session-port-forward.py` - This is the script used to access the deployed locust load testing
container and forward to your local port 4000 accessible
at [http://localhost:4000](http://localhost:4000).

`codebuild` - This script is invoked when making a new build/deployment using the AWS CodeBuild
service. It builds a new docker image and publishes it to ECR so the service can pull down the new
image. It also controls updating the service if there is a new task definition from updating the
Terraform code.

`install_tools` - This script is used in the local set up for this repository if you aren't using
`nix`.

`regenerate-swagger-client` - We are using
[openapi-generator](https://github.com/OpenAPITools/openapi-generator)
to generate python code that uses the milmove API. See the OpenAPI
Generator section below for more information

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

### `utils/flows/`

This directory contains different move "flows" that exercise a move
end to end through the system through the different roles (service
member, service counselor, TOO, prime).

You can run a flow outside of locust when developing/testing. For
example, try

  PYTHONPATH=$PWD python utils/flows/simple_hhg.py

### `utils/flows/steps`

This directory contains steps to support each flow.

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
   1. If you see something similar to the following

   ```shell
    direnv: loading ~/Projects/milmove_load_testing/.envrc
    direnv: Want to load secrets from chamber? 'ln -s .envrc.chamber.template .envrc.chamber'
    /bin/bash:979: pipenv: command not found
    /bin/bash:980: pipenv: command not found
   ```
   
   Then please run `install_tools` again.

3. Now run

    ```shell
    direnv allow
    ```

   1. This should install the dependencies via `pipenv` automatically.

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

If the python version changes, you may need to do `pipenv --rm` and
then something like `cd / && cd -`

##### Nix: Disabling Nix

Note that if you would like to disable `nix` for this repo, you can do so by creating
a `.nix-disable` file at the top level of this repo and reload your shell.

### Updating Python Dependencies

1. If the python dependencies get updated (`Pipfile` and/or `Pipfile.lock` files change), you can
  update your local environment by running:

    ```shell
    make install_python_deps
    ```

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

## Updating Python Version

To update python to a new version, you need to modify multiple files:

1. `.circleci/config.yml` Update the `cimg/python` version
1. `Dockerfile` Update the `FROM` at the top
1. `Pipfile` Update the `python_full_version` near the bottom
1. `frew-brew.local` Update the `python_version` near the top
1. `nix/default.nix` Update the python stanza from [nix package search](https://ahobson.github.io/nix-package-search/#/search)
1. Update the `load_tester` image in the `mymove/.circleci/config.yml`
   to the right version

NOTE: nix installs pipenv with its own bundled version of python, but
pipenv can create virtual envs for other versions of python.

## Updating Pipenv Version

We want to lock our pipenv version to ensure consistent behavior

1. `Dockerfile` Update the `RUN pip install` line
1. `nix/default.nix` Update the pipenv stanza from [nix package search](https://ahobson.github.io/nix-package-search/#/search)

## OpenAPI Generator

We are using
[openapi-generator](https://github.com/OpenAPITools/openapi-generator)
to generate python client code for interacting with the milmove API.

### Regenerating the client code as the server API evolves

Run `./scripts/regenerate-swagger-client` to build the newest version
of the files. They will be saved to `./openapi_client`.

One of the biggest challenges with this approach is that the swagger
definitions on milmove frequently do not match what is actually
returned my milmove. This is very definitely buggy behavior by the
milmove app, and so we try to work around it where we can.

## Running Locust Locally

To run locust on your local machine against a milmove instance running
on your local machine, use `make server_run` in the milmove directory
and then in another  shell in this repo, run

  locust -f locustfiles/queue.py --host local -u 10

Or, to run headless for 30 seconds and print the results, do

  locust -f locustfiles/queue.py --host local -u 10 -t 30s --headless

You should always see 0% failures.

## Running Tests

There are two types of tests in this repository:

* Load tests which run against the mymove server, whether local or deployed. For more info on these,
  see [Running Load Tests](https://transcom.github.io/mymove-docs/docs/tools/locust/working-with-load-tests).
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
pytest utils/tests/test_parsers.py
```

For more instructions and examples, please
read [pytest's documentation](https://docs.pytest.org/en/stable/).

## Reports

We store reports from running against the loadtest environment in
[confluence](https://dp3.atlassian.net/wiki/spaces/MT/pages/1469546505/Reports+and+metrics).
