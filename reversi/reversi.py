FIELD_WIDTH = 8
BLACK = 'b'
WHITE = 'w'
EMPTY = ' '


def is_valid_index(cell_idx):
    if 0 <= cell_idx[0] < FIELD_WIDTH and 0 <= cell_idx[1] < FIELD_WIDTH:
        return True

    return False


def normalize_direction(direction):
    y, x = direction
    ly, lx = abs(y), abs(x)
    if ly > lx:
        return int(y / ly), int(x / ly)
    if x == 0:
        return y, x

    return int(y / lx), int(x / lx)


def inverseof(color):
    return WHITE if color == BLACK else BLACK


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
        self.views = []
        self.field = [[EMPTY] * FIELD_WIDTH for i in range(FIELD_WIDTH)]
        self.field[3][3] = BLACK
        self.field[4][4] = BLACK
        self.field[3][4] = WHITE
        self.field[4][3] = WHITE

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
        color = self.field[cell_idx[0]][cell_idx[1]]
        inverse = inverseof(color)
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
            if current == color:
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
        for d in directions:
            self.flip_row(attacked, d)

    def notify(self):
        for v in self.views:
            v.update(self)

    def is_finished(self):
        black_coverage = self.get_coverage(BLACK)
        white_coverage = self.get_coverage(WHITE)
        if len(black_coverage) == 0 and len(white_coverage) == 0:
            return True
        return False

    def make_turn(self, cell_idx, color):
        coverage = self.get_coverage(color)
        self.flip_pieces(cell_idx, coverage[cell_idx])
        self.notify()

    def calculate_score(self):
        black = len(self.get_pieces(BLACK))
        white = len(self.get_pieces(WHITE))

        return black, white

    def reset(self):
        self.field = [[EMPTY] * FIELD_WIDTH for i in range(FIELD_WIDTH)]
        self.field[3][3] = BLACK
        self.field[4][4] = BLACK
        self.field[3][4] = WHITE
        self.field[4][3] = WHITE
        self.notify()
