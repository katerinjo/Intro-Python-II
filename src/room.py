# Implement a class to hold room information. This should have name and
# description attributes.

from entity import Entity

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
        return '\n'.join([
            self.name,
            self.description,
            '\nRoom contains:',
            content_list
        ])
