import pygame as pg

from text import Text


class ScoreTable:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.bg = pg.Rect(0, 0, self.settings.WIDTH, 70)
        self.table_xp = pg.Rect(5, 5, 318, 60)
        self.table_exercises = pg.Rect(677, 5, 318, 60)

        self.xp_text = Text(self.screen, 70, 30, "XP: 0", (255, 200, 255))
        self.level_text = Text(self.screen,  self.settings.WIDTH / 2, 30, "Level: 0", self.settings.SCREEN_COLOR)
        self.exercises_text = Text(self.screen, self.settings.WIDTH - 170, 30, "Solved Exercises: 0", (255, 200, 255))

    def prepare_xp(self, xp):
        self.xp_text.prepare_msg(xp)

    def prepare_level(self, level):
        self.level_text.prepare_msg(level)

    def prepare_exercises(self, exercises):
        self.exercises_text.prepare_msg(exercises)

    def draw_table(self):
        pg.draw.rect(self.screen, (255, 255, 255), self.bg)

        pg.draw.rect(self.screen, self.settings.SCREEN_COLOR, self.table_xp)
        pg.draw.rect(self.screen, self.settings.SCREEN_COLOR, self.table_exercises)

        self.xp_text.show_msg()
        self.level_text.show_msg()
        self.exercises_text.show_msg()
