# Write a class to hold player information, e.g. what room they are in
# currently.

from entity import Entity
from utils import color

class Player(Entity):
    def __init__(self, name, gender):
        super().__init__(name)
        self.gender = gender
        self.eyes = 2
        self.hominid_arms = 2
        self.hominid_legs = 2
        self.tails = 0

    def go(self, direction):
        destination = getattr(self.location, direction)
        if destination is None:
            raise RuntimeError("You can't go that way.")
        else:
            self.location.remove(self)
            self.location = destination
            destination.insert(self)

    def look(self):
        human_score = (
            self.eyes
            + self.hominid_arms
            + self.hominid_legs
            - self.tails
            )
        if human_score < 7:
            human_comment = "You aren't looking very human today."
        else:
            human_comment = "You look so human!"
        return [
            color(self.name, 'blue'),
            f'Your gender is {self.gender}.',
            f'You have {self.eyes} eyes.',
            f'You have {self.hominid_arms} arms and {self.hominid_legs} legs.',
            human_comment
        ]
