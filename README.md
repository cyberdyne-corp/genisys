# genysis

This component is in charge of the compute resource management.

It can upscale/downscale a service by sending actions to compute backend connectors. 

## Setup

Install the requirements (assuming you got a Python >= 3.4 devel environment ready):

````
$ pip install -r requirements.txt
````

## Run

Start the adapter:

````
$ python genisys.py
````

## Datacenter definition

To manage services, genisys provides a simple datacenter definition format.

It defines a link to a connector that will manage specific compute resources (Docker containers, AWS instances...) associated with a service.

A datacenter definition looks like:

````
myDC = {
	"name": "myDC",
	"connector": "http://localhost:7051"
}
````

A datacenter definition must include a *name* and a *connector*.

The *connector* field is the URL to the genisys connector used to manage compute resources inside this datacenter.

You can specify an optional file called *datacenter.py* at the root of the project and use it to define datacenters using the format defined above. 

## HTTP API

Genisys exposes a RESTful HTTP API. It can be used to perform CRUD actions on datacenters.

Note: The examples use the httpie CLI to query the API, see: https://github.com/jakubroztocil/httpie

### datacenter HTTP endpoint

The following endpoints are exposed:

* [/datacenter](#datacenter-1) : Register a new datacenter defintion
* [/datacenter/\<datacenter_name\>](#datacenterdatacenter_name) : Retrieve or update a datacenter definition
* [/datacenter/\<datacenter_name\>/start](#datacenterdatacenter_namestart) : Start a new container for a datacenter
* [/datacenter/\<datacenter_name\>/kill](#datacenterdatacenter_namekill) : Kill a container associated to a datacenter

#### /datacenter

This endpoint is used to create a new datacenter definition.

It expects a JSON request body to be POST. The request body must look like:

````
{
	"name": "datacenter_name",
	"connector": "http://connector.domain:port",
}
````

All fields are mandatory.

The *datacenter* field is used to identify the datacenter.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

````
$ http POST :7051/datacenter name="localdc" connector="http://localhost:7051"
````

#### /datacenter/\<datacenter_name\>

This endpoint is used to retrieve a datacenter definition or to update it.

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
$ http PUT :7051/datacenter/helloworld image="panamax/hello-world-php:latest" command="/run.sh"
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
	"datacenter": "datacenter_name",
}
````

The *datacenter* field is mandatory.

The *datacenter* field is used to identify the datacenter in which the compute resource will be created.

Example:

````
$ http POST :7001/service/myService/upscale datacenter="local"
````

#### /service/\<service_name\>/downscale

This endpoint is used to remove a running compute resource associated to the service.

It expects a JSON request body to be POST. The request body must look like:

````
{
	"datacenter": "datacenter_name",
}
````

The *datacenter* field is mandatory.

The *datacenter* field is used to identify the datacenter in which the compute resource will be removed.

Example:

````
$ http POST :7001/service/myService/downscale datacenter="local"
````
