import arcade
import random
from colors import get_background_color, get_cell_color

class BaseGame(arcade.View):
    def __init__(self, cell, grid_width, grid_height):
        super().__init__()
        arcade.set_background_color(get_background_color())

        self.cell = cell
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid = [[0 for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        self.game_started = False

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 1:
                    color = get_cell_color()
                    arcade.draw_circle_filled(
                        col * self.cell + self.cell / 2,
                        row * self.cell + self.cell / 2,
                        self.cell / 2,
                        color
                    )

    def on_update(self, delta_time):
        if self.game_started:
            self.grid = self.calculate_next_generation()

    def calculate_next_generation(self):
        new_grid = [[0] * self.grid_width for _ in range(self.grid_height)]
        for current_row in range(self.grid_height):
            for current_col in range(self.grid_width):
                neighbors = self.count_neighbors(current_row, current_col)
                if self.grid[current_row][current_col] == 1 and (neighbors == 2 or neighbors == 3):
                    new_grid[current_row][current_col] = 1
                elif self.grid[current_row][current_col] == 0 and neighbors == 3:
                    new_grid[current_row][current_col] = 1
        return new_grid

    def count_neighbors(self, row, col):
        count = 0
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                neighbor_row = row + row_offset
                neighbor_col = col + col_offset
                if (
                    0 <= neighbor_row < self.grid_height
                    and 0 <= neighbor_col < self.grid_width
                    and not (row_offset == 0 and col_offset == 0)
                ):
                    count += self.grid[neighbor_row][neighbor_col]
        return count

    def on_mouse_press(self, x, y, button, modifiers):
        clicked_col = int(x // self.cell)
        clicked_row = int(y // self.cell)

        if (
            0 <= clicked_row < self.grid_height
            and 0 <= clicked_col < self.grid_width
        ):
            self.grid[clicked_row][clicked_col] = 1 - self.grid[clicked_row][clicked_col]

class Game_Random(BaseGame):
    def __init__(self, cell, grid_width, grid_height):
        super().__init__(cell, grid_width, grid_height)
        self.grid = [[random.choice([0, 1]) for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        
    def on_update(self, delta_time):
        self.game_started = True
        super().on_update(delta_time)
        
class Game_Custom(BaseGame):
    def __init__(self, cell, grid_width, grid_height):
        super().__init__(cell, grid_width, grid_height)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.game_started = True

class BasePatternGame(BaseGame):
    def __init__(self, cell, pattern_file_path):
        super().__init__(cell, 0, 0)
        self.load_pattern(pattern_file_path)

    def load_pattern(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines.reverse()

            grid_height = len(lines)
            grid_width = len(lines[0].strip())

            self.grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]

            for j in range(grid_height):
                for i in range(grid_width):
                    self.grid[j][i] = 1 if lines[j][i] == 'X' else 0

            self.grid_height = grid_height
            self.grid_width = grid_width

    def on_update(self, delta_time):
        self.game_started = True
        super().on_update(delta_time)

class Game_Glider(BasePatternGame):
    def __init__(self, cell):
        super().__init__(cell, 'sample_patterns/glider.txt')

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = Game_Gosper(self.cell)
            game_view.setup()
            self.window.show_view(game_view)

class Game_Gosper(BasePatternGame):
    def __init__(self, cell):
        super().__init__(cell, 'sample_patterns/gosper-glider-gun.txt')

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = Game_Pulsar(self.cell)
            game_view.setup()
            self.window.show_view(game_view)

class Game_Pulsar(BasePatternGame):
    def __init__(self, cell):
        super().__init__(cell, 'sample_patterns/pulsar.txt')

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = Game_Glider(self.cell)
            game_view.setup()
            self.window.show_view(game_view)
