from room import Room
from player import Player
from item import Item

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

# Create items
dagger = Item('dagger', 'Thief dagger made of Mythril')
print(dagger.name)
sword = Item('sword', 'The mighty Ragnarok!')
print(sword.name)

# Add items to rooms
room['foyer'].add_item(sword.name)
room['foyer'].add_item(dagger.name)
room['foyer'].print_list()

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

playerOne = Player('Matt', room['outside'])

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

active = True

#gamplay loop
while active == True:

    print('============================================')
    print(f'Player: {playerOne.name}')
    print(f'Current Room: {playerOne.current_room.name}')
    print(f'Items Available: {playerOne.current_room.list}\n')
    print(f'{playerOne.current_room.description}')
    print('============================================')

    #input
    direction = input('Choose a direction: ').lower()

    #movement logic
    if direction == 'n' and playerOne.current_room.n_to:
        playerOne.current_room = playerOne.current_room.n_to
    elif direction == 's' and playerOne.current_room.s_to:
        playerOne.current_room = playerOne.current_room.s_to
    elif direction == 'e' and playerOne.current_room.e_to:
        playerOne.current_room = playerOne.current_room.e_to
    elif direction == 'w' and playerOne.current_room.w_to:
        playerOne.current_room = playerOne.current_room.w_to
    elif direction == 'q':
        active = False
    else:
        print('You cannot move in that direction')

    #item logic