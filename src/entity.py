from abc import ABC, abstractmethod

class Entity(ABC):

    def __init__(self, name):
        self.name = name
        self.contents = []

    def insert(self, entity):
        if entity != self:
            self.contents.append(entity)
        else:
            raise ValueError

    @abstractmethod
    def look(self):
        pass
