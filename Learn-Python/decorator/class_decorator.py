"""
类装饰器，为写好的类进行功能和属性的扩充
"""


def f(self):
    print("{}要吃东西".format(self.name))


def eat(cls):
    """吃东西的装饰器"""
    # cls.eat = lambda self: print("{}要吃东西".format(self.name))
    # 上一行用lambda表达式简单实现复杂逻辑
    cls.eat = f
    return cls


@eat
class Cat:
    """猫类"""

    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    cat = Cat('可乐')
    cat.eat()
