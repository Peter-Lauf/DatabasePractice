import tkinter as tk
from tkinter import *
from tkinter import ttk, StringVar
from tkinter import messagebox
import db_helper
import datetime


# -------- Right Frame -------- #
class RightFrame(ttk.Frame):
    def __init__(self, container, data):
        super().__init__(container)
        self.data = data
        self.data_frame_right = LabelFrame(
            container,
            text="Course modules".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=12,
            relief=RIDGE,
            font=("arial", 12, "bold"),
        )

        self.data_frame_right.place(x=910, y=150, width=615, height=350)


class RightFrameWidgets(RightFrame):
    def __init__(self, container, data):
        RightFrame.__init__(self, container, data)

        self.data = data
        self.txt_box = Text(
            self.data_frame_right,
            font=("arial", 12, "bold"),
            width=36,
            height=15,
            padx=2,
            pady=6,
        )
        self.txt_box.grid(row=0, column=2)

        self.list_scroll_bar = Scrollbar(self.data_frame_right)
        self.list_scroll_bar.grid(row=0, column=1, sticky="ns")

        self.list_modules = [
            "Python Developer - introduction",
            "Python - the basics",
            "Git system",
            "Python - technology",
            "Software testing and TDD",
            "Python - intermediate",
            "Algorithms and data structures",
            "Design patterns and good practices",
            "SQL databases",
            "Databases - programming",
            "HTTP basics",
            "HTML,CSS,JavaScript",
            "Backend technologies",
            "Final project",
        ]

        self.list_box = Listbox(
            self.data_frame_right, font=("arial", 10, "bold"), width=26, height=18
        )
        self.list_box.bind("<<ListboxSelect>>", self.select_module)
        self.list_box.grid(row=0, column=0, padx=4)
        self.list_scroll_bar.config(command=self.list_box.yview)

        for item in self.list_modules:
            self.list_box.insert(END, item)

    def select_module(self, event=""):
        choice = str(self.list_box.get(self.list_box.curselection()))
        self.set_module(choice)

    def set_module(self, choice):
        d1 = datetime.date.today()
        self.data.course_module_var.set(f"{choice}")
        self.data.study_date.set(d1.strftime("%m/%d/%Y"))


# -------- Left Frame -------- #
class LeftFrame(ttk.Frame):
    def __init__(self, container, data):
        super().__init__(container)

        self.data = data
        self.data_frame_left = LabelFrame(
            container,
            text="Student Details".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=12,
            relief=RIDGE,
            font=("arial", 12, "bold"),
        )

        self.data_frame_left.place(x=25, y=150, width=865, height=350)

        # Prompt user to choose user type
        self.user_type = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            font=("arial", 12, "bold"),
            text="User Type",
            padx=10,
            pady=15,
        )
        self.user_type.grid(row=0, column=0, sticky=W)


class LeftFrameWidgets(LeftFrame):
    def __init__(self, container, data):
        LeftFrame.__init__(self, container, data)

        self.data = data
        self.com_user_type = ttk.Combobox(
            self.data_frame_left,
            textvariable=self.data.user_var,
            state="readonly",
            font=("arial", 12, "bold"),
            width=25,
        )
        self.com_user_type["value"] = ("Student", "Admin", "Trainer")
        self.com_user_type.current(0)
        self.com_user_type.grid(row=0, column=1)

        # Prompt user first name
        self.student_first_name = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="First name: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.student_first_name.grid(row=1, column=0, sticky=W)

        self.txt_student_first_name = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            width=27,
        )
        self.txt_student_first_name.grid(row=1, column=1)

        # Prompt user last name
        self.student_last_name = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="Last name: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.student_last_name.grid(row=2, column=0, sticky=W)

        self.txt_student_last_name = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            width=27,
        )
        self.txt_student_last_name.grid(row=2, column=1)

        # Prompt user course name
        self.sda_course_name = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="Course name: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.sda_course_name.grid(row=3, column=0, sticky=W)

        self.txt_sda_course_name = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            width=27,
        )
        self.txt_sda_course_name.grid(row=3, column=1)

        # Course Module autofill
        self.course_module = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="Course module: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.course_module.grid(row=0, column=2, sticky=W)

        self.txt_course_module = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.data.course_module_var,
            width=27,
        )
        self.txt_course_module.grid(row=0, column=3)

        # Date of studying autofill
        self.study_date = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="Study date: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.study_date.grid(row=1, column=2, sticky=W)

        self.txt_study_date = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.data.study_date,
            width=27,
        )
        self.txt_study_date.grid(row=1, column=3)

        # Hours studied
        self.hours_studied = Label(
            self.data_frame_left,
            bg="mediumpurple4",
            text="Hours Studied: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        self.hours_studied.grid(row=2, column=2, sticky=W)

        self.txt_hours_studied = Entry(
            self.data_frame_left,
            font=("arial", 12, "bold"),
            width=27,
        )
        self.txt_hours_studied.grid(row=2, column=3)


# -------- Buttons Frame -------- #
class ButtonsFrame(ttk.Frame):
    def __init__(self, container, data):
        super().__init__(container)
        self.data = data

        self.frame_button = Frame(
            container, bd=12, relief=RIDGE, padx=20, bg="mediumpurple4"
        )
        self.frame_button.place(x=0, y=530, width=1550, height=70)


class ButtonsWidgets(ButtonsFrame):
    def __init__(self, container, data, left_frame_widgets):
        ButtonsFrame.__init__(self, container, data)

        self.left_frame = left_frame_widgets
        self.button_add_data = Button(
            self.frame_button,
            command=self.write_to_db,
            text="Add Data",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=0, padx=3, pady=7)

        self.button_add_data = Button(
            self.frame_button,
            text="Show Data",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=1, padx=3, pady=7)

        self.button_add_data = Button(
            self.frame_button,
            text="Update",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=2, padx=3, pady=7)

        self.button_add_data = Button(
            self.frame_button,
            text="Delete",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=3, padx=3, pady=7)

        self.button_add_data = Button(
            self.frame_button,
            text="Reset",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=4, padx=3, pady=7)

        self.button_add_data = Button(
            self.frame_button,
            text="Exit",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        self.button_add_data.grid(row=0, column=5, padx=3, pady=7)

    def write_to_db(self):
        db_helper.create_tables()
        db_helper.write_data_to_db(
            self.left_frame.com_user_type.get(),
            self.left_frame.txt_student_first_name.get(),
            self.left_frame.txt_student_last_name.get(),
            self.left_frame.txt_hours_studied.get(),
            self.data.study_date.get(),
            self.left_frame.txt_sda_course_name.get(),
            self.data.course_module_var.get(),
        )


# -------- Bottom & Table Frame -------- #
class BottomFrame(ttk.Frame):
    def __init__(self, container, data):
        super().__init__(container)
        self.data = data

        self.frame_details = Frame(container, bd=12, relief=RIDGE, padx=20, bg="gray52")
        self.frame_details.place(x=0, y=600, width=1550, height=195)


class TableFrame(BottomFrame):
    def __init__(self, container, data):
        BottomFrame.__init__(self, container, data)

        self.table_frame = Frame(self.frame_details, bd=6, relief=RIDGE, bg="gray52")
        self.table_frame.place(x=-8, y=3, width=1500, height=165)


class TableWidgets(TableFrame):
    def __init__(self, container, data):
        TableFrame.__init__(self, container, data)
        self.data = data

        self.xscroll = ttk.Scrollbar(self.table_frame, orient=HORIZONTAL)
        self.yscroll = ttk.Scrollbar(self.table_frame, orient=VERTICAL)

        self.sda_table = ttk.Treeview(
            self.table_frame,
            columns=(
                "usertype",
                "firstname",
                "lastname",
                "coursename",
                "coursemodule",
                "studydate",
                "studyhours",
            ),
            xscrollcommand=self.xscroll.set,
            yscrollcommand=self.yscroll.set,
        )

        self.xscroll.pack(side=BOTTOM, fill=X)
        self.yscroll.pack(side=RIGHT, fill=Y)

        self.xscroll.config(command=self.sda_table.xview)
        self.yscroll.config(command=self.sda_table.yview)

        self.sda_table.heading("usertype", text="User Type")
        self.sda_table.heading("firstname", text="First Name")
        self.sda_table.heading("lastname", text="Last Name")
        self.sda_table.heading("coursename", text="Course Name")
        self.sda_table.heading("coursemodule", text="Course Module")
        self.sda_table.heading("studydate", text="Study Date")
        self.sda_table.heading("studyhours", text="Hours Studied")

        self.sda_table["show"] = "headings"
        self.sda_table.pack(fill=BOTH, expand=1)

        self.sda_table.column("usertype", width=100)
        self.sda_table.column("firstname", width=100)
        self.sda_table.column("lastname", width=100)
        self.sda_table.column("coursename", width=100)
        self.sda_table.column("coursemodule", width=100)
        self.sda_table.column("studydate", width=100)
        self.sda_table.column("studyhours", width=100)


# Create all the above widgets
# Function is called from _main_view.py
def create_frames_widgets(root):

    left_frame = LeftFrame(root, root.data)
    left_frame_widgets = LeftFrameWidgets(root, root.data)

    right_frame = RightFrame(root, root.data)
    right_frame_widgets = RightFrameWidgets(root, root.data)

    buttons_frame = ButtonsFrame(root, root.data)
    buttons_widgets = ButtonsWidgets(root, root.data, left_frame_widgets)

    bottom_frame = BottomFrame(root, root.data)
    table_frame = TableFrame(root, root.data)
    table_widgets = TableWidgets(root, root.data)

    return (
        left_frame,
        left_frame_widgets,
        right_frame,
        right_frame_widgets,
        buttons_frame,
        buttons_widgets,
        bottom_frame,
        table_frame,
        table_widgets,
    )
