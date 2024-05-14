class Difficulty:
    def __init__(self, grid_size, mines_count):
        self.grid_size = grid_size
        self.mines_count = mines_count

EASY = Difficulty(grid_size=8, mines_count=9)
MEDIUM = Difficulty(grid_size=16, mines_count=35)
HARD = Difficulty(grid_size=20, mines_count=40)

# Default difficulty level
GRID_SIZE = EASY.grid_size
MINES_COUNT = EASY.mines_count

# Add these functions to calculate width and height percentages
def width_percentage(percentage):
    return int(WIDTH * percentage / 100)

def height_percentage(percentage):
    return int(HEIGHT * percentage / 100)

# Define the window dimensions
WIDTH = 1250
HEIGHT = 800
