from tkinter import *
import settings

def create_difficulty_buttons(root):
    def set_difficulty(difficulty):
        print("Selected difficulty:", difficulty)

    difficulties = ["Easy", "Medium", "Hard"]
    button_frame = Frame(root, bg='black')
    button_frame.place(x=0, y=settings.height_percentage(25))

    for idx, difficulty in enumerate(difficulties):
        button = Button(button_frame, text=difficulty, command=lambda d=difficulty: set_difficulty(d))
        button.grid(row=0, column=idx, padx=10)

if __name__ == "__main__":
    root = Tk()
    root.configure(bg="black")
    root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
    root.title('Choose Difficulty')
    root.resizable(False, False)

    create_difficulty_buttons(root)

    root.mainloop()
