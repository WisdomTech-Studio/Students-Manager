"""管理系统需要使用到的函数"""

from student import Student

# 获得主程序的列表供函数使用
stu_names_list, stu_info_list = [], []


def share_lists(names_list, info_list):
    """接受主程序传递的列表"""
    global stu_names_list, stu_info_list
    stu_names_list = names_list
    stu_info_list = info_list


# 功能函数
def return_student_info(name):
    """根据名字返回学生信息"""
    for student in stu_info_list:
        if student.name == name:
            return student


def add_student(name, gender):
    """添加学生到列表"""
    new_student_info = Student(name, gender)
    stu_info_list.append(new_student_info)
    stu_names_list.append(name)
    print("添加成功！")


def delete_student(info, name):
    """根据名字删除列表中的学生"""
    stu_info_list.remove(info)
    stu_names_list.remove(name)
