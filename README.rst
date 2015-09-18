Genisys
=======

Genisys is one of the main components of the `Skynet`_ stack.

It's main goal is to manage resources associated to a service.

It is able to communicate with different kinds of computes (such as AWS, Docker, VMWare VSphere...) via specific connectors.

Each connector is in charge of managing the resources (scale up/down) of its associated compute, Genisys is the component in charge of balancing the scale orders to the different computes.

Goals
-----

* Scales services in computes.
* Compute resources management.

Quick start
-----------

Start this component using Docker:

.. code-block:: bash

    $ docker run -p "7001:7001" cyberdynesystems/genisys:latest

Override the configuration file:

.. code-block:: bash

    $ docker run -p "7001:7001" -v "/path/to/config/genisys.yml:/app/genisys.yml" cyberdynesystems/genisys:latest

Documentation
-------------

`On readthedocs.org`_ or in the ``docs/source`` directory.

.. _On readthedocs.org: http://genisys.readthedocs.org/en/latest/
.. _Skynet: https://github.com/cyberdyne-corp/skynet
