import functions as fc
from student import Student
import os
import pickle

# 变量名缩写：
# stu(s) = student(s)
# info = information
stu_names_list, stu_info_list = [], []
active = True
input_message = "输入数字以执行对应操作："
stu_info_data = "students info.json"
stu_names_data = "students names.json"


def _load_data():
    global stu_info_list, stu_names_list
    if os.path.exists(stu_info_data):  # 判断数据文件是否存在
        with open(stu_info_data, "rb") as info_data:
            stu_info_list = pickle.load(info_data)  # 如果存在则导入数据
        print("已找到文件students info.json!")
    else:
        print(
            """找不到文件students info.json！
    不过这不影响系统的正常运行，系统退出后会自动生成"""
        )

    if os.path.exists(stu_names_data):
        with open(stu_names_data, "rb") as name_data:
            stu_names_list = pickle.load(name_data)
        print("已找到文件students names.json!")
    else:
        print(
            """找不到文件students names.json！
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
            if new_stu_gender == "0":
                fc.add_student(new_stu_name, "男")
                break
            elif new_stu_gender == "1":
                fc.add_student(new_stu_name, "女")
                break
            else:
                print("别瞎jb乱搞")
    else:
        print("别瞎jb乱搞")


def _del_student():
    while True:
        del_stu_name = input("请输入要删除的学生的姓名：")
        del_stu_info = fc.return_student_info(del_stu_name)
        if del_stu_info:
            fc.delete_student(del_stu_info, del_stu_name)
            print(f"学生{del_stu_name}已被删除！")
            break
        elif not del_stu_name:
            print("已退出！")
            break
        else:
            print(f"未找到学生{del_stu_name}！请检查输入是否正确")


def _find_student():
    while True:
        find_stu_name = input("请输入要查找的学生的姓名：（按回车退出）")
        find_stu_info = fc.return_student_info(find_stu_name)
        if find_stu_info:
            print("\n查询结果如下:")
            print(find_stu_info)
            way1 = input(f'''
0 修改信息  1 退出
{input_message}
''')
            if way1 == '0':
                changed_name,changed_gender = input('请依次输入修改后的姓名、性别：\n').split()
                find_stu_info.change_info(changed_name,changed_gender)
                print('修改成功！')
            if way1 == '1':
                None
            _show_list()
            break
        elif not find_stu_name:
            print("已退出！")
            break
        else:
            print(f"未找到学生{find_stu_name}！请检查输入是否正确")


def _save_data():
    pickle.dump(stu_info_list, file=open(stu_info_data, "wb"))
    pickle.dump(stu_names_list, open(stu_names_data, "wb"))
    print("数据保存成功！")

if __name__ == "__main__":
    _load_data()
    fc.share_lists(stu_names_list, stu_info_list)  # 向模块传递列表

    # 简介
    print(
        """
——————学生管理系统Beta——————
       By Billts_noo"""
    )

    # 主程序
    while active:
        main_way = input(
            f"""
——————————主菜单——————————
      0 显示学生列表
      1 保存并退出
{input_message}"""
        )

        # 主菜单
        # 显示学生列表
        if main_way == "0":
            _show_list()
            while True:
                way = input(
                    f"""
——学生列表菜单——
   0 添加学生
   1 删除学生
   2 查找学生
任意输入 回到主菜单
{input_message}"""
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
