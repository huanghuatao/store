'''dict = {"k1":"v1","k2":"v2","k3":"v3"}
for key in dict:
    print(key)
for c in dict:
    print(dict[c])
dict["k4"]="v4"
print(dict)'''

'''info={}
info['苹果']=32.8
info['香蕉']=22
info['葡萄']=15.5
print(info)'''

'''Friuts = {
    '苹果': 12.3,
    '草莓': 4.5,
    '香蕉': 6.3,
    '葡萄': 5.8,
    '橘子': 6.4,
    '樱桃': 15.8}


info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 1
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 1
    }
}

d = 0
Friuts_money = list(Friuts.values())
for name_ in info.keys():
    c = 0
    for a in Friuts.keys():
        b = info[name_]['fruits'].get(a, -1)
        if b == -1:
            continue
        else:
            c = c + b * Friuts_money[d]
            d += 1
    info[name_]['money'] = c
print(info)'''# 请将上面的数据存储到字典里，可以根据水果名称查询购买这个水果的费用，
# 请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。

'''import  collections
my_list=[21,21,21,56,56,56,56,56,56,56,56,56,10,10,10]
ctr=collections.Counter(my_list)
print("列表中元素的频率：",dict(ctr))'''

'''names = [
    ["刘备", "56", "男", "106", "IBM", 500, "50"],
    ["大乔", "19", "女", "230", "微软", 501, "60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700, "10"]
]
age = ['姓名','年龄', '性别', '编号', '任职公司', '薪资', '部门编号']
emintion = {}
s = 0
while s < len(names):
    i = 1
    a = {}
    while i <= 6:
        a[age[i]] = names[s][i]
        i += 1
    emintion[names[s][0]] = a
    s += 1
print(emintion)

age1 = ['年龄', '性别', '编号', '任职公司', '薪资', '部门编号']
for tal in names:
    emintion[tal[0]] = {age1[x]:tal[1:][x] for x in range(len(age1))}
print(emintion)'''





