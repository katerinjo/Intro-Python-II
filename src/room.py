# Implement a class to hold room information. This should have name and
# description attributes.

from entity import Entity
from utils import color

class Room(Entity):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return self.name + '\n' + self.description

    def look(self):
        content_list = '\n'.join(' - ' + item.name for item in self.contents)
        return [
            color(self.name, 'blue'),
            self.description,
            '',
            color('Room contains:', 'blue'),
            content_list
        ]
