from button import Button
from text import Text


class Game:
    """Класс предназначеный для управления экранами игры."""
    def __init__(self, screen, score_table, rows, aims_results_table, check_button, stats):
        self.screen = screen
        self.score_table = score_table
        self.rows = rows
        self.aims_results_table = aims_results_table
        self.check_button = check_button
        self.stats = stats

        self.title = Text(screen, 500, 50, 'Binary System', (255, 200, 255))
        self.play_btn = Button(screen, 425, 300, 150, 50, 'Play')

    def draw(self):
        match self.stats.game_state:
            case 0:
                self.title.show_msg()
                self.play_btn.draw_button()
            case 1:
                self.score_table.draw_table()

                for row in self.rows:
                    for button in row:
                        assert isinstance(button, Button)
                        button.draw_button()

                self.aims_results_table.show()

                self.check_button.draw_button()
