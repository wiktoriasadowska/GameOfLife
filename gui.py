import arcade
import arcade.gui
from arcade.gui import UIManager
from logic import Game_Random, Game_Custom, Game_Glider
from colors import get_background_color

class Menu(arcade.View):
    def __init__(self, cell, grid_width, grid_height, window_width, window_height):
        super().__init__()

        self.cell = cell
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.window_width = window_width
        self.window_height = window_height

        self.manager = UIManager()
        self.manager.enable()

        self.v_box = arcade.gui.UIBoxLayout()

        ui_text_label = arcade.gui.UILabel(
            text="GAME OF LIFE",
            width=450,
            height=150,
            font_size=40,
            align='center',
            font_name='Arial Bold'
        )

        self.v_box.add(ui_text_label.with_space_around(bottom=-20))

        button1 = arcade.gui.UIFlatButton(text="Generate random grid", width=300)
        self.v_box.add(button1.with_space_around(top=-5, bottom=10))

        @button1.event("on_click")
        def on_click_button1(event):
            game_view = Game_Random(self.cell, self.grid_width, self.grid_height)
            game_view.setup()
            self.window.show_view(game_view)

        button2 = arcade.gui.UIFlatButton(text="Make custom grid", width=300)
        self.v_box.add(button2.with_space_around(top=-5, bottom=10))

        @button2.event("on_click")
        def on_click_button2(event):
            game_view = Game_Custom(self.cell, self.grid_width, self.grid_height)
            game_view.setup()
            self.window.show_view(game_view)

        button3 = arcade.gui.UIFlatButton(text="See examples", width=300)
        self.v_box.add(button3.with_space_around(top=-5, bottom=10))

        @button3.event("on_click")
        def on_click_button3(event):    
            game_view = Game_Glider(self.cell)
            game_view.setup()
            self.window.show_view(game_view)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box
            )
        )

    def on_show_view(self):
        arcade.set_background_color(get_background_color())

    def on_draw(self):
        self.clear()
        self.manager.draw()