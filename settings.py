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