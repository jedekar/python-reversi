FIELD_WIDTH = 8


def is_valid_index(cell_idx):
    if 0 < cell_idx[0] < FIELD_WIDTH and 0 < cell_idx[1] < FIELD_WIDTH:
        return True

    return False


def normalize_direction(direction):
    y, x = direction
    if y > x:
        return y / y, x / y
    if x == 0:
        return y, x

    return y / x, x / x


def inverseof(color):
    if color == 'b':
        return 'w'
    else:
        return 'b'


def get_valid_neighbours(cell_idx):
    result = []
    neighbours = [(cell_idx[0] - 1, cell_idx[1]),
                  (cell_idx[0] - 1, cell_idx[1] + 1),
                  (cell_idx[0], cell_idx[1] + 1),
                  (cell_idx[0] + 1, cell_idx[1] + 1),
                  (cell_idx[0] + 1, cell_idx[1]),
                  (cell_idx[0] + 1, cell_idx[1] - 1),
                  (cell_idx[0], cell_idx[1] - 1),
                  (cell_idx[0] - 1, cell_idx[1] - 1)]
    for n in neighbours:
        if is_valid_index(n):
            result.append(n)

    return result


def get_directions(cell_idx, points):
    result = []
    for p in points:
        result.append((p[0] - cell_idx[0], p[1] - cell_idx[1]))

    return result


class Reversi:
    def __init__(self):
        self.is_finished = False
        self.views = []
        self.field = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'w', 'b', ' ', ' ', ' '],
                      [' ', ' ', ' ', 'b', 'w', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    def get_inverse_neighbours(self, cell_idx):
        result = []
        inverse = inverseof(self.field[cell_idx[0]][cell_idx[1]])
        neighbours = get_valid_neighbours(cell_idx)
        for n in neighbours:
            neighbour_cell = self.field[n[0]][n[1]]
            if neighbour_cell == inverse:
                result.append(n)

        return result

    def find_empty_cell(self, cell_idx, direction):
        start = self.field[cell_idx[0]][cell_idx[1]]
        inverse = inverseof(start)
        y = cell_idx[0] + direction[0]
        x = cell_idx[1] + direction[1]
        while True:
            if not is_valid_index((y, x)):
                return None
            current = self.field[y][x]
            if current == inverse:
                return None
            if current == ' ':
                return y, x
            if current == start:
                y += direction[0]
                x += direction[1]
                continue

    def get_available_moves(self, cell_idx):
        available_moves = []
        n = self.get_inverse_neighbours(cell_idx)
        d = get_directions(cell_idx, n)
        for i in range(len(n)):
            move = self.find_empty_cell(n[i], d[i])
            if move is not None:
                available_moves.append(move)

        return available_moves

    def get_pieces(self, color):
        pieces = []
        for i in range(FIELD_WIDTH):
            for j in range(FIELD_WIDTH):
                current = self.field[i][j]
                if current == color:
                    pieces.append((i, j))

        return pieces

    def get_coverage(self, color):
        pieces = self.get_pieces(color)
        coverage = {}

        for p in pieces:
            moves = self.get_available_moves(p)
            for m in moves:
                if m not in coverage:
                    coverage[m] = [p]
                else:
                    coverage[m].append(p)

        return coverage

    def flip_row(self, cell_idx, direction):
        color = self.field[cell_idx[0]][cell_idx[1]]
        inverse = inverseof(color)
        y = cell_idx[0] + direction[0]
        x = cell_idx[1] + direction[1]
        while True:
            current = self.field[y][x]
            if current == inverse:
                self.field[y][x] = color
                y += direction[0]
                x += direction[1]
                continue
            break

    def flip_pieces(self, attacked, attackers):
        color = self.field[attackers[0][0]][attackers[0][1]]
        self.field[attacked[0]][attacked[1]] = color
        directions = list(map(normalize_direction,
                              get_directions(attacked, attackers)))
        self.flip_row(attacked, directions)

    def notify(self):
        for v in self.views:
            v.update(self)

    def make_turn(self, cell_idx, color):
        coverage = self.get_coverage(color)
        self.flip_pieces(cell_idx, coverage[cell_idx])
        self.notify()
