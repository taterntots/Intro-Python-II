# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__ (self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
    self.name = name
    self.description = description
    self.n_to = n_to
    self.s_to = s_to
    self.e_to = e_to
    self.w_to = w_to
    self.list = []

  def add_item(self, item):
    self.list.append(item)

  def print_list(self):
    print(self.list)