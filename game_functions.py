from random import randint, shuffle
from time import sleep

import pygame as pg
from pygame.sprite import Group

from aim_results_table import AimsResultsTable
from button import Button
from text import Text


class GameFunctions:
    def __init__(self, screen, settings, score_table, game_stats):
        self.screen = screen
        self.settings = settings
        self.score_table = score_table
        self.game_stats = game_stats
        self.row1 = Group()
        self.row2 = Group()
        self.row3 = Group()
        self.row4 = Group()
        self.row5 = Group()
        self.rows = (self.row1, self.row2, self.row3, self.row4, self.row5)
        self.aims_results_table = AimsResultsTable(self.screen, ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'])

    def create_aims_and_results(self):
        aims = []
        results = ['0', '0', '0', '0', '0']

        for i in range(5):
            aims.append(str(randint(1, 255)))

        if self.game_stats.level <= 5:
            aims = [str(2 ** x) for x in [1, 2, 4, 6, 7]]
            shuffle(aims)

        self.aims_results_table.prepare_ames(aims)
        self.aims_results_table.prepare_results(results)

    def create_buttons(self):
        self.screen.fill(self.settings.SCREEN_COLOR)

        y = 100
        for row in self.rows:
            for x in range(260, 721, self.settings.BUTTON_WIDTH + 10):
                new_button = Button(self.screen, x, y, self.settings.BUTTON_WIDTH, self.settings.BUTTON_HEIGHT, '0')
                new_button.draw_button()
                row.add(new_button)
                pg.display.flip()
                sleep(0.1)
            y += self.settings.BUTTON_HEIGHT + 10

        self.check_button = Button(self.screen, self.settings.WIDTH - 110, self.settings.HEIGHT - 40, 105, 35, 'Check')
        self.check_button.color = (0, 255, 0)

    def click_check_button(self):
        if self.aims_results_table.aims == self.aims_results_table.results:
            win_text = Text(self.screen, 250, 570, "All Correct 25/25 XP", (0, 255, 0))
            win_text.show_msg()
            self.game_stats.xp += 25
            self.game_stats.solved_exercises += 1
            self.game_stats.level = self.game_stats.solved_exercises // 2
            self.score_table.prepare_xp("XP: " + str(self.game_stats.xp))
            self.score_table.prepare_exercises("Solved Exercises: " + str(self.game_stats.solved_exercises))
            self.score_table.prepare_level("Level: " + str(self.game_stats.level))

        else:
            not_win_text = Text(self.screen, 250, 570, "Something is incorrect 10/25 XP", (150, 0,  50))
            not_win_text.show_msg()
            self.game_stats.xp += 10
            self.score_table.prepare_xp("XP: " + str(self.game_stats.xp))

        self.create_aims_and_results()
        for row in self.rows:
            for button in row:
                button.value = '0'
                button.color = (30, 166, 217)
                assert isinstance(button, Button)
                button.prepare_msg()

        pg.display.flip()

        sleep(1.5)

    def check_events(self):
        for evt in pg.event.get():
            match evt.type:
                case pg.QUIT:
                    exit(0)
                case pg.KEYDOWN:
                    if evt.key == pg.K_ESCAPE:
                        exit(0)
                case pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    for row in self.rows:
                        for button in row:
                            if button.rect.collidepoint(mouse_x, mouse_y):
                                assert isinstance(button, Button)
                                button.clicked()
                    if self.check_button.rect.collidepoint(mouse_x, mouse_y):
                        self.click_check_button()

    def update_screen(self):
        self.screen.fill(self.settings.SCREEN_COLOR)

        self.score_table.draw_table()

        for row in self.rows:
            for button in row:
                assert isinstance(button, Button)
                button.draw_button()

        self.update_results()

        self.aims_results_table.show()

        self.check_button.draw_button()

        pg.display.flip()

    def update_results(self):
        results = [[], [], [], [], []]
        count = 0
        for row in self.rows:
            for r in row:
                results[count].append(r.value)
            count += 1

        prep_results = []
        for r in results:
            prep_results.append(str(int(''.join(r), 2)))

        self.aims_results_table.prepare_results(prep_results)
