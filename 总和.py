import random

Money = 0
dict = {}
i = 0
Library = {"1": {"name": 1,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1},
           "2": {"name": 2,
                 "password": 123456,
                 "country": 1,
                 "province": 1,
                 "street": 1,
                 "door": 1,
                 "money": 100,
                 "bank_name": 1}, }

def add():
    ID = random.randint(10000000, 99999999)  # random随机生成的整数
    name = input('请输入用户名：')
    password = input('请输入登录密码：')
    adress = input('请输入用户地址：')
    while True:
        if len(password) == 6 and password.isdigit():

            print('恭喜你添加用户成功！！!')

            Library[ID] = ['中国工商银行', name, password, 0, adress]
            print(ID, Library)
            break
        else:
            print('密码错误')
            password = input('请输入登录密码：')


#郑雪凤  取款
def withdraw():
    id = int(input('请输入账号：'))
    password = input('请输入密码：')
    withdraw1 = int(input('请您输入取钱金额:'))
    name1 = bank(id, password, withdraw1)
    if name1 == 1:
        print('用户不存在')
    elif name1 == 2:
        print('密码输入错误')
    elif name1 ==3:
        print('余额不足！！！！！！')
    else:
        print('               取款成功！')
def bank(id, password, withdraw1):
    if id in Library:
        if password != Library[id][2]:
            return 2
        else:
            if withdraw1 <= Library[id][3]:
                Library[id][3] = Library[id][3] - withdraw1
                print('            恭喜您取款成功！！！')
                print('            您的当前余额为：%0.2f元' % Library[id][3])
            elif withdraw1 > Library[id][3]:
                return 3
    else:
        return 1
# 青龙 转账
def bank_treasury(out_ID, enter_ID, out_pw, out_money):
    # 判断账号是否存在：
    if out_ID in Library and enter_ID in Library:

        if out_pw != Library[out_ID]["password"]:
            return 2
        elif Library[out_ID]["money"] - out_money < 0:
            return 3
        else:
            Library[out_ID]["money"] = Library[out_ID]["money"] - out_money
            Library[enter_ID]["money"] = Library[enter_ID]["money"] + out_money
            return 0
    else:
        return 1
def transfer():
    # 转出的账号，转入的账号，转出账号的密码，转出的金额
    out_ID = input('请输入转出的账号：')
    enter_ID = input('请输入转入的账号：')
    out_pw = int(input('请输入转出的账号的密码：'))
    out_money = int(input('请输入转账金额：'))
    reply = bank_treasury(out_ID, enter_ID, out_pw, out_money)
    if reply == 0:
        print('转账成功！')
        print('您的账户余额为：', Library[out_ID]["money"])
    elif reply == 1:
        print('您输入的账户不对！')
    elif reply == 2:
        print('密码输入错误！')
    elif reply == 3:
        print('账户金额不足！')
#马芳宇 查询
def cx():
    acc = input("请输入账号")
    pas = int(input("请输入密码"))
    for k in Library:
        acc_1 =k
        if acc == acc_1:
            pas_1 = Library[k]["password"]
            if pas == pas_1:
                print('账号:', Library[k]["name"])
                print('密码:', Library[k]["password"])
                print('余额:', Library[k]["money"])
                print('居住地址:', Library[k]["country"], Library[k]["province"], Library[k]["street"], Library[k]["door"])
                print('开户银行地址:', Library[k]["bank_name"])
            else:
                print("密码错误")
        else:
            print("您查找的账户不存在")
#黄华涛 存款
def SaveMoney():  # 银行的数据库存款
    names = input("请输入您的账户")
    password = int(input("请输入密码"))
    if names in Library:
        if password == Library[names]["password"]:
            L = int(input("请输入要存的金额"))
            Library[names]["money"] = Library[names]["money"] + L
            Library[names]["money"] = Library[names]["money"]
            print(Library[names]["money"])
        return False
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
        SaveMoney
    elif num=='3':
        withdraw()
    elif num =='4':
        '''
        # 首页界面
        def front_page():
            print('**********欢迎来到中国建设银行*********')
            print('1、开户')
            print('2、存钱')
            print('3、取钱')
            print('4、转账')
            print('5、查询')
            print('6、Bye')
            print('************************************')
        '''
        transfer()
    elif num=='5':
        cx()