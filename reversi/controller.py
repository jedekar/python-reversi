class HumanController():
    def get_input(self, game, color):
        pass


class BotController():
    def get_input(self, game, color):
        pass


def prepare():
    player_one = None
    player_two = None
    while True:
        print('Choose your opponent')
        inp = input('> ')
        if inp == 'bot':
            player_one = HumanController()
            player_two = BotController()
            break
        elif inp == 'human':
            player_one = HumanController()
            player_two = HumanController()
            break
        else:
            print(f'Unknown command: {inp}')

    return (player_one, player_two)


class Controller():
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.passes = 0

    def process_player(self, game, player, color):
        if game.get_coverage(color):
            cell_idx = player.get_input(game, color)
            game.make_turn(cell_idx, color)
        else:
            self.passes += 1

    def process(self, game):
        while True:
            self.passes = 0
            self.process_player(game, self.player_one, "b")
            self.process_player(game, self.player_two, "w")
            if self.passes == 2:
                break
        game.is_finished = True
