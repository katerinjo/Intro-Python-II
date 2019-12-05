from entity import Entity
from utils import color

class Treasure(Entity):
    def __init__(self, name, value):
        super().__init__(name)
        self.value = value
