class Inhabitant(object):
    """description of class"""

    def __init__(self, name, surname, gender, age, status):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.status = status

    def __str__(self):
        return f"name - {self.name} surname - {self.surname}; gender - {self.gender}; age - {self.age}; status - {self.status}"


