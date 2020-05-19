from inhabitant import Inhabitant

class Room(object):
    """description of class"""
    def __init__(self, number, sanitary_state, general_state):
        self.number = number
        self.sanitary_state = sanitary_state
        self.general_state = general_state
        self.inhabitans = []

    def add_inhabitant(self, inhabitant):
        if isinstance(inhabitans, Inhabitant):
            self.inhabitans.append(inhabitant)

    def __str__(self):
        representer = f"room number {self.number}\tinhabitants:"

        for inhabitant in self.inhabitans:
            representer += '\n' + str(inhabitant)
        return representer



