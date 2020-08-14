# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item
class Room():
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = [item]
     

def __str___(self):
    return f"Room: {self.name}, Description: {self.description}"


def remove_item(self, item):
    del self.item[item]


def add_item(self, item):
    self.item.append(item)

# * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    #which point to the room in that respective direction.

    #Realized this was, along with the pre populated rooms, set with the rooms
    #All set up in adv.py lmao

    # MIght reuse this to allow users to type full direction values instead of n w e s
