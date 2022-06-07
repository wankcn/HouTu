class Cat(object):
    tag = "猫科动物"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def breath():
        """静态方法括号内不需要表示实例"""
        print("猫呼吸")

    @classmethod
    def show_info(cls,name):
        print("类的属性{}，实例的属性{}".format(cls.tag, name))

    def show_info2(self):
        print("类的属性{}，实例的属性{}".format(self.tag, self.name))


if __name__ == '__main__':
    # 静态方法可以通过类调用也可以通过实例调用
    Cat.breath()
    cat = Cat('可乐')
    cat.breath()
    cat.show_info("cole")
