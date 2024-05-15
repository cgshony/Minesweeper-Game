"""
This module defines the Cell class used in the Minesweeper game,
including the methods for cell interactions, mine randomization, and cell count updates.
"""

from tkinter import Button, Label
import random
import ctypes
import settings
import sys

class Cell:
    """
        Represent a cell in the Minesweeper game.
        Attributes:
            x: The x-coordinate of the cell.
            y: The y-coordinate of the cell.
            is_mine: Bool whether the cell is a mine.
        """
    all = []
    cell_count = 0
    cell_count_label_obj = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_potential_mine = False
        self.cell_button_object = None
        self.x = x
        self.y = y
        Cell.all.append(self)

    def create_button_obj(self, location):  # Creates a button for the cell.
        button = Button(
            location,
            width=2,  # Adjust width for better appearance
            height=1,  # Adjust height
        )
        button.bind('<Button-1>', self.left_click_actions)
        button.bind('<Button-3>', self.right_click_actions)
        self.cell_button_object = button
        return button

    @staticmethod
    def create_cell_count_label(location): #Create a label to display the remaining cells during gameplay.
        label = Label(
            location,
            text=f"Remaining cells: {Cell.cell_count}",
            width=25,
            height=5,
            font=('', 15),
            anchor='w',  # Ensure the text remains left-aligned
            justify='left',  # Ensure the text remains left-aligned
            bg='black',
            fg='white'
        )
        Cell.cell_count_label_obj = label

    def left_click_actions(self, event):  #Handle left-click actions on the cell.
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounding_cells_mines_count == 0:
                for cell_obj in self.surrounding_cells:
                    cell_obj.show_cell()
            self.show_cell()
        if Cell.cell_count == 0:
            ctypes.windll.user32.MessageBoxW(0, 'You won the game!', 0)
        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):  #Get the surrounding cells of the current cell.
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_cells_mines_count(self):   #Count the number of mines in the surrounding cells.
        counter = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):   #Show the cell's content.
        if self.cell_button_object:
            if not self.is_opened:
                self.is_opened = True
                Cell.cell_count -= 1
                self.cell_button_object.configure(text=self.surrounding_cells_mines_count)
                if Cell.cell_count_label_obj:
                    Cell.cell_count_label_obj.configure(
                        text=f"Remaining cells: {Cell.cell_count}",
                        font=('', 15)
                    )
                self.cell_button_object.configure(bg='SystemButtonFace')

    def show_mine(self):   #Show the mine and end the game.
        if self.cell_button_object:
            self.cell_button_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine.', 'Game Over', 0)
        sys.exit()

    def right_click_actions(self, event):  # Handle right-click actions on the cell.
        if not self.is_potential_mine:
            self.cell_button_object.configure(bg='orange')
            self.is_potential_mine = True
        else:
            self.cell_button_object.configure(bg='SystemButtonFace')
            self.is_potential_mine = False

    @staticmethod
    def randomize_mines():   # Randomize the mines in the grid.
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'