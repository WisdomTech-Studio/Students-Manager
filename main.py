import functions as fc
from student import Student
import os
import pickle

# 变量名缩写：
# stu(s) = student(s)
# info = information
stu_names_list, stu_info_list = [], []
active = True
input_message = "输入数字以执行对应操作:"
stu_info_filename = "students info.json"
stu_names_filename = "students names.json"


def _load_data():
    global stu_names_list,stu_info_list
    lst = [stu_names_list,stu_info_list]
    for i,filename in enumerate([stu_names_filename, stu_info_filename]):
        if os.path.exists(filename):  # 判断数据文件是否存在
            with open(filename, "rb") as f:
                lst[i].extend(pickle.load(f))
            print(f"已找到文件{filename}!")
        else:
            print(
                f"""找不到文件{filename}！
        不过这不影响系统的正常运行，系统退出后会自动生成"""
            )


def _show_list():
    if stu_info_list:
        print(f"\n学生列表共 {len(stu_info_list)} 名学生：")
        for stu_info in stu_info_list:
            print(stu_info)
    else:
        print("\n无学生")


def _add_student():
    new_stu_name = input("请输入要添加的学生的姓名：")
    if new_stu_name:
        while True:
            new_stu_gender = input("0 男\n1 女\n请选择新学生的性别：")
            if new_stu_gender == '0' or new_stu_gender == '1':
                fc.add_student(new_stu_name, fc.translate_gender(new_stu_gender))
                break
            else:
                print("别瞎搞awa")
    else:
        print("别瞎搞awa")


def _del_student():
    while True:
        del_stu_name = input("请输入要删除的学生的姓名：（按回车退出）")
        del_stu_info = fc.return_student_info(del_stu_name)
        if del_stu_info:
            fc.delete_student(del_stu_info, del_stu_name)
            print(f"学生{del_stu_name}已被删除！")
            break
        elif not del_stu_name: # 未输入要删除的学生的姓名则退出
            print("已退出！")
            break
        else:
            print(f"未找到学生{del_stu_name}！请检查输入是否正确")


def __change_student(stu_name,stu_info):
    way1 = input(f'\n0 修改信息  （按回车退出）\n{input_message}')
    while True:
        if way1 == '0':
            try:
                changed_name, changed_gender = input(
                    '请依次输入修改后的姓名、性别（输入0或1）：（用空格隔开）\n').split()
            except ValueError:
                print(f"非法输入！请检查输入是否正确")
            else:
                if changed_gender == '0' or changed_gender == '1':
                    stu_info.change_info(changed_name, fc.translate_gender(changed_gender))
                    stu_names_list.remove(stu_name)
                    stu_names_list.append(changed_name)
                    break
                else:
                    print(f"非法输入！请检查输入是否正确")
        else:
            print("已退出！")
            break


def _find_student():
    while True:
        find_stu_name = input("请输入要查找的学生的姓名：（按回车退出）")
        find_stu_info = fc.return_student_info(find_stu_name)
        if find_stu_info:
            print("\n查询结果如下:")
            print(find_stu_info)
            __change_student(find_stu_name,find_stu_info)
            _show_list()
            break
        elif not find_stu_name:
            print("已退出！")
            break
        else:
            print(f"未找到学生{find_stu_name}！请检查输入是否正确")


def _save_data():
    pickle.dump(stu_info_list, file=open(stu_info_filename, "wb"))
    pickle.dump(stu_names_list, open(stu_names_filename, "wb"))
    print("数据保存成功！")


if __name__ == "__main__":
    _load_data()
    fc.share_lists(stu_names_list, stu_info_list)  # 向模块传递列表

    # 简介
    print(
        """
——————[Students Manager v0.0.2-beta]——————
           By WisdomTech Studio
——————————————————————————————————————————"""
    )

    # 主程序
    while active:
        main_way = input(
            f"""
—————————[主菜单]—————————
|     0 显示学生列表     |
|      1 保存并退出      |
| {input_message}|
——————————————————————————\n"""
        )

        # 主菜单
        # 显示学生列表
        if main_way == "0":
            _show_list()
            while True:
                way = input(
                    f"""
———————[学生列表菜单]———————
|        0 添加学生        |
|        1 删除学生        |
|   2 查找或修改学生信息   |
|    任意输入 回到主菜单   |
|  {input_message} |
————————————————————————————\n"""
                )

                # 学生列表菜单
                if way == "0":
                    _add_student()

                if way == "1":
                    _del_student()

                if way == "2":
                    _find_student()

                else:
                    break
        # 退出
        if main_way == "1":
            # 保存数据
            _save_data()
            active = False
