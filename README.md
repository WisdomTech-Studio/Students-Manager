# Students Manager
### <font color=FFA500>最新版本：</font>[![releases](https://badgen.net/github/release/WisdomTech-Studio/Student-Manager)](https://github.com/WisdomTech-Studio/Student-Manager/releases)

## <font color=1E90FF>前言</font>  
这是一个极其简单且简陋的Python项目，是工作室成员用来练习Python的。  
**<font color=8B0000>因此不要将此程序用于管理学生！</font>**<font color=A9A9A9>（~~也没人看的上~~）</font>  
开发者们都是**新手**，如果有任何方面的意见或建议请向我们提出！ 
出于学习目的，部分功能使用了较复杂或者特别的方式实现，当然如果有简化的建议也可以与我们分享！
## <font color=1E90FF>需要的第三方库</font>    
**gui.py**需要第三方库<u>[ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/zh/gettingstarted/installation/)</u>。  

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<font color=8470FF>**通过PyPI安装**</font>  
```
python -m pip install ttkbootstrap
```  
&emsp;&emsp;&emsp;&emsp;&emsp;<font color=8470FF>**通过PyPI清华镜像源安装**</font>  
```
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple ttkbootstrap
```  
## <font color=1E90FF>运行</font>  
项目其中有两个.py文件，分别是**main.py**和**gui.py**，二者运行其中一个皆可。  它们的区别在于： 
* <font color=FFA500>**main.py是在终端上显示输出结果并与用户交互；**</font>  
* <font color=FFA500>**而gui.py则会显示独立窗口与用户交互。**</font>  

因此我们建议运行**gui.py**，体验更佳  
### **<font color=8B0000><u>！！！注意！！！由于main.py中使用了“f字符串”，故仅适用于Python3.6及以上的Python版本运行！</u></font>**
## <font color=1E90FF>代码简述</font>  

### <font color=8470FF>**main.py**</font>  
**主要开发者：** <u>[Billts-noo](https://github.com/Billts-noo)</u>  
**运行原理（单独运行main.py时）：**  
1. 使用`print()`函数输出指定菜单，并标注各功能所对应的数字，用户通过在终端输入数字使用对应功能；  

2. 在“添加学生”（自定义函数`_add_student()`）中，用户将会依次输入学生信息，我们创建一个学生实例来存储单个学生的信息，再将实例存储到列表**stu_info_list**中。我们还会将学生的姓名单独存储到列表**stu_names_list**中，便于后续的查找工作。下面是部分代码；
```Python
def add_student(name, gender):
    """添加学生到列表"""
    new_student_info = Student(name, gender)
    stu_info_list.append(new_student_info)
    stu_names_list.append(name)
    print("添加成功！")
```
3. 在删除、查找以及后续会上线的更改功能中，我们都在对学生信息操作前遍历一次列表**stu_names_list**比对被操作的学生是否存在，再根据结果执行对应操作；  

4. 我们还使用pickle模块实现了**数据存储**的功能，**students info.json**和**students names.json**分别存储两个列表**stu_info_list**和**stu_names_list**，第一次保存时会自动创建。**<font color=8B0000><u>用户需要执行在主菜单的操作“保存并退出”才能正常保存数据！</u></font>**
5. **functions.py**将管理系统要用到的函数独立出来，为了函数能正常调用上述的两个列表，我们使用自定义函数`share_lists()`实现两个文件之间的列表传输。<font color=A9A9A9>*（想法来自于工作室成员xnz233）*</font>  
***  
### <font color=8470FF>**gui.py**</font>
**主要开发者：** <u>[xnz233](https://github.com/xnz233/)</u>  
**运行原理（单独运行gui.py时）：**  
1. 使用`tkinter`库进行窗口的绘制，并与主程序共用一部分函数；自定义了窗口的类，将图形界面部分的定义单独抽离出来，使得代码逻辑更加清晰，下面是部分代码：
```Python
class StudentManagementGUI:
def __init__(self, root):
global screen_height, screen_width, root_width, root_height
self.root = root
self.root.title("学生管理系统")
screen_width = root.winfo_screenwidth() # 获取屏幕宽度
screen_height = root.winfo_screenheight() # 获取屏幕高度
root_width = 600
root_height = 500

self.root.geometry(

f"{root_width}x{root_height}+{int((screen_width-root_width)/2)}+{int((screen_height-root_height)/2)}" # 计算窗口位置，使其绘制在屏幕中央
)
# more...
```

2. 使用<u>[ttkbootstrap](https://ttkbootstrap.readthedocs.io/en/latest/zh/gettingstarted/installation/)</u>库进行窗口美化，使图形化窗口更美观。
