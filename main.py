import arcade
import os
import time
import random
from enum import Enum
from time import sleep

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


class Bullet(arcade.Sprite):
    def __init__(self, image_path, scale, x, y, cx):
        super().__init__(image_path, scale)
        self.center_x = x
        self.center_y = y
        self.change_x = cx

    def update(self):
        super().update()
        if self.center_x < 10 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.kill()

    # def on_draw(self):
    #     arcade.draw_circle_filled(self.center_x, self.center_y, 5, arcade.color.GREEN)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 100

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "DodgeTheBullet")
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.frame_count = 0
        self.random_bullet_delay = 0
        self.game_over = False

        self.all_sprite_list = None
        self.bullet_list = None
        self.player = None

        self.score = 0

    def start_new_game(self):
        self.frame_count = 0
        self.cached_score = 0
        self.game_over = False

        self.all_sprite_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.player = StickMan("images/man_standing.png")
        self.all_sprite_list.append(self.player)

    def generate_bullet(self):
        self.test_bullet = Bullet("images/bullet.png", 1.0, 600, 70, -20)
        self.bullet_list.append(self.test_bullet)
        self.all_sprite_list.append(self.test_bullet)

    def on_draw(self):
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()
        self.all_sprite_list.draw()
        
        if self.game_over:
            arcade.draw_text(str(self.score), 100, 50, arcade.color.RED, 23)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_x -= 5
        elif symbol == arcade.key.RIGHT:
            self.player.change_x += 5
        elif symbol == arcade.key.DOWN:
            self.player.kneel()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.player.change_x = 0
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = 0
        elif symbol == arcade.key.DOWN:
            self.player.stand()

    def update(self, x):
        if not self.player.dead:
            self.frame_count += 1
            self.all_sprite_list.update()

            for bullet in self.bullet_list:
                collision = arcade.check_for_collision(bullet, self.player)
                if collision:
                    bullet.kill()
                    self.player.kill()
                    self.game_over = True

            if self.player._state == States.STAND:
                self.score += 1
            
            if self.random_bullet_delay == 0:
                self.random_bullet_delay = random.randint(25, 100)
            if not self.frame_count % self.random_bullet_delay:
                self.generate_bullet()
                self.random_bullet_delay = 0
        else:
            print(self.score)
            sleep(2)
            arcade.close_window()

    def get_bullets(self):
        return self.bullet_list


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

game = MyGame()
game.start_new_game()

t0 = time.time()
arcade.run()
t1 = time.time()
print("time elapsed: ", t1-t0)

print(game.get_bullets())