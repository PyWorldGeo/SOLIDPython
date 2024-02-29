#5
# The Dependency Inversion principle states that our classes should depend upon interfaces
# or abstract classes instead of concrete classes and functions.

#Incorrect
class Logger:
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:

    def __init__(self):
        self.logger = Logger()

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result

#Correct

from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    @abstractmethod
    def log(self, message):
        pass

class Logger(LoggerInterface):
    def log(self, message):
        with open('log.txt', 'a') as f:
            f.write(message + '\n')

class Calculator:
    def __init__(self, logger: LoggerInterface):
        self.logger = logger

    def add(self, x, y):
        result = x + y
        self.logger.log(f"Added {x} and {y}, result = {result}")
        return result