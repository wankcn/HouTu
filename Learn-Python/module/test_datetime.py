import datetime
# from datetime import datetime
import time

print(dir(datetime))

# 打印现在时间
now_time = datetime.datetime.now()
print("现在时间:{}".format(now_time))

# 当前的日期
print("当前的日期:{}".format(now_time.date()))
# 当前的时间
print("当前的时间:{}".format(now_time.time()))

# 当前年份
print("year:{}".format(now_time.year))
# 当前月份
print("month:{}".format(now_time.month))
# 当天日期
print("day:{}".format(now_time.day))

print(dir(now_time))

print("--------------------------------")
print(time.time())  # 获取到当前毫秒数 1970年到现在







from datetime import datetime
# 得到当前日期时间（两种方法）
now =datetime.now()
print("当前日期时间：{}".format(now))
now =datetime.today()
print("当前日期时间：{}".format(now))
# 得到当前日期
print("当前日期：{}".format(now.date()))
# 得到当前时间
print("当前时间：{}".format(now.time()))
# 得到当前年份用year_变量接收
year=now.year
# 得到当前月份用month_变量接收
month =now.month
# 得到当前天用day_变量接收
day =now.day
# 使用-拼接年月日得到当前日期
print("当前日期：{0}-{1}-{2}".format(year,month,day))