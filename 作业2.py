'''list=[]
for _ in range(10):
    while 1 :
        num=input("输入第{}个整数: ".format(_+1))
        if not num:
            print('输入为空请重新输入 ! ')
        if num.isdigit():
            list.append(int(num))
            break
        else:
            print("要输入整数")
print('当前输入的所有数字的和是: {}'.format(sum(list)))'''#10个数的结果

'''def NxN(n):
    for i in range(1,n+1):
        for j in range(1,i+1):

            print(j,"x",i,"=",(j*i),"\t",end="")
        print()
while True:
    chose=input("请输入N层乘法")
    chose=int(chose)
    NxN(chose)'''#NN乘法表

'''list=[]
for _ in range(10):
    while 1 :
        num=input("输入第{}个整数: ".format(_+1))
        if not num:
            print('输入为空请重新输入 ! ')
        if num.isdigit():
            list.append(int(num))
            break
        else:
            print("要输入整数")
print("最大的数是 :{}".format(list))
print('当前输入的所有数字的和是: {}'.format(sum(list)))'''#最大数、和、平均值

'''n, w = 9, 9
while n > 0:
    o = 1
    while o <= w:
        print(n, '*', o, '=', n * o, end=' ')
        o += 1
    n -= 1
    w -= 1
    print('')'''#99乘法表

'''import random
randint_num=random.randint(50, 150)
while True:
    num=int(input("请输入一个数字"))
    if num ==randint_num:
        print("Ok")
        break
    elif num>randint_num:
        print("你输入的过大")
    elif num<randint_num:
        print("你输入的过小")'''#50~150之间的数

'''for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i+1):
        print("* ",end="")
    print("")'''#打印三角形

'''a=int(input("请输入你的第一条边长: "))
b=int(input("请输入你的第二条边长: "))
c=int(input("请输入你的第三条边长: "))
if a+b>c and b+c>a and c+a>b:
    print("可以构成三角形" )
    if a==b==c:
        print("等边三角形")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("等腰三角形")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("直角三角形")
    else:
         print("普通三角形")
else:
    print("不能构成三角形")'''#判断三角形

'''x=input("请输入x的值：")
y=input("请输入y的值：")
x,y=y,x
print("交换后的x值为：{}".format(x))
print("交换后的y值为：{}".format(y))'''#使用+，-号实现两个数的调换

'''name="root"
passwd="admin"
for i in range(0,3):
    use_name=input("用户名")
    num_passwd=input("密码")
    if use_name==use_name and num_passwd==passwd:
        print("密码输入正确")
        break
    elif name!=use_name or passwd!=num_passwd:
        if i < 2:
            print("密码输入错误")
        else:
             print("三次输入错误，系统自动锁定")'''#三次密码输入错误锁定功能

'''a=input('输入井口的高度')
b=int(a)/2
if int(list(str(b))[-1])>1:
    c=str(int(b))+'1'
    print("跳出井口的天数为：%s"%c)
elif int(list(str(b))[-1])==0:
    print("跳出井口的天数为：%s"%int(b))'''#青蛙跳井

'''def recursion(n): #'定义递归函数实现求阶乘功能'
    if n==1:
        return 1
    else:
        return n*recursion(n-1)
list=[ ] #定义一个空的列表，将调用递归函数生成的阶乘值追加到列表
for i in range(1,20):
    list.append(recursion(i))# 将调用递归函数生成的阶乘值追加到列表
print('阶乘之和',sum(list)) #列表求和
Sum = 0
for i in range(1,20):
    Sum +=recursion(i)
print('阶乘之和',Sum)'''#用循环来实现20以内的数的阶乘

'''import random  

z = 0
while 1: 
    randint_num = random.randint(0, 100) 
    min_, max_, integral = 0, 100, 1000
    while 1: 
        z += 1
        try:  
            a = input('请输入你预测的数字')  
            if a == 'q' or a == 'Q':  
                print('游戏退出')
                integral = 0  
                break  
            num = int(a) 
            integral = integral - 100
        except ValueError:  
            print('请输入正确的数字')
            break  
        else: 
            if num > 100 or num < 0:  
                print('请输入0至100之间的数字', ',第', z, '次', ',积分为', integral)
            elif num == randint_num:  
                print('猜对了,重新来')
                break  
            elif num < randint_num:  
                print(num, '到', max_, ',第', z, '次', ',积分为', integral)
                if min_ < num: 
                    min_ = num
            elif num > randint_num: 
                print(min_, '到', num, ',第', z, '次', ',积分为', integral)
                if max_ > num:  
                    max_ = num
            if integral <= 0:  
                print('你输了')
                break 
    if integral <= 0:  
        break '''#猜字游戏

'''char=0
Oax_li=0
fLul=0
BYTE=0
T_T=0
Cy%ty=0#不合法
$123=0#不合法
3_3 =0#不合法'''#判断变量命名是否合法
