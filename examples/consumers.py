import logging

from rejected import consumer

LOGGER = logging.getLogger(__name__)

class ExampleConsumer(consumer.Consumer):

    def process(self):
        LOGGER.info(self.body)
