# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room

# MIght reuse this to allow users to type full direction values instead of n w e s
direction_names = {
    'n': 'North',
    'e': 'East',
    'w': 'West',
    's': 'South'
}

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    
