"""
    简单的货币兑换系统
    实现：
    人民币〈=〉美元
    人民币 =〉欧元
"""

service_menu = {
    "1": "人民币转换美元",
    "2": "美元转换人民币",
    "3": "人民币转换欧元",
    # "4": "查看兑换汇率",
    "0": "结束程序"
}

while True:
    # 打印登录界面
    print("**********欢迎使用货币服务转换系统**********")
    # 遍历字典
    for k, v in service_menu.items():
        print("{0}.{1}".format(k, v))
    print("****************************************")
    # 进行服务操作
    Your_Choice = input("请您选择需要的服务：")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if Your_Choice == "1":
        print("欢迎使用人民币转换美元服务")
        your_money = int(input("请输入您需要转换的人民币金额："))
        print("您需要转换的人民币为：{}¥".format(your_money))
        RMB_to_US = your_money / 6.72
        print("兑换成美元为：{:,.2f}$".format(RMB_to_US))
        print("========================================\n")
    elif Your_Choice == "2":
        print("欢迎使用美元转换人民币服务")
        your_money = int(input("请输入您需要转换的美元金额："))
        print("您需要转换的美元为：{}$".format(your_money))
        US_to_RMB = your_money * 6.72
        print("兑换成人民币为：{:,.2f}¥".format(US_to_RMB))
        print("========================================\n")
    elif Your_Choice == "3":
        print("欢迎使用人民币转换欧元服务")
        your_money = int(input("请输入您需要转换的人民币金额："))
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_EUR = your_money * 0.13
        print("兑换成欧元为：{:,.2f}欧元".format(RMB_to_EUR))
        print("========================================\n")
    # elif Your_Choice == "4":
    #     print("兑换汇率如下：")
    #     print("1美元 = 6.72人民币\n1人民币 = 0.13欧元")
    #     print("========================================\n")
    elif Your_Choice == "0":
        print("感谢您的使用，祝您生活愉快，再见！")
        break
    else:
        print("输入错误，请重新输入\n")
