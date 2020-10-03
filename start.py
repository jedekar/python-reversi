from reversi.reversi import Reversi
from reversi.controller import BotController
from reversi.runner import Runner
from reversi.console_view import ConsoleView

game = Reversi()
player_one = BotController()
player_two = BotController()
runner = Runner(player_one, player_two)
view = ConsoleView()
game.views.append(view)
view.update(game)
runner.process(game)
view.update(game)
