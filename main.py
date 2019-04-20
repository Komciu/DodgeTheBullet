import arcade
import os
import time
from enum import Enum
from Game import MyGame


game = MyGame()
game.start_new_game()

t0 = time.time()
arcade.run()
t1 = time.time()
print("time elapsed: ", t1-t0)

for bullet in game.get_bullets():
    print(bullet)