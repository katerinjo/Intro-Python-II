# Write a class to hold player information, e.g. what room they are in
# currently.

from entity import Entity

class player(Entity):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender
        self.eyes = 2
        self.hominid_arms = 2
        self.hominid_legs = 2
        self.tails = 0

    def go(self, direction):
        destination = getattr(self.location, direction)
        self.location.remove(self)
        self.locaton = destination
        destination.insert(self)
