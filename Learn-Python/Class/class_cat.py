class Cat(object):
    """
    猫科动物类
    """
    tag = "我是家猫"  # 类的属性

    def __init__(self, name, age, sex=None):  # 默认可以不传，必须写在最后面
        # 实例化后的属性
        self.name = name
        self.__age = age  # 私有属性
        self.sex = sex

    def set_age(self, age):
        """
        改变猫的年龄
        :param age: int 年龄
        """
        self.__age = age
        # return self.__age

    def eat(self):
        """吃"""
        print("猫爱吃鱼")

    def catch(self):
        """捉老鼠"""
        print("猫能捉老鼠")

    def call(self):
        """叫"""
        print("猫喵喵叫")

    def show_info(self):
        """
        显示猫的信息
        :return:
        """
        return "我叫：{0}, 性别：{1}, 今年{2}岁".format(self.name, self.sex, self.__age)


class Tiger(object):
    pass


if __name__ == '__main__':
    # 实例化我家的可乐
    cole = Cat("可乐", 1)
    cole.eat()
    info = cole.show_info()
    print(info)
    # cole.__age  # 无法访问私有变量
    print("---------------------")
    cole.name = "橙汁"  # 更改名字
    cole.sex = "公"
    cole.__age = 2  # 无法更改私有
    info2 = cole.show_info()
    print(info2)
    print("---------------------")
    cole.set_age(2)
    info3 = cole.show_info()
    print(info3)

    # 实例化你家的小黑
    cat_black = Cat("小黑", 2, "母")
    info = cat_black.show_info()
    print(info)

    # 类的实例判断 返回True
    print(isinstance(cole, Cat))
    print(isinstance(cat_black, Cat))
    print("--------")
    print(isinstance(cole, Tiger))
    print(isinstance(cat_black, Tiger))
