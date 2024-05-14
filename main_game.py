from tkinter import *
from cell_config import Cell
import settings


def set_difficulty(difficulty):
    global center_frame  # Declare center_frame as a global variable
    print("Selected difficulty:", difficulty)

    # Set the grid size and mines count based on difficulty
    if difficulty == "Easy":
        settings.GRID_SIZE = settings.EASY.grid_size
        settings.MINES_COUNT = settings.EASY.mines_count
    elif difficulty == "Medium":
        settings.GRID_SIZE = settings.MEDIUM.grid_size
        settings.MINES_COUNT = settings.MEDIUM.mines_count
    elif difficulty == "Hard":
        settings.GRID_SIZE = settings.HARD.grid_size
        settings.MINES_COUNT = settings.HARD.mines_count

    # Destroy all existing buttons and clear the Cell.all list
    for cell in Cell.all:
        if cell.cell_button_object:
            cell.cell_button_object.destroy()
    Cell.all.clear()

    # Reset the cell count
    Cell.cell_count = settings.GRID_SIZE ** 2

    # Regenerate cells based on the new grid size
    center_frame.destroy()  # Clear existing cells
    center_frame = Frame(
        root,
        bg='black',
        width=settings.width_percentage(75),
        height=settings.height_percentage(75)
    )
    center_frame.place(
        x=settings.width_percentage(25),
        y=settings.height_percentage(25)
    )

    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_button_obj(center_frame)
            c.cell_button_object.grid(column=x, row=y)

    # Update the remaining cells count label
    Cell.cell_count_label_obj.configure(text=f"Remaining cells: {Cell.cell_count - settings.MINES_COUNT}")

    # Randomize mines after creating the cells and labels
    Cell.randomize_mines()

# Ensure difficulty buttons are created only once

def create_difficulty_buttons(root):
    difficulties = ["Easy", "Medium", "Hard"]
    button_frame = Frame(root, bg='black')
    button_frame.place(x=0, y=settings.height_percentage(25))

    for idx, difficulty in enumerate(difficulties):
        button = Button(button_frame, text=difficulty, command=lambda d=difficulty: set_difficulty(d))
        button.grid(row=0, column=idx, padx=10)



root = Tk()  # creates a window
# override settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)  # not allowed to resize wind

"""--------Difficulty"""
# Define difficulty levels

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=settings.height_percentage(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(x=settings.width_percentage(25), y=0)

left_frame = Frame(
    root,
    bg='black',
    width=settings.width_percentage(25),
    height=settings.height_percentage(75)
)
left_frame.place(x=0, y=settings.height_percentage(25))
create_difficulty_buttons(left_frame)  # Call the function here

center_frame = Frame(
    root,
    bg='black',
    width=settings.width_percentage(75),
    height=settings.height_percentage(75)
)
center_frame.place(
    x=settings.width_percentage(25),
    y=settings.height_percentage(25)
)

# Generate cells and randomize mines
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_obj(center_frame)
        c.cell_button_object.grid(column=x, row=y)

# Create the remaining cells count label
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

# Randomize mines after creating the cells and labels
Cell.randomize_mines()

print("Running the main loop")
# Run the window
root.mainloop()
