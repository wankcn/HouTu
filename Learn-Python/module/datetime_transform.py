from datetime import datetime, date, time, timedelta

# 自定义日期和时间
d = datetime(2020, 10, 30, 14, 5)
print(d)

d2 = date(2019, 3, 23)
print(d2)

t = time(9, 0)
print(t)

print("-----------------------------------")
# 日期、时间与字符串之间的相互转换
date_str = "2019-6-8 22:49:23"
# 转换需要上下一致 字符串转换datetime对象
ds_t = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
print(ds_t)
# datetime转换成字符串
print("-----------------------------------")
n = datetime.now()
print("当前时间:{}".format(n))  # 上下格式可以不一样
n_str = n.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后时间:{}".format(n_str))

# datetime 之间的加法操作
print("-----------------------------------")
n = datetime.now()
# 给当前时间加5天42小时
print("当前时间:{}".format(n))
n_next = n + timedelta(days=5, hours=42, minutes=63, seconds=20, microseconds=222)
print("加5天42小时之后:{}".format(n_next))

# datetime 之间的减法操作
print("-----------------------------------")
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)
rest = d2 - d1
print(rest)
print(type(rest))  # <class 'datetime.timedelta'>

rest2 = d1 - d2
print(rest2)
