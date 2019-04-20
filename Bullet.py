import arcade


class Bullet(arcade.Sprite):
    def __init__(self, image_path, scale, x, y, cx):
        super().__init__(image_path, scale)
        self.center_x = x
        self.center_y = y
        self.change_x = cx

    def __str__(self):
        return "Pos: {}".format(self.center_x)

    def update(self):
        super().update()
        if self.center_x < 10 or self.center_x > 1500 or \
                self.center_y > 1100 or self.center_y < -100:
            self.kill()