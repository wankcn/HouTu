import random
import time
from multiprocessing import current_process, Pool


def run(file_name, num):
    """
    进程执行的业务逻辑
    往文件中写入数据
    :param file_name:  str 文件名称
    :param num:  int 写入的数字
    :return:  写入的结果
    """
    with open(file_name, "a+", encoding="UTF-8") as f:
        # 当前的进程
        now_process = current_process()
        # 写入的内容
        content = "进程的名称{0}\n进程ID:{1}\n写入的数字:{2}\n".format(
            now_process.name,
            now_process.pid,
            num
        )
        f.write(content)
        # 写完之后随机休息1-3秒
        time.sleep(random.randint(1, 3))
        print(content)
    return "OK"


if __name__ == '__main__':
    file_name = "test_pool.txt"
    # import os
    # os.cpu_count()
    # 不指定大小,根据cpu的大小指定
    # 指定进程池大小
    pool = Pool(2)
    # for i in range(20):
    #     # 同步添加任务 拿到结果之后在执行
    #     result = pool.apply(run, args=(file_name, i))
    #     print("{0}{1}".format(i, result))
    # # 关闭进程池
    # pool.close()
    # pool.join()

    result_list = []
    # 异步 马上返回一个取到结果的地址，循环完之后在执行
    for i in range(20):
        # 异步添加任务
        result = pool.apply_async(run, args=(file_name, i))
        result_list.append(result)

    # 关闭进程池
    pool.close()
    pool.join()
    # 查看异步执行的所有结果
    # for i in result_list:
    #     print(i.get())
    # 查看异步执行的第一个结果
    print(result_list[0].get())
