print("欢迎使用电价计算器")
print("输入用电量：")
elec_num = input()
elec_num =int(elec_num)
charge = (240 * 0.4883) + (400 - 240) * 0.5383 + (elec_num - 400) * 0.7883
print("本月用电量：")
print(elec_num)
print("本月应缴电费：")
print(charge)

