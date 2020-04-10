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

# Creates items
items = {
    'dagger': Item('dagger', 'Thief dagger made of Mythril'),
    'sword': Item('sword', 'The mighty Ragnarok!'),
    'peanuts': Item('peanuts', 'Scrooge McDuck levels'),
    'staff': Item('staff', 'You shall not pass!')
}

# Add items to rooms
room['overlook'].add_item(items['sword'])
room['treasure'].add_item(items['peanuts'])
room['foyer'].add_item(items['staff'])
room['foyer'].add_item(items['dagger'])

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

    #shortcuts
    current_room = playerOne.current_room
    room_items = [item.name for item in current_room.list]
    player_equipment = [item.name for item in playerOne.inventory]

    #HUD
    print('============================================')
    print(f'Player: {playerOne.name}')
    print(f'Equipment: {player_equipment}')
    print(f'Current Room: {current_room.name}')
    print(f'Items Available: {room_items}\n')
    print(f'{current_room.description}')
    print('============================================')

    #input
    command = input('Choose a direction [n][s][e][w] or pickup/drop an item [get][drop]: ').lower().split(" ")

    #movement logic
    if len(command) < 2:
        command = command[0]
        if command == 'n' and playerOne.current_room.n_to:
            playerOne.current_room = playerOne.current_room.n_to
        elif command == 's' and playerOne.current_room.s_to:
            playerOne.current_room = playerOne.current_room.s_to
        elif command == 'e' and playerOne.current_room.e_to:
            playerOne.current_room = playerOne.current_room.e_to
        elif command == 'w' and playerOne.current_room.w_to:
            playerOne.current_room = playerOne.current_room.w_to
        elif command == 'q':
            active = False
        else:
            print('You cannot move in that direction')
    #item logic
    else: 
        if command[0] == 'get':
            if command[1] in room_items:
                playerOne.add_inventory(items[command[1]])
                items[command[1]].on_take()
                
                for i, item in enumerate(room_items):
                    if item == command[1]:
                        del current_room.list[i]
            else:
                print(f'{command[1]} is not in this room')
        
        if command[0] == 'drop':
            if command[1] in player_equipment:
                current_room.add_item(items[command[1]])
                items[command[1]].on_drop()

                for i, item in enumerate(player_equipment):
                    if item == command[1]:
                        del playerOne.inventory[i]
            else:
                print(f'{command[1]} is not in your inventory')


                    # if command == f'get {item[i]}':
                    #     playerOne.add_inventory(items[room_items[i]])
                    #     # room[keys].remove_item(room_items[i])
                    #     # print(f'You have picked up {playerOne.inventory[i]}!')
                    # # elif command == f'drop {playerOne.inventory[i]}':
                    # #     playerOne.remove_inventory(room_list[i])
                    # #     room[keys].add_item(room_list[i])
                    # #     print('You have dropped {room_list[i]}')
                    # else:
                    #     print('No such item exists')