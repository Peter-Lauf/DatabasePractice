from tkinter import *
import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import messagebox
import frames_widgets
from student_data import StudentData

class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SDA Course Tracking System")
        self.geometry("1550x800+0+0")

        # Main title and frame
        self.sda_title = Label(
            self,
            text="SDA Course Study Tracking".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=20,
            relief=RIDGE,
            font=("arial", 50, "bold"),
            padx=2,
            pady=6,
        )

        self.sda_title.pack(side=TOP, fill=X)

        self.frame = Frame(self, bd=15, relief=RIDGE, padx=20, bg="mediumpurple4")
        self.frame.place(x=0, y=130, width=1550, height=400)
        self.data = StudentData()

if __name__ == "__main__":
    root = MainFrame()
    frames_widgets.create_frames_widgets(root)
    root.mainloop()