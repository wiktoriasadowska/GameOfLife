# Game of Life

Game of Life is a Python project that implements Conway's Game of Life, a cellular automaton devised by the mathematician John Conway.

## Features

The project offers three menu options for users to choose from:

1. **Generate Random Grid:**
   - Allows the user to run the game with a random placement of alive cells and observe how the automaton behaves.
   - Users can manipulate the pattern by clicking on cells while the game is running. Clicking on an alive cell kills it, and clicking on a dead one makes it alive.

2. **Make Custom Grid:**
   - Enables users to create their own custom start state for the grid by clicking on dead cells and making them alive.
   - After creating the custom pattern, users press ENTER to start the game.
   - It is also possible to manipulate the pattern while it is running using the mouse.

3. **See Examples:**
   - Allows users to view predefined examples of patterns, including Glider, Gosper Glider Gun, and Pulsar.
   - Examples are loaded from a predefined text file.
   - Users can switch between examples by pressing SPACE.
   - It is possible to manipulate the grid using the mouse, as in the previous options.

## Modifications

The `main.py` and `colors.py` files are designed for easy customization:
- You can change the code to choose the desired size of the grid and cell size, resulting in changes to the window size, however keep in mind that the visibility of examples depends on it.
- Easily modify the colors of the background (dead cells) and alive cells. The default is pink, but you can choose from other colors in the `arcade.color` package.


