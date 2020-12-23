from reversi.controller import prepare
from reversi.pygame_view import PygameView
from reversi.reversi import Reversi
from reversi.runner import Runner

view = PygameView()
game = Reversi()
game.views.append(view)

players = prepare(view)
runner = Runner(*players)
view.update(game)
while True:
    runner.process(game)
