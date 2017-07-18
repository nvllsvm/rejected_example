Rejected Framework Example
==========================

A minimal example of the `Rejected`_ framework.

Usage
#####

You'll need to have Docker for this.

1. Start RabbitMQ

.. code-block:: bash

    $ docker-compose up -d rabbitmq

2. Declare the queue and publish a message

.. code-block:: bash

    $ python publish.py hi there

3. Start Rejected with the example consumer

.. code-block:: bash

    $ rejected -c examples/config.yaml -f -p $(pwd)
    INFO       2017-07-18 16:21:54  rejected v3.18.3 initializing
    INFO       2017-07-18 16:21:54  Spawning example-1 process for example
    INFO       2017-07-18 16:21:54  Initializing for example-1
    INFO       2017-07-18 16:21:54  Creating consumer examples.consumers.ExampleConsumer
    INFO       2017-07-18 16:21:54  b'hi there'

.. _rejected: https://github.com/gmr/rejected
