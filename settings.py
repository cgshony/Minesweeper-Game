WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6
CELLS_COUNT = GRID_SIZE ** 2
MINES_COUNT = (CELLS_COUNT ) // 4

#utils

def height_percentage(percentage):
    return (HEIGHT/100) * percentage

print(height_percentage(25))

def width_percentage(percentage):
    return (WIDTH / 100) * percentage

class DifficultyLevel:
    def __init__(self, name, grid_size, mines_count):
        self.name = name
        self.grid_size = grid_size
        self.mines_count = mines_count

EASY = DifficultyLevel("Easy", 6, 6)
MEDIUM = DifficultyLevel("Medium", 8, 12)
HARD = DifficultyLevel("Hard", 10, 20)