# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__ (self, name, current_room, inventory=None):
    self.name = name
    self.current_room = current_room

    if inventory is None:
      self.inventory = []
    else:
      self.inventory = inventory

  def add_inventory(self, item):
    self.inventory.append(item)

  def remove_inventory(self, item):
    self.inventory.remove(item)

  # def add_inventory2(self, item):
  #   if item in self.current_room.list:
  #     self.current_room.list.remove(item)
  #     self.inventory.append(item)
  #   else:
  #     print('That item does not exist in this room')