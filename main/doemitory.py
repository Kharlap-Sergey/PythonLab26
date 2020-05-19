from level import Level
class Dormitory(object):
    """description of class"""


    dormitory_amount = 0
    def __init__(self, dormitoryname):
        Dormitory.dormitory_amount += 1
        self.bestrooms = []
        self.name = dormitoryname
        self.levels = []
    
    def add_level(self, level):
        if isinstance(level, Level):
            self.levels.append(level)
    
    def finde_best_rooms(self):
        self.bestrooms = []

        if len(self.levels) == 0:
            return
        bests = []
        
        for level in self.levels:
            level.finde_best_rooms()
            bests.extend(level.bestrooms)

        if len(bests) == 0:
            return

        best = bests[0]
        for room in bests:
            if best.sanitary_state + best.general_state < room.sanitary_state + room.general_state:
                best = room

        for room in bests:
            if best.sanitary_state + best.general_state == room.sanitary_state + room.general_state:
                self.bestrooms.append(room)
        
        def __str__(self):
            representer = f"dormitory name - {self.name}\tlevels:"
            for room in self.rooms:
                representer += '\n' + str(room)

            return representer

    def __str__(self):
        representer = f"dormitory - {self.name}"
        for level in self.levels:
            representer += '\n' + str(level)

        self.finde_best_rooms()
        representer += f'\n best rooms:'
        for room in self.bestrooms:
            representer += '\n' + str(room)
        return representer


