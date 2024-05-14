WIDTH = 1440
HEIGHT = 720
GRID_SIZE = 6
CELLS_COUNT = GRID_SIZE ** 2
MINES_COUNT = CELLS_COUNT // 4

class DifficultyLevel:
    def __init__(self, name, grid_size):
        self.name = name
        self.grid_size = grid_size

EASY = DifficultyLevel("Easy", 6)
MEDIUM = DifficultyLevel("Medium", 8)
HARD = DifficultyLevel("Hard", 10)

def height_percentage(percentage):
    return (HEIGHT/100) * percentage

def width_percentage(percentage):
    return (WIDTH / 100) * percentage
