from collections import OrderedDict
import random
lst=sorted([(random.randint(20,100))for i in range(1000)])
print(lst,end='\n\n')

od=OrderedDict()
for k in lst:
    od.setdefault(k,0)
    od[k]+=1
print(od)


goods = [{"name": "电脑  ", "price": 1999},

         {"name": "鼠标  ", "price": 10},

         {"name": "显示器", "price": 120},

         {"name": "内存  ", "price": 230}, ]
for a in range(len(goods)):
    print(a + 1, ' ', goods[a]['name'], ' ', goods[a]['price'])
while True:
    try:
        a = input('请输入商品序号')
        if a == 'q' or a == 'Q':
            print('退出系统')
            break
        else:
            print(a, ' ', goods[int(a) - 1]['name'], ' ', goods[int(a) - 1]['price'])
    except:
        print('请输入正确的序号')
        continue








