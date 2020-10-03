class Runner():
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.passes = 0

    def process_player(self, game, player, color):
        if game.is_finished:
            return

        if game.get_coverage(color):
            inp = player.get_input(game, color)
            if inp == 'finish':
                game.is_finished = True
                return False
            if inp == 'restart':
                game.restart()
                return False
            game.make_turn(inp, color)
            return True
        else:
            self.passes += 1
            return True

    def process(self, game):
        self.passes = 0
        turn_successful = self.process_player(game, self.player_one, "b")
        if not turn_successful:
            return
        turn_successful = self.process_player(game, self.player_two, "w")
        if not turn_successful:
            return
        if self.passes == 2:
            game.is_finished = True
