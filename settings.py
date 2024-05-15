"""
This module defines the game settings for Minesweeper, including the grid size and mine count
for different difficulty levels, as well as helper functions for calculating width and height percentages.
"""

class Difficulty:
    #Represent the difficulty levels.
    def __init__(self, grid_size, mines_count):
        self.grid_size = grid_size
        self.mines_count = mines_count

# Define difficulty levels
EASY = Difficulty(grid_size=8, mines_count=9)
MEDIUM = Difficulty(grid_size=16, mines_count=30)
HARD = Difficulty(grid_size=20, mines_count=75)

# Default difficulty level
GRID_SIZE = EASY.grid_size
MINES_COUNT = EASY.mines_count

#Define the window dimensions
WIDTH = 1250
HEIGHT = 800

def width_percentage(percentage):

    return int(WIDTH * percentage / 100)   #Calculate the width percentage of a window.

def height_percentage(percentage):

    return int(HEIGHT * percentage / 100)  #Calculate the height percentage of the window.
