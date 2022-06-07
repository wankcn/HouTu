"""
    1、自定义Point类，并重写其构造（初始化）方法__init__( )，将参数x和y赋值给实例对象的属性
    2、自定义该类实例方法string( )，功能：打印“{X：xx, Y：xx}”
    3、自定义Circle类，继承自Point类，并重写其构造（初始化）方法__init__( )，x、y参数通过调
用父类的构造函数进行赋值，radius通过子类重写的 __init__( )进行赋值。
    4、自定义该类实例方法string( )，功能：打印“该图形初始化点为：{X：xx, Y：xx}; {半径为：xx}”
    5、自定义Size类，并重写其构造（初始化）方法__init__( )，将参数width和height赋值给实例对象的属性
    6、自定义该类实例方法string( )，功能：打印“{Width：xx, Height：xx}”
    7、自定义Rectangle类，继承自Point类和Size类，并重写其构造（初始化）方法__init__( )，x、y、width、height
4个参数全部通过调用父类的构造函数进行赋值
    8、自定义该类实例方法string( )，功能：打印“该图形初始化点为：{X：xx, Y：xx}; 长宽分别为：{Width：xx, Height：xx}
    9、初始化Circle类的对象c，并调用其格式化输出函数string( )
    10、初始化Rectangle类的对象r1、r2,并分别调用其格式化输出函数string( )
"""


class Point(object):
    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 自定义Point类对象的格式化输出函数(string())
    def string(self):
        print("x:{},y:{}".format(self.x, self.y))


class Circle(Point):
    # 自定义Circle类的构造(初始化)方法
    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    # 自定义Circle类对象的格式化输出函数(string())
    def string(self):
        print("该图形初始化点为：X:{}, Y:{}; 半径为:{}".format(self.x, self.y, self.radius))


class Size(object):
    # 自定义Size类的构造(初始化)方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 自定义Size类对象的格式化输出函数(string())
    def string(self):
        print("width:{},height:{}".format(self.width, self.height))


class Rectangle(Point, Size):
    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    # 自定义Rectangle类对象的格式化输出函数(string())
    def string(self):
        print("该图形初始化点为：X:{},Y:{};长宽分别为：Width:{},Height:{}".format(self.x, self.y, self.width, self.height))


if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    circle = Circle(5, 5, 8)
    circle.string()
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    r1 = Rectangle(15, 15, 15, 15)
    r1.string()
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    r2 = Rectangle(40, 40, 11, 14)
    r2.string()
