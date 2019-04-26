class player:
    def __init__(self, name):
        self.points = 0
        self.name = name

    def change_name(self, name):
        self.name = name

    def reset_points(self):
        self.points = 0

    def add_points(self, points):
        self.points += points

    def subtract_points(self, points):
        self.points -= points
