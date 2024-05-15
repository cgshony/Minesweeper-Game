"""
This module initializes and runs the Minesweeper game, including setting up the main window,
creating the game grid, and allowing the player to select the difficulty level.
"""

from tkinter import *
from cell_config import Cell
import settings



def set_difficulty(difficulty):  #Set the difficulty for the gameplay.
    global center_frame
    print("Selected difficulty:", difficulty)

    if difficulty == "Easy":
        settings.GRID_SIZE = settings.EASY.grid_size
        settings.MINES_COUNT = settings.EASY.mines_count
    elif difficulty == "Medium":
        settings.GRID_SIZE = settings.MEDIUM.grid_size
        settings.MINES_COUNT = settings.MEDIUM.mines_count
    elif difficulty == "Hard":
        settings.GRID_SIZE = settings.HARD.grid_size
        settings.MINES_COUNT = settings.HARD.mines_count

    # Clear existing cells to correspond to the chosen level
    for cell in Cell.all:
        if cell.cell_button_object:
            cell.cell_button_object.destroy()
    Cell.all.clear()

    Cell.cell_count = settings.GRID_SIZE * settings.GRID_SIZE  # Update cell count based on grid size

    # Recreate the center frame
    center_frame.destroy()
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

    # Create new cells
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_button_obj(center_frame)
            c.cell_button_object.grid(column=x, row=y)

    Cell.cell_count_label_obj.configure(
        text=f"Remaining cells: {Cell.cell_count}",
        width=30,
        height=5,
        font=('', 15)
    )
    Cell.randomize_mines()

#Create buttons to select the difficulty level.
def create_difficulty_buttons(root):
    difficulties = ["Easy", "Medium", "Hard"]
    button_frame = Frame(root, bg='black')
    button_frame.place(x=0, y=settings.height_percentage(25))

    for idx, difficulty in enumerate(difficulties):
        button = Button(button_frame, text=difficulty, command=lambda d=difficulty: set_difficulty(d))
        button.grid(row=0, column=idx, padx=10)

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=settings.height_percentage(15)
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
    width=settings.width_percentage(20),
    height=settings.height_percentage(75)
)
left_frame.place(x=0, y=settings.height_percentage(25))
create_difficulty_buttons(left_frame)

center_frame = Frame(
    root,
    bg='black',
    width=settings.width_percentage(85),
    height=settings.height_percentage(80)
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
Cell.cell_count_label_obj.configure(font=('', 15)) #ensire font size is consitent


# Randomize mines after creating the cells and labels
Cell.randomize_mines()

# Run the main loop
print("Running the game")
root.mainloop()
