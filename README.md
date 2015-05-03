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

A service definition must include a *name* and a *connector*.

The *connector* field is the URL to the genisys connector used to manage compute resources inside this datacenter.

You can specify an optional file called *datacenter.py* at the root of the project and use it to define datacenters using the format defined above. 
