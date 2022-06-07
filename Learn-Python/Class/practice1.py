"""
1、自定义一个交通工具类(Vehicle)
2、设置类属性trans_type（固定值为'SUV'）和实例属性速度speed（int 类型，单位为 km/h）、体积size（tuple类型，单位为米。）
3、自定义方法 show_info( )，打印实例的所属类型和速度、体积的值；
4、自定义实例方法如下：
    （1）定义move( )方法，实现打印“我已向前移动了50米”
    （2）定义set_speed(new_speed)方法，设置对应实例的速度为new_speed km/h
    （3）定义get_speed()方法，如果（2）中设置了速度值则打印出来，打印格式为'我的时速为：设置的速度值 km/h'
    （4）定义speed_up()方法，设置每次调用时实例的速度都增加10km/h，并打印“我的速度由xx km/提升到了xx km/h”
    （5）定义speed_down()方法，设置每次调用时实例的速度都降低15km/h，并打印“我的速度由xx km/下降到了xx km/h”
5、自定义方法 transport_identify( )，判断实例是否为Vehicle类型。若是则打印‘类型匹配’，反之则打印‘类型不匹配’
6、初始化实例对象tool_1，并根据上述效果图调用对应方法
"""
from functools import reduce


class Vehicle(object):
    # 自定义Vehicle类属性
    trans_type = "SUV"

    # 自定义实例的初始化方法
    def __init__(self, speed, size):
        self.speed = speed
        self.size = size

    # 自定义实例方法show_info，打印实例的速度和体积
    def show_info(self):
        bulk = reduce(lambda x, y: x * y, self.size)
        return "我所属类型：{0}，速度：{1}km/h，体积：{2:.3f}/m³".format(self.trans_type, self.speed, bulk)

    # 自定义实例方法move,打印“我已向前移动了50米”
    def move(self):
        print("我已向前移动了50米")

    # 自定义实例方法set_speed，设置对应的速度值
    def set_speed(self, new_speed):
        self.speed = new_speed

    # 自定义实例方法get_speed，打印当前的速度值
    def get_speed(self):
        print("当前速度：{}km/h".format(self.speed))

    # 自定义实例方法speed_up，实现对实例的加速
    def speed_up(self):
        self.speed += 10
        print("我的速度由{}km/h提升到了{}km/h".format(self.speed - 10, self.speed))

    # 自定义实例方法speed_down，实现对实例的减速
    def speed_down(self):
        self.speed -= 15
        print("我的速度由{}km/h下降到了{}km/h".format(self.speed + 15, self.speed))

    # 自定义实例方法transport_identify，实现对实例所属类型的判断
    def transport_identify(self, class_name):
        if isinstance(class_name, Vehicle) is True:
            print("类型匹配")
        else:
            print("类型不匹配")


if __name__ == "__main__":
    tool_1 = Vehicle(20, (3, 1.9, 1.75))

    # 调用实例方法 打印实例的速度和体积
    info = tool_1.show_info()
    print(info)

    # 调用实例方法 实现实例的前移
    tool_1.move()
    tool_1.set_speed(40)

    # 调用实例方法 打印当前速度
    tool_1.get_speed()

    # 调用实例方法 对实例进行加速
    tool_1.speed_up()

    # 调用实例方法 对实例进行减速
    tool_1.speed_down()

    # 调用实例方法 判断当前实例的类型
    tool_1.transport_identify(tool_1)
