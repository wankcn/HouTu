"""
1、自定义People类，并重写其构造（初始化）方法__init__( )，将参数n和a赋值给实例对象的属性
2、自定义该类实例方法speak( )，功能：打印“xxx说: 我xxx岁”
3、自定义Speaker类，并重写其构造（初始化）方法__init__( )，将参数n、c、t赋值给实例对象的属性
4、自定义该类实例方法speak( )，功能：打印“我叫xxx,我是一个xxx,我演讲的主题是 xxx”
5、实例化Student类对象s
6、调用父类的speak( )方法
7、根据效果图进行格式化输出
"""


class People(object):
    # 重写People类的构造方法，并将参数n、a赋值给实例属性name、age
    def __init__(self, n, a):
        self.name = n
        self.age = a

    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print("{0}说: 我{1}岁".format(self.name, self.age))


class Speaker(object):
    # 重写Speaker类的构造方法，并将参数n、c、t赋值给实例属性name、career、topic
    def __init__(self, n, c, t):
        self.name = n
        self.career = c
        self.topic = t

    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print("我叫{0},我是一个{1},我演讲的主题是{2}".format(self.name, self.career, self.topic))


class Student(Speaker, People):
    pass


if __name__ == '__main__':
    s = Student('Jonh', '演说家', 'Python')
    # s对象调用父类的speak( )方法
    s.speak()
    # 格式化打印Student是否为Speaker的子类
    print("Student是否为Speaker的子类:{}".format(issubclass(Student, Speaker)))
    # 格式化打印Student是否为People的子类
    print("Student是否为People的子类:{}".format(issubclass(Student, People)))
