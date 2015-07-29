# genisys

This component is in charge of the compute resource management.

It can upscale/downscale a service by sending actions to compute backend connectors.

## Setup

Install the requirements (assuming you got a Python >= 3.4 devel environment ready):

````
$ pip install -r requirements.txt
````

## Run

Start the component:

````
$ python genisys.py
````

## Compute definition

To manage computes, genisys provides a simple compute definition format.

It defines a link to a connector that will manage specific compute resources (Docker containers, AWS instances...) associated with a service.

A compute definition looks like:

````
myCompute = {
	"name": "myCompute",
	"connector": "http://localhost:7051"
}
````

A compute definition must include a *name* and a *connector*.

The *connector* field is the URL to the genisys connector used to manage compute resources inside this compute.

You can specify an optional file called *computes.py* at the root of the project and use it to define computes using the format defined above.

## HTTP API

Genisys exposes a HTTP API. It can be used to perform CRUD actions on computes and trigger remote procedure calls on services.

Note: The examples use the httpie CLI to query the API, see: https://github.com/jakubroztocil/httpie

### compute HTTP endpoint

The following endpoints are exposed:

* [/compute](#compute-1) : Register a new compute definition
* [/compute/\<compute_name\>](#computecompute_name) : Retrieve or update a compute definition

#### /compute

This endpoint is used to create a new compute definition.

It expects a JSON request body to be POST. The request body must look like:

````
{
	"name": "compute_name",
	"connector": "http://connector.domain:port",
}
````

All fields are mandatory.

The *compute* field is used to identify the compute.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

````
$ http POST :7001/compute name="localdc" connector="http://localhost:7051"
````

#### /compute/\<compute_name\>

This endpoint is used to retrieve a compute definition or to update it.

It supports the following methods: PUT and GET.

When hitting the endpoint with a GET, it returns a JSON body like this:

````
{
    "connector": "http://localhost:7051",
    "name": "localdc"
}
````

When hitting the endpoint with a PUT, it expects a JSON request body that must look like:

````
{
	"connector": "http://localhost:7051"
}
````

The *connector* field is mandatory.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

````
$ http PUT :7001/compute/local connector="http://localhost:7052"
````

### service HTTP endpoint

The following endpoints are exposed:

* [/service/\<service_name\>/upscale](#serviceservice_namestart) : Upscale a service by adding an associated compute resource.
* [/service/\<service_name\>/downscale](#serviceservice_namekill) : Downscale a service by removing an associated compute resource.

#### /service/\<service_name\>/upscale

This endpoint is used to create a new compute resource associated to the service.

It expects a JSON request body to be POST. The request body must look like:

````
{
	"compute": "compute_name",
}
````

The *compute* field is mandatory.

The *compute* field is used to identify the compute in which the compute resource will be created.

Example:

````
$ http POST :7001/service/myService/upscale compute="local"
````

#### /service/\<service_name\>/downscale

This endpoint is used to remove a running compute resource associated to the service.

It expects a JSON request body to be POST. The request body must look like:

````
{
	"compute": "compute_name",
}
````

The *compute* field is mandatory.

The *compute* field is used to identify the compute in which the compute resource will be removed.

Example:

````
$ http POST :7001/service/myService/downscale compute="local"
````
