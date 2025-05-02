import pygame as pg

from text import Text


class AimsResultsTable:
    def __init__(self, screen, aims, results):
        self.screen = screen
        self.aims = aims
        self.text_aims = []
        self.results = results
        self.text_results = []
        x = 220
        y = 135
        for aim in self.aims:
            text = Text(self.screen, x, y, aim, (255, 200, 255))
            self.text_aims.append(text)
            y += 70 + 10

        x = 780
        y = 135

        for result in self.results:
            text = Text(self.screen, x, y, result, (255, 200, 255))
            self.text_results.append(text)
            y += 70 + 10

        self.prepare_ames(self.aims)
        self.prepare_results(self.results)

    def prepare_ames(self, ames: list[str]):
        for aim, prep_ame in zip(self.text_aims, ames):
            aim.prepare_msg(prep_ame)
        self.aims = ames

    def prepare_results(self, results: list[str]):
        for result, prep_result in zip(self.text_results, results):
            result.prepare_msg(prep_result)
        self.results = results

    def show(self):
        for aim in self.text_aims:
            aim.show_msg()
        for result in self.text_results:
            result.show_msg()
