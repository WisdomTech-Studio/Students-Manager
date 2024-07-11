class Student:
    """学生类"""

    def __init__(self,name,gender):
        """初始化学生信息"""
        self.name = name
        self.gender = gender

    def __str__(self) -> str:
        return f'姓名：{self.name} 性别：{self.gender}'
    
    def change_info(self,new_name,new_gender):
        self.name = new_name
        self.gender = new_gender
