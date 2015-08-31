# genisys

This component is in charge of the compute resource management.

It can scale a service by sending actions to compute backend connectors.

## Setup

Install the requirements (assuming you got a Python >= 3.4 devel environment ready):

````
$ pip install -r requirements.txt
````

## Configuration

The configuration file `genisys.yml` is written in [YAML format](http://en.wikipedia.org/wiki/YAML).

```yml
genisys:
  # Application port
  port: 7001

  # Path to compute definitions
  compute_file: ./computes.py

consul:
  # Consul host
  host: localhost

  # Consul port
  port: 8500

  # Prefix for services managed by genisys
  service_prefix: 'skynet_'

connector:
  # How frequently to poll all connectors for service status
  poll_interval: 15s

```

## Run

Start the component:

````
$ python genisys.py
````

## Compute definition

To manage computes, genisys provides a simple compute definition format.

It defines a link to a connector that will manage specific compute resources (Docker containers, AWS instances...) associated with a service.

A compute definition looks like:

```python
myCompute = {
	"name": "myCompute",
	"connector": "http://localhost:7051"
}
```

A compute definition must include a *name* and a *connector*.

The *connector* field is the URL to the genisys connector used to manage compute resources inside this compute.

You can specify an optional file called *computes.py* at the root of the project and use it to define computes using the format defined above.

## HTTP API

Genisys exposes a HTTP API. It can be used to perform CRUD actions on computes and trigger remote procedure calls on services.

Note: The examples use the httpie CLI to query the API, see: https://github.com/jakubroztocil/httpie

### compute HTTP endpoint

The following endpoints are exposed:

* [/compute](#compute-1) : List compute definitions or register a new compute definition
* [/compute/\<compute_name\>](#computecompute_name) : Retrieve or update a compute definition

#### /compute

This endpoint is used to list existing compute definitions or to create a new compute definition.

It supports the following methods: POST and GET.

When hitting the endpoint with a GET, it returns a JSON body like this:

```json
{
  "compute_nameA": {
		"name": "compute_nameA",
		"connector": "http://connector.domain:port",
  },
	"compute_nameB": {
		"name": "compute_nameB",
		"connector": "http://other-connector.domain:port",
  }
}
```

When hitting the endpoint with a POST, it expects a JSON request body that must look like:

```json
{
	"name": "compute_name",
	"connector": "http://connector.domain:port",
}
```

All fields are mandatory.

The *compute* field is used to identify the compute.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

```bash
$ http POST :7001/compute name="localdc" connector="http://localhost:7051"
```

#### /compute/\<compute_name\>

This endpoint is used to retrieve a compute definition or to update it.

It supports the following methods: PUT and GET.

When hitting the endpoint with a GET, it returns a JSON body like this:

```json
{
    "connector": "http://localhost:7051",
    "name": "localdc"
}
```

When hitting the endpoint with a PUT, it expects a JSON request body that must look like:

```json
{
	"connector": "http://localhost:7051"
}
```

The *connector* field is mandatory.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

```bash
$ http PUT :7001/compute/local connector="http://localhost:7052"
```

### service HTTP endpoint

The following endpoints are exposed:

* [/service/\<service_name\>/scale](#serviceservice_namescale) : Ensure that a specific number of compute resource is running for a service.

#### /service/\<service_name\>/scale

This endpoint is used to ensure that specific number of compute resources associated to a service are running.

It expects a JSON request body to be POST. The request body must look like:

```json
{
	"number": "number_of_compute_resources",
	"compute": "compute_name"
}
```

The *number* field is mandatory.

The *compute* field is used to identify the compute in which the compute resource will be created.
If not specified, genisys will automatically pick up the first compute defined.

Example:

```bash
$ http POST :7001/service/myService/scale number=3 compute="local"
```
