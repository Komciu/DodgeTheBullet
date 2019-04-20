import arcade
import os
from StickMan import StickMan, States
import random
from Bullet import Bullet
from time import sleep

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
