import logging

logger = logging.getLogger(__name__)

class SimpleClass:

    def __init__(self, name):
        self.name = name
        logger.info(f"SimpleClass initialized with name: {self.name}")
    def greet(self):
        return f"Hello, {self.name}!"

    def __str__(self):
        return f"SimpleClass(name={self.name})"
