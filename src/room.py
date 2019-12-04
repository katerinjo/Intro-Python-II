# Implement a class to hold room information. This should have name and
# description attributes.

from entity import Entity

class Room(Entity):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def look(self):
        content_list = '\n'.join(' - ' + item.name for item in self.contents)
        return '\n'.join([
            self.name,
            self.description,
            '\nRoom contains:',
            content_list
        ])
