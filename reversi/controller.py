import random

class HumanController():
    def get_input(self, game, color):
        pass


class BotController():
    def get_input(self, game, color):
        coverage = game.get_coverage(color)
        return random.choice(coverage.keys())


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
