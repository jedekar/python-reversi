from reversi.controller import PASS, RESTART


class Runner:
    def __init__(self, player_one, player_two):
        self.current = player_one
        self.next = player_two

    def process_player(self, game):
        inp = self.current.get_input(game)
        if inp == PASS:
            return
        if inp == RESTART:
            game.reset()
            self.switch_player()
            return

        game.make_turn(inp, self.current.color)

    def switch_player(self):
        self.current, self.next = self.next, self.current

    def process(self, game):
        self.process_player(game)
        self.switch_player()
