=============
Configuration
=============

Configuration file
==================

The configuration file *genisys.yml* is written in `YAML format`_.

.. code-block:: yaml

    genisys:
      # Server address to bind to.
      bind: 127.0.0.1

      # Application port
      port: 7001

      # Path to compute definitions
      compute_file: ./computes.py

    consul:
      # Consul host
      host: localhost

      # Consul port
      port: 8500

      # Prefix of services managed by genisys
      service_prefix: 'skynet_'

    connector:
      # How frequently to poll all connectors for service status
      poll_interval: 15s


Genisys section
---------------

This section is related to the component configuration.

``bind``
^^^^^^^^

The server address to bind to.

``port``
^^^^^^^^

The port that will be used to communicate with the component via HTTP.

.. _config-compute-file:

``compute_file``
^^^^^^^^^^^^^^^^

A python file that defines an optional list of computes that will be loaded by the component during startup.

See :ref:`compute-definition` below for more information on the format of the file.

Consul section
--------------

This section is related to the Consul service registry.

``host``
^^^^^^^^

The host where is located the Consul server.

``port``
^^^^^^^^

Port associated to the Consul server.

``service_prefix``
^^^^^^^^^^^^^^^^^^

Genisys will poll informations about a selected list of services from the Consul service registry.
This option is used to configure which services will be targeted by Genisys management.

Connector section
-----------------

This section is related to Genisys connectors.

``poll_interval``
^^^^^^^^^^^^^^^^^

Determines how frequently Genisys will poll its connectors to retrieve each service status.

.. _compute-definition:

Compute definition
==================

A compute definition defines a link to a connector that will manage specific compute resources (Docker containers, AWS instances...) associated with a service.

A compute definition looks like:

.. code-block:: python

    myCompute = {
      "name": "myCompute",
      "connector": "http://localhost:7051"
    }

A compute definition must include a *name* and a *connector*.

The *connector* field is the URL to the genisys connector used to manage compute resources associated to this compute.

An optional *service_file* (see :ref:`config-compute-file`) can be used to define services using the format defined above. These definitions will be loaded during the connector startup.

.. _YAML format: https://en.wikipedia.org/wiki/YAML
