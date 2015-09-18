========
HTTP API
========

Genisys exposes a HTTP API. It can be used to perform CRUD actions on computes and trigger remote procedure calls on services.

NOTE: The examples use the `httpie CLI`_ to query the API.

Compute HTTP endpoint
=====================

The following endpoints are exposed:

* :ref:`compute-endpoint`: List service definitions or register a new service definition
* :ref:`compute-name-endpoint`: Retrieve or update a service definition

.. _compute-endpoint:

``/compute``
------------

This endpoint is used to list existing compute definitions or to create a new compute definition.

It supports the following methods: POST and GET.

When hitting the endpoint with a GET, it returns a JSON body like this:

.. code-block:: javascript

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

When hitting the endpoint with a POST, it expects a JSON request body that must look like:

.. code-block:: javascript

    {
      "name": "compute_name",
      "connector": "http://connector.domain:port",
    }

All fields are mandatory.

The *compute* field is used to identify the compute.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

.. code-block:: bash

  $ http POST :7001/compute name="localdc" connector="http://localhost:7051"

.. _compute-name-endpoint:

``/compute/<compute_name>``
---------------------------

This endpoint is used to retrieve a compute definition or to update it.

It supports the following methods: PUT and GET.

When hitting the endpoint with a GET, it returns a JSON body like this:

.. code-block:: javascript

    {
      "connector": "http://localhost:7051",
      "name": "localdc"
    }

When hitting the endpoint with a PUT, it expects a JSON request body that must look like:

.. code-block:: javascript

    {
  	  "connector": "http://localhost:7051"
    }

The *connector* field is mandatory.

The *connector* field specifies the URL to a genisys connector that will manage the backend.

Example:

.. code-block:: bash

  $ http PUT :7001/compute/local connector="http://localhost:7052"

Service HTTP endpoint
=====================

The following endpoints are exposed:

* :ref:`service-scale-endpoint`: Ensure that a specific number of compute resource is running for a service

.. _service-scale-endpoint:

``/service/<service_name>/scale``
---------------------------------

This endpoint is used to ensure that specific number of compute resources associated to a service are running.

It expects a JSON request body to be POST.

The request body must look like:

.. code-block:: javascript

    {
      "number": "number_of_compute_resources",
      "compute": "compute_name"
    }

The *number* field is mandatory.

The *compute* field is used to identify the compute in which the compute resource will be created.
If not specified, Genisys will automatically pick up the first compute defined.

Example:

.. code-block:: bash

  $ http POST :7001/service/myService/scale number=3 compute="local"

.. _httpie CLI: https://github.com/jakubroztocil/httpie
