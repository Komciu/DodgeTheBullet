import arcade
from enum import Enum


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 100

class States(Enum):
    STAND = 0
    KNEEL = 1

class StickMan(arcade.Sprite):
    def __init__(self, image_path, scale = 1):
        super().__init__(image_path, scale)
        self._state = States.STAND
        self.respawn()
        self.dead = False
        self.score = 0

    def update(self):
        super().update()

    def get_state(self):
        return self._state

    def kneel(self):
        self.center_y = 20
        self._state = States.KNEEL

    def stand(self):
        self.center_y = 50
        self._state = States.STAND

    def respawn(self):
        self.center_x = 50
        self.center_y = SCREEN_HEIGHT / 2
        self.angle = 0
        self.respawning = True

    def kill(self):
        print("KILL")
        self.dead = True
        super().kill()