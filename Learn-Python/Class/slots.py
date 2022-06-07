class Cat():
    """宠物猫类"""

    """使用slots后不允许添加新的实例"""
    __slots__ = ('name', '__age')  # 设置只能用slots里的属性

    def __init__(self, name, age):
        """
        构造方法
        :param name: 名称
        :param age: 信息
        """
        self.name = name
        self.__age = age

    # 描述符 打印方法不写括号，把方法当作属性
    @property
    def show_info(self):
        """
        显示猫的信息
        :return:
        """
        return "姓名：{},年龄：{}".format(self.name, self.__age)

    def __str__(self):
        """ 打印类的描述， 类似java中的toString"""
        return self.show_info()


class HuaCat(Cat):
    """中华田园猫"""
    __slots__ = ('color',)  # 一个数据的元组，逗号结束
    pass


def eat():
    print("猫爱吃鱼")


if __name__ == '__main__':
    cat_white = HuaCat("小白", 3)
    info2 = cat_white.show_info
    print(info2)
    cat_white.color = "白色"
    print(cat_white.color)
    cat_white.name = '白白'
    print(cat_white.name)

    """
        父类指定了solts，那么父类不能添加新的属性。
        对继承的子类不受影响，子类继续可以添加新的属性
        如果子类也添加的slots，那么子类不允许修改的范围是父类加子类的范围
    """
    # 不可以执行
    # cat_white.aa = "a"
    # print(cat_white.aa)
