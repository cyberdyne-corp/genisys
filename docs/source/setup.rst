=====
Setup
=====

Docker
======

A public Docker image is available and can be used to start the component:

.. code-block:: bash

    $ docker run -p "7001:7001" cyberdynesystems/genisys:latest

Do not forget to map the port 7001 of the container to a specific port on the Docker host.

Overriding the configuration
----------------------------

You can map your own configuration file in the container file system:

.. code-block:: bash

    $ docker run -p "7001:7001" -v "/path/to/config/genisys.yml:/app/genisys.yml" cyberdynesystems/genisys:latest

From sources
============

Requirements
------------

Ensure you have *python* >= 3.4 and *git* installed on your system.

Installation
------------

Clone this repository and install the dependencies using **pip**:

.. code-block:: bash

    $ git clone https://github.com/cyberdyne-corp/genisys && cd genisys
    $ pip install -r requirements.txt


Start
-----

Start the component:

.. code-block:: bash

    $ python main.py
