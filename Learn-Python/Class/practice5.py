"""
1、自定义Car类，并重写其构造（初始化）方法__init__( )，将参数l，w，h，brand赋值给实例对象的属性L，W，H，brand。设置类属性
description，以列表形式初始化值为：'大众'，'丰田'，'广本'，'沃尔沃'， '凯迪拉克'
2、自定义该类实例方法modify_des ( )。功能：判断类属性description是否存在，若存在，直接返回；反之，返回“请输入您的车辆描述”
3、自定义静态方法basic_parameters( )。功能：打印‘已完成车辆基本参数信息的录入！’
4、自定义类方法upkeep( )，并接收参数desc。功能：判断参数desc是否在类属性desc之中，若条件成立则打印“根据汽车保养的相关经验，
xx品牌的车应于5000km/次的频率进行专业性保养”；反之则打印“非常抱歉！xx品牌不在我们的保养范围内

5、实例化Car类对象car_1，并调用实例方法basic_parameters()
6、运用if-else结构，调用实例（car_1）方法modify_des( )作为if语句的判断条件，若成立则调用实例的upkeep( )方法，并将实例car_1
的brand属性传递给参数desc；反之则打印：'请正确填写相关的车辆信息
7、实例化Car类对象car_2，并调用实例方法basic_parameters()
8、运用if-else结构，调用实例（car_2）方法modify_des( )作为if语句的判断条件，若成立则调用实例的upkeep( )方法，并将实例car_2
的brand属性传递给参数desc；反之则打印：'请正确填写相关的车辆信息'
"""


class Car(object):
    description = ['大众', '丰田', '广本', '沃尔沃', '凯迪拉克']

    def __init__(self, l, w, h, brand):
        self.L = l
        self.W = w
        self.H = h
        self.brand = brand

    def modify_des(self):
        # hasattr()函数用于判断对象是否包含对应的属性。
        if hasattr(self, 'description'):
            return True
        else:
            print("请输入您的车辆描述")

    @staticmethod
    def basic_parameters():
        print("已完成车辆基本参数信息的录入！")

    @classmethod
    def upkeep(cls, desc):
        if desc in cls.description:
            print("根据汽车保养的相关经验，{0}品牌的车应于5000km/次的频率进行专业性保养".format(desc))
        else:
            print("非常抱歉！{}品牌不在我们的保养范围内".format(desc))


if __name__ == '__main__':
    car_1 = Car(4.2, 1.8, 1.5, '大众')
    Car.basic_parameters()
    if car_1.modify_des():
        Car.upkeep(car_1.brand)
    else:
        print("请正确填写相关的车辆信息")

    car_2 = Car(4.2, 1.8, 1.5, '保时捷')
    Car.basic_parameters()
    if car_2.modify_des():
        Car.upkeep(car_2.brand)
    else:
        print("请正确填写相关的车辆信息")
