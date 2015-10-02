Genisys
=======

Genisys is one of the main components of the `Skynet`_ stack.

It's main goal is to manage resources associated to a service.

It is able to communicate with different kinds of computes (such as AWS, Docker, VMWare VSphere...) via specific connectors.

Each connector is in charge of managing the resources (scale up/down) of its associated compute, Genisys is the component in charge of balancing the scale orders to the different computes.

Contents
--------

.. toctree::
   :maxdepth: 2

   setup
   configuration
   api
   connector

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Skynet: https://github.com/cyberdyne-corp/skynet
