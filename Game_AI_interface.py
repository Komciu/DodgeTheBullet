import arcade
import os
import time
from enum import Enum
from Game import MyGame


class AI_game(MyGame):
    def __init__(self):
        super().__init__()

    def on_key_press(self, symbol, modifiers):
        self.on_key_press_virtual(symbol, modifiers)

    def on_key_press_virtual(self, symbol, modifiers):
        print("virt")
        super().on_key_press(arcade.key.DOWN, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.on_key_release_virtual(symbol, modifiers)

    def on_key_release_virtual(self, symbol, modifiers):
        print("virt2")
        super().on_key_press(arcade.key.RIGHT, modifiers)