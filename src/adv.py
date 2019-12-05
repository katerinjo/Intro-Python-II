from room import Room
from player import Player
from textwrap import fill

# Functions

def color(text, color):
    chosen = {
        'red': '\u001b[31m',
        'green': '\u001b[32m',
        'blue': '\u001b[34m',
        'yellow': '\u001b[33m'
    }[color]
    return chosen + text + '\u001b[0m'

def log(text, color=None):
    out_text = color(text, color) if color else text
    print(fill(text))

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player('Nonny', 'nice try NSA')
player.location = room['outside']
room['outside'].insert(player)

while True:
    log(player.location.look())
    command = input('? ')
    if command in ['n', 'north']:
        player.go('n_to')
    elif command in ['s', 'south']:
        player.go('s_to')
    elif command in ['e', 'east']:
        player.go('e_to')
    elif command in ['w', 'west']:
        player.go('w_to')
    elif command in ['h', 'help']:
        print('''
        Available commands:
        (h)elp - list commands you can use
        (q)uit - leave the game
        (n)orth - go north
        (s)outh - go south
        (e)ast - go east
        (w)est - go west
        ''')
    elif command in ['q', 'quit']:
        log('Are you sure you want to quit?')
        if input('(y/n)') in ['y', 'yes']:
            quit()
