from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, name):
        self.name = name
        self.contents = []

    @abstractmethod
    def look(self):
        pass
