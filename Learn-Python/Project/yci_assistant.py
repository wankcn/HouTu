# 生活小助理
import random


def print_info():
    print("======================")
    print("\t1-双色球随机选号")
    print("\t2-号码百事通")
    print("\t3-明日天气预报")
    print("\t0-结束程序")
    print("======================")


def union_lotto(num):
    """
    生成双色球的方法
    :param num: 需要购买的注数
    """
    for i in range(0, int(num)):
        for x in range(0, 6):
            red = random.randint(1, 33)
            print(red, end=" ")
        blue = random.randint(1, 16)
        print(blue)


def find_phone(keyword):
    """
    号码百事通
    :param keyword: 要查找的信息
    """
    phone_str = "匪警[110],火警[119],急救中心[120]," \
                "道路交通事故报警[122],水上求救专用电话[12395]," \
                "天气预报[12121],报时服务[12117],森林火警[12119]," \
                "电力服务[95598],红十字会急救台[999]," \
                "公安短信报警[12110],通用紧急求救[112]," \
                "信产部IP/网站备案[010-66411166]"
    phone_list = phone_str.split(",")
    # print(list)
    for p in phone_list:
        if p.find(keyword) != -1:
            print(p)


def find_weather(city):
    """
    天气预报功能
    :return:
    """
    # 数据初始化解析
    weather_str = "北京,2019年1月12日,多云,8°C,-4°C,南风3级~" \
                  "上海,2019年1月12日,小雨,9°C,6°C,北风2级~" \
                  "广州,2019年1月12日,阵雨转多云,22°C,15°C,持续无风向微风"
    # print(weather_str)
    weather_list = weather_str.split("~")
    # print(weather_list)
    weather_dict = {}
    for i in range(0, len(weather_list)):
        n = weather_list[i].split(",")
        # print(n)
        weather_info = {"city": n[0], "date": n[1], "weather": n[2], "max": n[3], "min": n[4], "wind": n[5]}
        weather_dict[weather_info["city"]] = weather_info
    # print(weather_dict)
    if city in weather_dict:
        return weather_dict.get(city)
    else:
        return {}


while True:
    print_info()
    c = input("请输入功能编号：")
    if c == "1":
        n = input("请输入需要买几注：")
        union_lotto(n)
        print("\n")
    elif c == "2":
        n = input("您要查询的机构或者电话号码：")
        find_phone(n)
        print("\n")
    elif c == "3":
        n = input("请输入您要查找城市的天气：")
        info = find_weather(n)
        if "city" in info:
            print("{city} {date} {weather} {max}/{min} {wind}".format_map(info))
        else:
            print("抱歉！未找到该城市信息")
        print("\n")
    elif c == "0":
        print("感谢使用，祝您生活愉快！")
        break
    else:
        print("输入错误，请重新输入！")
