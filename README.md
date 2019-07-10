# Load Testing

Load testing for the [MilMove](https://github.com/transcom/mymove) application is done with the code in this repo.
Testing employs the [locust.io](https://docs.locust.io/en/stable/) framework which in turn uses the
[Bravado](https://bravado.readthedocs.io/en/stable/) swagger library to make requests.

## Creating devlocal users for load testing

Load testing will require that you create a number of different users for your scenarios. To create a devlocal
user you'll hit the `/devlocal-auth/create` endpoint. The `/create` method is different from `/new` because it
returns a JSON formatted version of the User model for the new user instead of redirecting to the landing page.
The new user will be logged in upon creation and the response will contain the session token you'd expect from
a normal login.

## What is tested

The load testing demo implements these things:

- Anon User: Touching home page only
- Service Member App: PPM Flow only
- Office App: Queue and Move Inspection (no move modification)
- TSP App: Queue and Move Inspection (no move modification)

## Quick Start

Getting started

```sh
make setup
```

From the MilMove application in a separate window ensure that the app server is running with `make server_run`.

### Running tests with Web UI

```sh
make load_test
```

Then open [http://localhost:8089](http://localhost:8089/) and enter the number of users to simulate and the hatch rate.
Finally, hit the `Start swarming` button and wait for the tests to finish.

### Running tests from the CLI

You can run the test suite without the Web UI with a command similar to this:

```sh
make load_test_noweb
```

Or you can run this by hand with:

```sh
locust -f locustfile.py --no-web --clients=50 --hatch-rate=5 --run-time=60s
```

## Load Testing against AWS Experimental Environment

To load test against the AWS Experimental Environment you must modify the
[`DEVLOCAL_AUTH` environment variable](https://github.com/transcom/mymove/blob/master/config/env/experimental.env#L15)
and [deploy the code to the experimental environment](https://github.com/transcom/mymove/blob/master/docs/how-to/deploy-to-experimental.md).

Then you can use the same steps as the development as above as long as you change the `host` parameter in the
`locustfile.py` test classes and point them to the experimental domains:

- [https://my.experimental.move.mil](https://my.experimental.move.mil)
- [https://office.experimental.move.mil](https://office.experimental.move.mil)
- [https://tsp.experimental.move.mil](https://tsp.experimental.move.mil)

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

- [app-experimental cluster metrics](https://us-west-2.console.aws.amazon.com/ecs/home?region=us-west-2#/clusters/app-experimental/services/app/metrics)
- [app-experimental CloudWatch dashboard](https://us-west-2.console.aws.amazon.com/cloudwatch/home?region=us-west-2#dashboards:name=mil-experimental)

## References

- [Original Load Testing PR](https://github.com/transcom/mymove/pull/1597)
