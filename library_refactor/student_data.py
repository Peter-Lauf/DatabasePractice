import tkinter as tk


class StudentData:
    def __init__(self, root):
        self._user_var = tk.StringVar(root)
        self._first_name = tk.StringVar(root)
        self._last_name = tk.StringVar(root)
        self._study_hours = tk.StringVar(root)
        self._study_date = tk.StringVar(root)
        self._course_name_var = tk.StringVar(root)
        self._course_module_var = tk.StringVar(root)

    @property
    def user_var(self):
        return self._user_var

    @user_var.setter
    def user_var(self, value):
        self._user_var = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def study_hours(self):
        return self._study_hours

    @study_hours.setter
    def study_hours(self, value):
        self._study_hours = value

    @property
    def study_date(self):
        return self._study_date

    @study_date.setter
    def study_date(self, value):
        self._study_date = value

    @property
    def course_name_var(self):
        return self._course_name_var

    @course_name_var.setter
    def course_name_var(self, value):
        self._course_name_var = value

    @property
    def course_module_var(self):
        return self._course_module_var

    @course_module_var.setter
    def course_module_var(self, value):
        self._course_module_var = value
