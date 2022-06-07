class Cat():
    """宠物猫类"""

    def __init__(self, name, age):
        """
        构造方法
        :param name: 名称
        :param age: 信息
        """
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            print("必须是整数")
            return 0
        if value < 0 or value > 100:
            print("只能在1-100之间")
            return 0
        self.__age = value

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


if __name__ == '__main__':
    cole = Cat("可乐", 2)
    info = cole.show_info
    print(info)
    cole.age = 1111
    info = cole.show_info
    print(info)
