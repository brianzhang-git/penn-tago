import pentago as p
import numpy as np
import random


a, o = p.init_game()
a, o, s = p.move_debug(a, (0, 1), 4, 1)
a, o, s = p.move_debug(a, (0, 0), 4, 1)
a, o, s = p.move_debug(a, (1, 1), 4, 1)
a, o, s = p.move_debug(a, (1, 0), 4, 1)
a, o, s = p.move_debug(a, (2, 1), 4, 1)
a, o, s = p.move_debug(a, (2, 0), 4, 1)
a, o, s = p.move_debug(a, (3, 1), 4, 1)
a, o, s = p.move_debug(a, (3, 0), 4, 1)
a, o, s = p.move_debug(a, (5, 1), 4, 1)
a, o, s = p.move_debug(a, (4, 0), 4, 1)
print(s)
p.show_board(a)