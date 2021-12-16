import pygame as pg
from pygame.sprite import Sprite

from text import Text


class Button(Sprite):
    def __init__(self, screen, x, y, width, height, msg):
        super().__init__()

        self.screen = screen
        self.width = width
        self.height = height
        self.color = (30, 166, 217)
        self.x = x
        self.y = y
        self.value = msg

        self.rect = pg.Rect(x, y, width, height)

        self.text = Text(self.screen, self.rect.centerx, self.rect.centery, self.value, (0, 10, 0))

        self.prepare_msg()

    def prepare_msg(self):
        self.text.prepare_msg(self.value)

    def clicked(self):
        if self.value == '0':
            self.value = '1'
            self.color = (230, 217, 32)
        else:
            self.value = '0'
            self.color = (30, 166, 217)

        self.prepare_msg()

    def draw_button(self):
        pg.draw.polygon(self.screen, self.color, ((self.x + 5, self.y),
                                                  (self.x + self.width - 5, self.y),
                                                  (self.x + self.width, self.y + 5),
                                                  (self.x + self.width, self.y + self.height - 5),
                                                  (self.x + self.width - 5, self.y + self.height),
                                                  (self.x + 5, self.y + self.height),
                                                  (self.x, self.y + self.height - 5),
                                                  (self.x, self.y + 5)))
        self.text.show_msg()
