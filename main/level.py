from room import Room

class Level(object):
    """description of class"""

    def __init__(self, number):
        self.bestrooms = []
        self.rooms = []
        self.number = number

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(inhabitant)

    def finde_best_rooms(self):
        self.bestrooms = []
        if(len(self.rooms) == 0):
            self.bestrooms = []
        else:
            best = self.rooms[0]
            for i in self.rooms:
                if best.sanitary_state + best.general_state < i.sanitary_state + i.general_state:
                    best = i

            for i in self.rooms:
                if best.sanitary_state + best.general_state == i.sanitary_state + i.general_state:
                    self.bestrooms.append(i);


    def __str__(self):
        representer = f"level number - {self.number}\trooms:"
        for room in self.rooms:
            representer += '\n' + str(room)

        return representer

