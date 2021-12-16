import pygame as pg

from game_functions import GameFunctions
from game_stats import GameStats
from score_table import ScoreTable
from settings import Settings


def main():
    pg.init()

    settings = Settings()

    screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
    pg.display.set_caption("--- Binary System ---")

    score_table = ScoreTable(screen, settings)

    game_stats = GameStats()

    gf = GameFunctions(screen, settings, score_table, game_stats)

    clock = pg.time.Clock()

    gf.create_buttons()
    gf.create_aims_and_results()

    while True:
        gf.update_screen()
        gf.check_events()

        clock.tick(settings.FPS)


try:
    main()
finally:
    pg.quit()
