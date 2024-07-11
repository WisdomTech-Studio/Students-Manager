import tkinter as tk
import ttkbootstrap as ttk
import functions as fc
import main


class StudentManagementGUI:
    def __init__(self, root):
        global screen_height, screen_width, root_width, root_height, add_width, add_height
        self.root = root
        self.root.title("学生管理系统")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root_width = 600
        root_height = 500
        add_width = 400
        add_height = 150
        self.root.geometry(
            f"{root_width}x{root_height}+{int((screen_width-root_width)/2)}+{int((screen_height-root_height)/2)}"
        )
        # Student List Label
        self.list_label = ttk.Label(root, text="学生列表：")
        self.list_label.pack()
        # Frame for student list
        self.list_box = tk.Listbox(root)
        self.list_box.pack(pady=10, fill=tk.BOTH, expand=False)

        # Buttons Frame
        self.buttons_frame = ttk.Frame(root)
        self.buttons_frame.pack(pady=10)
        # “添加学生”按钮
        self.add_button = ttk.Button(
            self.buttons_frame, text="添加学生", command=self.add_student
        )
        self.add_button.grid(row=0, column=0, padx=5)

        # “删除学生”按钮
        self.del_button = ttk.Button(
            self.buttons_frame, text="删除学生", command=self.del_student
        )
        self.del_button.grid(row=0, column=1, padx=5)

        # Find Student Button
        # self.find_button = ttk.Button(
        #     self.buttons_frame, text="查找学生", command=self.find_student
        # )
        # self.find_button.grid(row=0, column=2, padx=5)

        # “保存并退出”按钮
        self.save_quit_button = ttk.Button(
            self.root, text="保存并退出", command=self.save_and_quit
        )
        self.save_quit_button.pack()

        # 导入学生数据
        main._load_data()
        fc.share_lists(main.stu_names_list, main.stu_info_list)  # 向模块传递列表
        self.update_student_list()

    def add_student(self):
        def add():
            name = name_var.get()
            gender = gender_var.get()
            fc.add_student(name, gender)
            self.update_student_list()
            window.destroy()

        window = ttk.Toplevel()
        window.title("添加学生")
        window.geometry(
            f"{add_width}x{add_height}+{int((screen_width-add_width)/2)}+{int((screen_height-add_height)/2)}"
        )
        window.resizable(0, 0)
        name_var = ttk.StringVar(window)
        gender_var = ttk.StringVar(window)
        label1 = ttk.Label(window, text="学生姓名：")
        entry1 = ttk.Entry(window, textvariable=name_var)
        button1 = ttk.Button(window, text="添加", command=add)
        c1 = ttk.Checkbutton(
            window, width=4, variable=gender_var, onvalue="男", text="男"
        )
        c2 = ttk.Checkbutton(
            window, width=4, variable=gender_var, onvalue="女", text="女"
        )
        label1.grid(row=1, column=1)
        entry1.grid(row=1, column=2, pady=10)
        c1.place(x=150, y=60)
        c2.place(x=250, y=60)
        button1.grid(row=2, column=1)
        window.mainloop()

    def del_student(self):
        stu_name = main.stu_names_list[self.list_box.index("active")]
        stu_info = main.stu_info_list[self.list_box.index("active")]

        def _del():
            fc.delete_student(stu_info, stu_name)
            window.destroy()
            self.update_student_list()

        window = ttk.Toplevel()
        label = ttk.Label(window, text=f"确定要删除{stu_name}吗？")
        button = ttk.Button(window, text="确定", command=_del)
        label.pack()
        button.pack()
        window.mainloop()

    # def find_student(self):
    #     window = ttk.Toplevel()
    #     str_var = ttk.StringVar(window)
    #     l1 = ttk.Label(window,text="要查找的学生姓名：")
    #     e1 = ttk.Entry(window,textvariable=str_var)
    #     window.mainloop()

    def save_and_quit(self):
        main._save_data()
        self.root.destroy()

    def update_student_list(self):
        self.list_box.delete(0, tk.END)
        if main.stu_info_list:
            for stu_info in main.stu_info_list:
                self.list_box.insert(tk.END, str(stu_info))
        else:
            self.list_box.insert(tk.END, "无学生")

    #     self.list_text.delete(1.0, tk.END)
    #     if main.stu_info_list:
    #         for stu_info in main.stu_info_list:
    #             self.list_text.insert(tk.END, str(stu_info) + "\n")
    #     else:
    #         self.list_text.insert(tk.END, "无学生")


if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = StudentManagementGUI(root)
    root.mainloop()
