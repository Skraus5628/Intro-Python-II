# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
     


# * The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    #which point to the room in that respective direction.

    #Realized this was, along with the pre populated rooms, set with the rooms
    #All set up in adv.py lmao