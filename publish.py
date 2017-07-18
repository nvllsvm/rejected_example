import sys

import pika

exchange = ''
queue = 'example'

message = ' '.join(sys.argv[1:])

rabbit_connection = pika.BlockingConnection()
channel = rabbit_connection.channel()
channel.queue_declare(queue=queue, durable=True,
                      exclusive=False, auto_delete=False)

channel.basic_publish(
    exchange=exchange,
    routing_key=queue,
    body=message)
