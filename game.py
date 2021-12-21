from button import Button


class Game:
    """Класс предназначеный для управления экранами игры."""
    def __init__(self, screen, score_table, rows, aims_results_table, check_button, stats):
        self.screen = screen
        self.score_table = score_table
        self.rows = rows
        self.aims_results_table = aims_results_table
        self.check_button = check_button
        self.stats = stats

    def draw(self):
        match self.stats.game_state:
            case 0:
                pass
            case 1:
                self.score_table.draw_table()

                for row in self.rows:
                    for button in row:
                        assert isinstance(button, Button)
                        button.draw_button()

                self.aims_results_table.show()

                self.check_button.draw_button()
