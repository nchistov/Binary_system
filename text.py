import pygame as pg


class Text:
    def __init__(self, screen, x, y, msg: str, text_color):
        self.x = x
        self.y = y
        self.msg = msg
        self.screen = screen
        self.text_color = text_color

        self.font = pg.font.SysFont('', 45)
        self.prepare_msg(self.msg)

    def prepare_msg(self, msg: str):
        self.msg_image = self.font.render(msg, True, self.text_color)

        self.msg_rect = self.msg_image.get_rect()
        self.msg_rect.centerx = self.x
        self.msg_rect.centery = self.y

    def show_msg(self):
        self.screen.blit(self.msg_image, self.msg_rect)
