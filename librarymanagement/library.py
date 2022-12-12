from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime

# Pull request test ///

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
        self.study_date_var = StringVar()
        self.study_hours_var = StringVar()

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
            font=("arial", 12, "bold"),
            text="User Type",
            padx=10,
            pady=15,
        )
        user_type.grid(row=0, column=0, sticky=W)

        com_user_type = ttk.Combobox(
            data_frame_left,
            textvariable=self.user_var,
            state="readonly",
            font=("arial", 12, "bold"),
            width=25,
        )
        com_user_type["value"] = ("Student", "Admin", "Trainer")
        com_user_type.current(0)
        com_user_type.grid(row=0, column=1)

        # Prompt user first name
        student_first_name = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="First name: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
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
            padx=10,
            pady=15,
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
            padx=10,
            pady=15,
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
        course_module = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Course module: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        course_module.grid(row=0, column=2, sticky=W)

        txt_course_module = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.course_module_var,
            width=27,
        )
        txt_course_module.grid(row=0, column=3)

        # Date of studying autofill
        study_date = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Study date: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        study_date.grid(row=1, column=2, sticky=W)
        txt_study_date = Entry(data_frame_left,
                               font=("arial", 12, "bold"),
                               textvariable=self.study_date_var,
                               width=27)
        txt_study_date.grid(row=1, column=3)

        # Hours studied
        hours_studied = Label(
            data_frame_left,
            bg="mediumpurple4",
            text="Hours Studied: ",
            font=("arial", 12, "bold"),
            padx=10,
            pady=15,
        )

        hours_studied.grid(row=2, column=2, sticky=W)

        txt_hours_studied = Entry(
            data_frame_left,
            font=("arial", 12, "bold"),
            textvariable=self.study_hours_var,
            width=27,
        )
        txt_hours_studied.grid(row=2, column=3)

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

        def select_module(event=''):
            value = str(list_box.get(list_box.curselection()))
            x = value
            if x == "Python Developer - introduction":
                d1 = datetime.date.today()
                self.course_module_var.set("Python Developer - introduction")
                self.study_date_var.set(d1)

            elif x == "Python - the basics":
                d1 = datetime.date.today()
                self.course_module_var.set("Python - the basics")
                self.study_date_var.set(d1)

            elif x == "Git system":
                d1 = datetime.date.today()
                self.course_module_var.set("Git system")
                self.study_date_var.set(d1)

            elif x == "Python - technology":
                d1 = datetime.date.today()
                self.course_module_var.set("Python - technology")
                self.study_date_var.set(d1)

            elif x == "Software testing and TDD":
                d1 = datetime.date.today()
                self.course_module_var.set("Software testing and TDD")
                self.study_date_var.set(d1)

            elif x == "Python - intermediate":
                d1 = datetime.date.today()
                self.course_module_var.set("Python - intermediate")
                self.study_date_var.set(d1)

            elif x == "Algorithms and data structures":
                d1 = datetime.date.today()
                self.course_module_var.set("Algorithms and data structures")
                self.study_date_var.set(d1)

            elif x == "Design patterns and good practices":
                d1 = datetime.date.today()
                self.course_module_var.set("Design patterns and good practices")
                self.study_date_var.set(d1)

            elif x == "SQL databases":
                d1 = datetime.date.today()
                self.course_module_var.set("SQL databases")
                self.study_date_var.set(d1)

            elif x == "Databases - programming":
                d1 = datetime.date.today()
                self.course_module_var.set("Databases - programming")
                self.study_date_var.set(d1)

            elif x == "HTTP basics":
                d1 = datetime.date.today()
                self.course_module_var.set("HTTP basics")
                self.study_date_var.set(d1)

            elif x == "HTML,CSS,JavaScript":
                d1 = datetime.date.today()
                self.course_module_var.set("HTML,CSS,JavaScript")
                self.study_date_var.set(d1)

            elif x == "Backend technologies":
                d1 = datetime.date.today()
                self.course_module_var.set("Backend technologies")
                self.study_date_var.set(d1)

            elif x == "Final project":
                d1 = datetime.date.today()
                self.course_module_var.set("Final project")
                self.study_date_var.set(d1)

        list_box = Listbox(
            data_frame_right, font=("arial", 10, "bold"), width=26, height=18
        )
        list_box.bind("<<ListboxSelect>>", select_module)
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
                "studyhours"
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

        self.fetch_data()

    def add_data(self):
        connection = mysql.connector.Connect(
            host="localhost", username="root", password="newPass", database="practice"
        )
        my_cursor = connection.cursor()
        my_cursor.execute(
            "insert into library values(%s, %s, %s, %s, %s, %s, %s)", (
                                                                    self.user_var.get(),
                                                                    self.first_name_var.get(),
                                                                    self.last_name_var.get(),
                                                                    self.course_name_var.get(),
                                                                    self.course_module_var.get(),
                                                                    self.study_date_var.get(),
                                                                    self.study_hours_var.get()
                                                                ))

        connection.commit()
        self.fetch_data()
        connection.close()

        messagebox.showinfo("Success", "User was inserted successfully")

    def fetch_data(self):
        connection = mysql.connector.connect(host="localhost", username="root", password="newPass", database="practice")
        my_cursor = connection.cursor()
        my_cursor.execute("select * from library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.sda_table.delete(*self.sda_table.get_children())
            for i in rows:
                self.sda_table.insert("", END, values=i)
            connection.commit()
        connection.close()

    def get_cursor(self):
        cursor_row = self.sda_table.focus()
        content = self.sda_table.item(cursor_row)
        row = content['values']

        self.user_var.set(row[0])


if __name__ == "__main__":
    root = Tk()
    obj = SDACourseTrackingSystem(root)
    root.mainloop()
