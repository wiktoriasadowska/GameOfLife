import arcade
from gui import Menu

def start_game():
    ROW_COUNT = 50
    COLUMN_COUNT = 50
    CELL_SIZE = 12
    WINDOW_WIDTH = COLUMN_COUNT * CELL_SIZE
    WINDOW_HEIGHT = ROW_COUNT * CELL_SIZE
    WINDOW_TITLE = "Conway's Game of Life"

    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    start_view = Menu(CELL_SIZE, COLUMN_COUNT, ROW_COUNT, WINDOW_WIDTH, WINDOW_HEIGHT)
    window.show_view(start_view)

    arcade.run()

start_game()
