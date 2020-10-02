FIELD_WIDTH = 8


class Reversi():
    def __init__(self):
        self.is_finished = False
        self.free_cells = 60
        self.field = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'w', 'b', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'b', 'w', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.piece = " "
        self.current_player = "b"

    def inverseof(self, color):
        if color == 'b':
            return 'w'
        else:
            return 'b'

    def is_valid_index(self, cell_idx):
        if (cell_idx[0] > 0 and cell_idx[0] < 8
            and cell_idx[1] > 0 and cell_idx[1] < 8):
            return True

        return False

    def get_valid_neighbours(self, cell_idx):
        result = []
        neighbours = [(cell_idx[0]-1, cell_idx[1]),
                      (cell_idx[0]-1, cell_idx[1]+1),
                      (cell_idx[0], cell_idx[1]+1),
                      (cell_idx[0]+1, cell_idx[1]+1),
                      (cell_idx[0]+1, cell_idx[1]),
                      (cell_idx[0]+1, cell_idx[1]-1),
                      (cell_idx[0], cell_idx[1]-1),
                      (cell_idx[0]-1, cell_idx[1]-1)]
        for n in neighbours:
            if self.is_valid_index(n):
                result.append(n)

        return result

    def get_inverse_neighbours(self, cell_idx):
        inverse = self.inverseof(self.field[cell_idx[0]][cell_idx[1]])
        neighbours = self.get_valid_neighbours(cell_idx)
        result = []
        for n in neighbours:
            neighbour_cell = self.field[n[0]][b[1]]
            if neighbour_cell == inverse:
                result.append(n)

        return result

    def get_vectors(self, cell_idx, points):
        result = []
        for p in points:
            result.append((p[0] - cell_idx[0], p[1] - cell_idx[1]))

        return result

    def turn(self):
        self.free_cells -= 1

    def check_up(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell - FIELD_WIDTH, 0, -FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_down(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        for i in range(cell + FIELD_WIDTH, FIELD_WIDTH ** 2, FIELD_WIDTH):
            up = self.field[i]
            if up == curr:
                return None
            if up == not_curr:
                prev = True
                continue
            if up == " " and prev is True:
                return i
            return None

    def check_vertical(self, cell):
        moves = []
        up = self.check_up(cell)
        down = self.check_down(cell)
        if up is not None:
            moves.append(up)
        if down is not None:
            moves.append(down)
        return moves

    def check_left(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        first_in_row = 0
        for i in range(0, FIELD_WIDTH ** 2, FIELD_WIDTH):
            if cell < i:
                first_in_row = i - FIELD_WIDTH
                break
        for i in range(cell - 1, first_in_row - 1, -1):
            left = self.field[i]
            if left == curr:
                return None
            if left == not_curr:
                prev = True
                continue
            if left == " " and prev is True:
                return i
            return None
        return None

    def check_right(self, cell):
        prev = False
        curr = self.field[cell]
        not_curr = "w" if curr == "b" else "b"
        last_in_row = 0
        for i in range(0, FIELD_WIDTH ** 2, FIELD_WIDTH):
            if cell < i:
                last_in_row = i
                break
        for i in range(cell + 1, last_in_row + 1):
            left = self.field[i]
            if left == curr:
                return None
            if left == not_curr:
                prev = True
                continue
            if left == " " and prev is True:
                return i
            return None
        return None

    def check_horizontal(self, cell):
        moves = []
        left = self.check_left(cell)
        right = self.check_right(cell)
        if left is not None:
            moves.append(left)
        if right is not None:
            moves.append(right)
        return moves

    def next(self):
        if self.current_player == "b":
            pass
        else:
            self.current_player = "w"
        return self.current_player

    def get_coverage(self, color):
        pass
