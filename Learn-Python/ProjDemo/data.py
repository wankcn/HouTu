"""
    main
"""

# 打开数据库连接
import pymysql
import datetime  # 获取系统时间模块

# 打开数据库连接
db = pymysql.connect("localhost", "root", "APTX4869", "Staff")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 获取系统时间 定义系统时间格式

# 获取该格式时间
theTime = datetime.datetime.now().strftime("%Y-%m-%d")

new_time = datetime.datetime.now().strftime("%H:%M:%S")


def create():
    """
        创建 用户数据表 和时间数据表
    """
    # 使用 execute() 方法执行 SQL，如果表存在则删除
    cursor.execute("DROP TABLE IF EXISTS userinfo")
    cursor.execute("DROP TABLE IF EXISTS timeinfo")

    # 使用预处理语句创建新的用户信息表
    user_sql = """
            CREATE TABLE userinfo(
            -- count INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   -- 自增长计数
            session VARCHAR(20) NOT NULL PRIMARY KEY,        -- 计算机地址 
            ip VARCHAR(16) NULL,                             -- 计算机ip地址
            user_name VARCHAR(20) NULL,                      -- 用户姓名
            gender VARCHAR(10) NULL,                         -- 用户性别
            email VARCHAR(50) NULL,                          -- 用户邮箱
            phone_number VARCHAR(11) NULL                    -- 用户电话号码
            )"""
    cursor.execute(user_sql)
    print("**     创建用户数据表成功     **")
    # 创建新的签到时间记录表
    time_sql = """
            CREATE TABLE timeinfo(
            count INT NOT NULL AUTO_INCREMENT PRIMARY KEY,   -- 这里的计数应该是唯一的
            session VARCHAR(20)  NULL ,               -- 计算机地址 
            check_in VARCHAR(16) NULL,                       -- 上班签到时间
            check_out VARCHAR(20) NULL,                      -- 下班打卡时间
            data_time VARCHAR(20) NULL                       -- 打卡当天日期
            )"""
    cursor.execute(time_sql)
    print("**     创建时间数据表成功     **")


def match():
    """
        查询数据库是否存在相应的资料
    """
    global sever_session
    sever_session = "ACDE48001122"  # input

    # 获取数据库主机session信息
    sql = "select session from userinfo"
    cursor.execute(sql)  # 执行sql语句
    result = cursor.fetchall()  # 存放sql结果的元组
    # print(result)  # 二维元组
    data_session = []  # 存放session信息的列表
    # 把session存入列表中
    for x in result:
        for y in x:
            data_session.append(y)
    global b
    print("这里显示当前获取到的计算机已有主机用户名:{}".format(data_session))
    b = (sever_session in data_session)
    return b


def into_user():
    """
        插入用户数据
    """
    # 像数据库中插入新的用户信息
    user = "INSERT INTO userinfo(session,ip,user_name,gender,email,phone_number) " \
           "VALUES (%s,%s,%s,%s,%s,%s)"
    values = ("ACDE48001122",
              "192.168.1.245",
              "wankcn",
              "male",
              "wankcn@icloud.com",
              "13520562678"
              )
    cursor.execute(user, values)
    db.commit()
    print("---------插入用户数据成功---------")


def into_time():
    """
        插入时间表数据
    """
    # 像数据库中插入新的时间信息
    time = "INSERT INTO timeinfo(session,check_in, data_time) " \
           "VALUES (%s,%s,%s)"
    values = ("ACDE48001122",
              new_time,
              theTime
              )
    cursor.execute(time, values)
    db.commit()
    print("---------插入时间数据成功---------")


def judge():
    """
        判断时间表的日期和打卡时间是否存在
    """
    global sever_checkin, sever_day
    sever_checkin = "01"  # input
    sql = "select check_in from timeinfo"
    cursor.execute(sql)
    result = cursor.fetchall()
    data_checkin = []
    # 把数据库中的时间信息存入列表中
    for x in result:
        for y in x:
            data_checkin.append(y)
    print("当前数据库已包含的时间列表{}".format(data_checkin))
    sever_day = theTime  # input
    sql = "select data_time from timeinfo"
    cursor.execute(sql)
    result = cursor.fetchall()
    data_day = []
    # 把数据库中的日期信息存入列表中
    for x in result:
        for y in x:
            data_day.append(y)
    print("当前数据库已包含的日期列表{}".format(data_day))
    x = ((sever_day in data_day) and (sever_checkin in data_checkin))
    return x


def clock():
    if judge() == True:
        time = "INSERT INTO timeinfo(session,check_in,data_time) " \
               "VALUES (%s,%s,%s)"
        values = ("ACDE48001123",
                  new_time,
                  theTime
                  )
        cursor.execute(time, values)
        db.commit()
        print("---------插入上班打卡数据成功---------")
    else:

        # 下班打卡
        # update_out = "UPDATE timeinfo SET check_out=%s WHERE data_time=%s,"
        # values = (new_time,
        #           theTime
        #           )
        cursor.execute("UPDATE timeinfo SET check_out=%s WHERE data_time=%s", (new_time, theTime))
        db.commit()
        print("---------更新下班打卡数据成功---------")


if __name__ == '__main__':
    
    # input("第一天创建数据库的两张表")
    # create()
    input("这里判断唯一逐句session是不是存在 -->")
    if match():  # 存在调用时间表方法

        input("--> 存在的情况下进入打卡签到操作")
        clock()  # 操作时间表

    else:  # 不存在主机地址插入新的数据
        input("--> 不存的情况下 先建立插入主机的用户数据，然后更新打卡表:")
        into_user()
        input("--> 插入用户数据成功，接下来开始插入打卡数据")
        time = "INSERT INTO timeinfo(session,check_in,data_time) " \
               "VALUES (%s,%s,%s)"
        values = ("ACDE48001123",
                  new_time,
                  theTime
                  )
        cursor.execute(time, values)
        db.commit()
        print("---------插入第一次打卡数据成功---------")

# 关闭数据库
db.close()
