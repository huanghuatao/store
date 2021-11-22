import random
import pymysql

# fetchone()返回单个的元组
# fetchall()返回多个元组
# 连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="company")
'''
# 创建控制台
cursor = con.cursor()
sql = "insert into us values(%s,%s) "
user = ('admine', 123456)
# 执行sql语句
cursor.execute(sql, user)
# 提交到数据库
con.commit()
# 关闭资源
cursor.close()
con.close()
'''
Money = 0
i = 0


def add():
    ID = random.randint(10000000, 99999999)  # random随机生成的整数
    name = input('请输入用户名：')
    password = input('请输入登录密码：')
    country = input('请输入国家：')
    province = input('请输入省份：')
    city = input('请输入市：')
    street = input('请输入街道：')
    money = 0
    bank_name = '中国工商银行昌平区分行'
    while True:
        if len(password) == 6 and password.isdigit():
            # con = pymysql.connect(host="localhost", user="root", password="root", database="db_goods")
            cursor = con.cursor()
            sql = "insert into us values(%s,%s,%s,%s,%s,%s,%s,%s,%s) "
            user = (ID, password, name, country, province, city, street, money, bank_name)
            cursor.execute(sql, user)  # 执行sql语句
            con.commit()  # 提交到数据库
            cursor.close()  # 关闭控制台
            print('恭喜你添加用户成功！！!')
            print('您的账号为:', ID)
            break
        else:
            print('密码错误')
            password = input('请输入登录密码：')


def verify():
    acc = int(input("请输入账号"))
    password = input("请输入密码")
    cursor = con.cursor()
    sql = "select * from us "
    cursor.execute(sql)  # 执行sql语句
    for line in cursor.fetchall():
        if acc in line:
            while True:
                if line[1] == password:
                    return line
                    break
                else:
                    password = input('密码错误,请重新输入密码')
    cursor.close()  # 关闭控制台


def withdraw():
    v = verify()
    withdraw1 = float(input('请您输入取钱金额:'))
    if v[7] < withdraw1:
        print('您的余额不足,无法取款')
    else:
        mone = v[7] - withdraw1
        # update
        cursor = con.cursor()
        sql = f"update us set money = %s where id = %s "
        user = (mone, v[0])
        # 执行sql语句
        cursor.execute(sql, user)
        # 提交到数据库
        con.commit()
        # 关闭资源
        cursor.close()


def transfer():
    v = verify()
    enter_ID = int(input('请输入转入的账号：'))
    out_money = float(input('请您输入转账金额:'))
    if v[7] < out_money:
        print('您的余额不足,无法转账')
    else:
        mone = v[7] - out_money
        # update
        cursor = con.cursor()
        sql = "update us set money = %s where id = %s "
        user = (mone, v[0])
        # 执行sql语句
        cursor.execute(sql, user)
        sql = "select * from us "
        cursor.execute(sql)  # 执行sql语句
        # 提交到数据库
        con.commit()
        for line in cursor.fetchall():
            if enter_ID in line:
                mon = line[7] + out_money
                sql_1 = "update us set money = %s where id = %s "
                us = (mon, line[0])
                cursor.execute(sql_1, us)
                # 提交到数据库
                con.commit()
        # 关闭资源
        cursor.close()


def cx():
    acc = int(input("请输入账号"))
    password = input("请输入密码")
    cursor = con.cursor()
    sql = "select * from us "
    cursor.execute(sql)  # 执行sql语句
    for line in cursor.fetchall():
        if acc in line:
            while True:
                if line[1] == password:
                    print('您的账号:', line[0], '余额:', line[7], '姓名:', line[2], '开户地:', line[8])
                    break
                else:
                    password = input('密码错误,请重新输入密码')
    cursor.close()  # 关闭控制台


def SaveMoney():  # 银行的数据库存款
    v = verify()
    withdraw1 = float(input('请您输存款金额:'))
    mone = v[7] + withdraw1
    cursor = con.cursor()
    sql = f"update us set money = %s where id = %s "
    user = (mone, v[0])
    # 执行sql语句
    cursor.execute(sql, user)
    # 提交到数据库
    con.commit()
    # 关闭资源
    cursor.close()


print('*********************中国工商银行**********************')
print('*1.开户')
print('*2.存钱')
print('*3.取钱')
print('*4.转账')
print('*5.查询')
print('*6.Bye！')
print('************************************************************')

while 1:
    num = input('请选择您需要的业务：')
    if num == '1':
        add()
    elif num == '2':
        SaveMoney()
    elif num == '3':
        withdraw()
    elif num == '4':
        transfer()
    elif num == '5':
        cx()
    elif num == '6':
        break
    else:
        print('输入有误,请重新输入')
