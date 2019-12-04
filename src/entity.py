from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self):
        self.contains = []

    @abstractmethod
    def look(self):
        pass
