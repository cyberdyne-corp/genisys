=========
Connector
=========

Available connectors
====================

List of existing connectors:

* Docker: `genisys-connector-docker`_

How can I create my connector?
==============================

A connector must expose a HTTP API with specific endpoints:

* :ref:`service-scale-endpoint`: Endpoint used to ensure that a number of containers are running for a service
* :ref:`service-status-endpoint`: Endpoint used to return the number of running resources for a service

These are the **mandatory** endpoints. *Genisys* will use them when trying to automatically scale services.

The connector is not limited to these and could expose other endpoints (for example, a specific endpoint to define a service).

.. _service-scale-endpoint:

``/service/<service_name>/scale``
---------------------------------

This endpoint must ensure that a specific number of containers associated to a service are running.

It must expects a JSON request body to be POST.

The request body must look like:

.. code-block:: javascript

  {
    "number": number_of_containers,
  }

The *number* field is mandatory.

.. _service-status-endpoint:

``/service/<service_name>/status``
----------------------------------

This endpoint must returns the number of running resources for a service managed by this connector.

When hitting the endpoint with a GET, it must returns a JSON body like this:

.. code-block:: javascript

  {
    "running_resources": number_of_running_resources,
  }

.. _genisys-connector-docker: https://github.com/cyberdyne-corp/genisys-connector-docker
