from reversi.reversi import INVALID_CELL, inverseof, INFINITY


class MinimaxNode:
    def __init__(self, value, move):
        self.value = value
        self.move = move


def alphabeta(game, color, depth, alpha, beta):
    alpha = alpha
    inverse = inverseof(color)
    node = MinimaxNode(-1, INVALID_CELL)
    moves = game.get_available_moves_for(color)
    if depth == 0 or len(moves) == 0:
        node.value = game.sev(color)
        return node

    level = game.replicate_for_all(color)

    node.value = -INFINITY
    for i in range(len(level)):
        prev = node.value
        node.value = max(node.value,
                         -alphabeta(level[i], inverse, depth - 1, -beta, -alpha).value)
        if prev != node.value:
            node.move = moves[i]
        alpha = max(alpha, node.value)
        if alpha >= beta:
            break

    return node
