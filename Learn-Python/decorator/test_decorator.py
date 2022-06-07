def hello():
    """简单功能模拟"""
    print("hello world")


def test():
    print("test")


def hello_wrapper():
    print("Star ...")
    hello()
    print("End!")


if __name__ == '__main__':
    # hello()
    hello_wrapper()
