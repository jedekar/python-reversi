class Reversi():
    def __init__(self):
        self.is_finished = False
        self.free_cells = 60

    def turn(self):
        self.free_cells -= 1
