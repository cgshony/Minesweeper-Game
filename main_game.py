from tkinter import *
from cell_config import Cell
import settings

root = Tk() #creates a window
#override settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False) #not allowed to resize wind

top_frame = Frame(
    root,
    bg='black', #change later to black
    width = settings.WIDTH,
    height= settings.height_percentage(25)
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
    bg='black', #change later to black
    width = settings.width_percentage(25),
    height= settings.height_percentage(75)
)
left_frame.place(x=0, y=settings.height_percentage(25))

center_frame = Frame(
    root,
    bg='black', #change later to black
    width = settings.width_percentage(75),
    height= settings.height_percentage(75)
)
center_frame.place(
    x=settings.width_percentage(25),
    y=settings.height_percentage(25)
)

# c1 = Cell()
# c1.create_button_obj(center_frame)
# c1.cell_button_object.grid(column=0, row=0)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_obj(center_frame)
        c.cell_button_object.grid (column=x, row=y)

#call the lable from Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_obj.place(x=0, y=0)

Cell.randomize_mines()


#run the window
root.mainloop()