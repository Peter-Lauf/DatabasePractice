from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime


class SDACourseTrackingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("SDA Course Tracking System")
        self.root.geometry("1550x800+0+0")

        # ================================== Variables ======================================
        self.user_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.course_name_var = StringVar()
        self.course_module_var = StringVar()
        self.study_date = StringVar()

        sda_title = Label(
            self.root,
            text="SDA Course Study Tracking".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=20,
            relief=RIDGE,
            font=("arial", 50, "bold"),
            padx=2,
            pady=6,
        )

        sda_title.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=15, relief=RIDGE, padx=20, bg="mediumpurple4")
        frame.place(x=0, y=130, width=1550, height=400)

        # ================================ Data Frame Left ===================================
        data_frame_left = LabelFrame(
            frame,
            text="Student Details".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=12,
            relief=RIDGE,
            font=("arial", 12, "bold"),
        )

        data_frame_left.place(x=0, y=5, width=900, height=350)

        # Prompt user to choose user type
        user_type = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="User type:  ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        user_type.grid(row=0, column=0, sticky=W)

        txt_user_type = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.user_var,
            width=27,
        )
        txt_user_type.grid(row=0, column=1)

        # Prompt user first name
        student_first_name = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="First name: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        student_first_name.grid(row=1, column=0, sticky=W)

        txt_student_first_name = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.first_name_var,
            width=27,
        )
        txt_student_first_name.grid(row=1, column=1)

        # Prompt user last name
        student_last_name = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Last name: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        student_last_name.grid(row=2, column=0, sticky=W)

        txt_student_last_name = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.last_name_var,
            width=27,
        )
        txt_student_last_name.grid(row=2, column=1)

        # Prompt user course name
        sda_course_name = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Course name: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        sda_course_name.grid(row=3, column=0, sticky=W)

        txt_sda_course_name = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.course_name_var,
            width=27,
        )
        txt_sda_course_name.grid(row=3, column=1)

        # Course Module autofill
        student_module = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Course module: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        student_module.grid(row=0, column=2, sticky=W)

        txt_student_module = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.course_module_var,
            width=27,
        )
        txt_student_module.grid(row=0, column=3)

        # Prompt date of studying
        study_date = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Study date: ",
            font=("arial", 12, "bold"),
            padx=2,
            pady=6,
        )

        study_date.grid(row=1, column=2, sticky=W)
        # date_format = Label(data_frame_left, text="dd/mm/yyyy", bg="mediumpurple4",
        #                     bd=20, font=("arial", 25, "bold"), pady=0)
        # date_format.grid(row=2, column=3, pady=0, sticky="n")

        txt_study_date = Entry(data_frame_left,
                               font=("arial", 12, "bold"),
                               textvariable=self.study_date,
                               width=27)
        txt_study_date.grid(row=1, column=3)

        # ================================ Data Frame Right ==================================

        data_frame_right = LabelFrame(
            frame,
            text="Course modules".upper(),
            bg="mediumpurple4",
            fg="peach puff",
            bd=12,
            relief=RIDGE,
            font=("arial", 12, "bold"),
        )

        data_frame_right.place(x=910, y=5, width=575, height=350)

        self.txt_box = Text(
            data_frame_right,
            font=("arial", 12, "bold"),
            width=36,
            height=15,
            padx=2,
            pady=6,
        )
        self.txt_box.grid(row=0, column=2)

        list_scroll_bar = Scrollbar(data_frame_right)
        list_scroll_bar.grid(row=0, column=1, sticky="ns")

        list_modules = [
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

    # def select_module(event=''):
    #     value = str(list_box.get(list_box.curselection()))
    #     x = value
    #     if ()

        list_box = Listbox(
            data_frame_right, font=("arial", 10, "bold"), width=26, height=18
        )
        list_box.grid(row=0, column=0, padx=4)
        list_scroll_bar.config(command=list_box.yview)

        for item in list_modules:
            list_box.insert(END, item)

        # ================================ Buttons Frame =====================================
        frame_button = Frame(
            self.root, bd=12, relief=RIDGE, padx=20, bg="mediumpurple4"
        )
        frame_button.place(x=0, y=530, width=1550, height=70)

        button_add_data = Button(
            frame_button,
            command=self.add_data,
            text="Add Data",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=0, padx=3, pady=7)

        button_add_data = Button(
            frame_button,
            text="Show Data",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=1, padx=3, pady=7)

        button_add_data = Button(
            frame_button,
            text="Update",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=2, padx=3, pady=7)

        button_add_data = Button(
            frame_button,
            text="Delete",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=3, padx=3, pady=7)

        button_add_data = Button(
            frame_button,
            text="Reset",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=4, padx=3, pady=7)

        button_add_data = Button(
            frame_button,
            text="Exit",
            font=("arial", 12, "bold"),
            width=23,
            bg="peach puff",
            fg="gray37",
        )
        button_add_data.grid(row=0, column=5, padx=3, pady=7)

        # ================================ Information Frame =================================
        frame_details = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="gray52")
        frame_details.place(x=0, y=600, width=1550, height=195)

        table_frame = Frame(frame_details, bd=6, relief=RIDGE, bg="gray52")
        table_frame.place(x=0, y=2, width=1485, height=180)

        xscroll = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.sda_table = ttk.Treeview(
            table_frame,
            columns=(
                "usertype",
                "firstname",
                "lastname",
                "coursename",
                "coursemodule",
                "studydate",
            ),
            xscrollcommand=xscroll.set,
            yscrollcommand=yscroll.set,
        )

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.sda_table.xview)
        yscroll.config(command=self.sda_table.yview)

        self.sda_table.heading("usertype", text="User Type")
        self.sda_table.heading("firstname", text="First Name")
        self.sda_table.heading("lastname", text="Last Name")
        self.sda_table.heading("coursename", text="Course Name")
        self.sda_table.heading("coursemodule", text="Course Module")
        self.sda_table.heading("studydate", text="Study Date")

        self.sda_table["show"] = "headings"
        self.sda_table.pack(fill=BOTH, expand=1)

        self.sda_table.column("usertype", width=100)
        self.sda_table.column("firstname", width=100)
        self.sda_table.column("lastname", width=100)
        self.sda_table.column("coursename", width=100)
        self.sda_table.column("coursemodule", width=100)
        self.sda_table.column("studydate", width=100)

    def add_data(self):
        connection = mysql.connector.Connect(
            host="localhost", username="root", password="newPass", database="practice"
        )
        my_cursor = connection.cursor()
        my_cursor.execute(
            "insert into library values(%s, %s, %s, %s, %s, %s)", (
                                                                    self.user_var.get(),
                                                                    self.first_name_var.get(),
                                                                    self.last_name_var.get(),
                                                                    self.course_name_var.get(),
                                                                    self.course_module_var.get(),
                                                                    self.study_date.get()
                                                                ))

        connection.commit()
        connection.close()

        messagebox.showinfo("Success", "User was inserted successfully")


if __name__ == "__main__":
    root = Tk()
    obj = SDACourseTrackingSystem(root)
    root.mainloop()
