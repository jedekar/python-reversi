from reversi.reversi import Reversi
from reversi.controller import BotController, HumanController, prepare
from reversi.runner import Runner
from reversi.console_view import ConsoleView

game = Reversi()
players = prepare()
runner = Runner(*players)
view = ConsoleView()
game.views.append(view)
print("Welcome to Reversi!",
      "Type RESTART or FINISH to restart or finish respectively.")
view.update(game)
while not game.is_finished:
    runner.process(game)
view.update(game)
