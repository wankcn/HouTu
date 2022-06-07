"""
    猫科动物的细化
    Tiger  Panda  Cat
"""


class ProtextedMixin(object):
    # mixin是一种设计模式，用于多个子类用，一个扩展
    """受保护的类，用于类的多继承"""

    def protected(self):
        print("我是受省级保护的动物")


class CountryProtextedMixin(object):
    # mixin是一种设计模式，用于多个子类用，一个扩展
    """受保护的类，用于类的多继承"""

    def protected(self):
        print("我是受国家保护的动物")


class BaseCat(object):
    """
    猫科动物的基础类
    """
    tag = "猫科动物"

    # 都有名称和年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        """猫科动物吃东西"""
        print("动物都需要吃东西")

    def eat2(self):
        print("我是爷爷类")


class Tiger(BaseCat, ProtextedMixin):
    """老虎类"""

    def eat(self):
        super(Tiger, self).eat()
        print("老虎还喜欢吃大肉")


class Panda(BaseCat, ProtextedMixin, CountryProtextedMixin):
    """熊猫类"""
    pass


class PetCat(BaseCat):
    """宠物猫类"""

    def eat(self):
        super(PetCat, self).eat()
        print("宠物猫还喜欢吃猫粮")


class HuaCat(PetCat):
    """中华田园猫类"""

    def eat(self):
        super(HuaCat, self).eat()
        print("中华田园猫还喜欢吃猫粮")


class EnCat(PetCat):
    """英国短毛猫"""

    def eat(self):
        print("英短啥都吃")


if __name__ == '__main__':
    # 实例化中华田园猫
    cole_cat = HuaCat("可乐", 2)
    cole_cat.eat()
    print("-----------------------")
    # 实例化英短
    black = EnCat("小黑", 1)
    black.eat()
    black.eat2()  # 找不到会一层一层往上找

    # 子类的判断
    print(issubclass(EnCat, BaseCat))  # 子类的子类
    print(issubclass(EnCat, HuaCat))  # 兄弟
    print(issubclass(EnCat, PetCat))  # 子类

    print("------------------------")
    panda = Panda("卧龙大熊猫", 1)
    panda.eat()
    panda.protected()  # 继承两个类都有proctected方法，调继承的第一个
    print("---验证子类信息---")
    print(issubclass(Panda, ProtextedMixin))
