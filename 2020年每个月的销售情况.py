import xlrd
import operator


def dealexcel(fname, num=0):
    file = xlrd.open_workbook(filename=fname, encoding_override=True)
    sheet = file.sheet_by_index(num)
    return sheet


# 取行数据
def rowsexcel(sheet, rows0, rows1):
    list = []
    for i in range(rows0, rows1):
        list.append(sheet.row_values(i))
    return list


# 取列数据
def colsexcel(sheet, cols0, cols1):
    list = []
    for i in range(cols0, cols1):
        list.append(sheet.col_values(i))
    return list


# 取m到n行某列数据
def dataexcel(sheet, rows1, rows2, cols):
    list = []
    for i in range(rows1, rows2):
        list.append(sheet.row_values(i)[cols])
    return list


def opers(s, a, b):
    oper = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truth
    }
    return oper[s](a, b)


# 两列表运算
def operlist(s, list1, list2):
    list = []
    for i in range(len(list1)):
        list.append(opers(s, list1[i], list2[i]))
    return list


# 计算某月到某月的总销售额
def addall(fname, num1, num2):
    sumall = 0
    for i in range(num1 - 1, num2):
        date = dealexcel(fname, i)
        sumall += sum(operlist('*', dataexcel(date, 1, date.nrows, 2), dataexcel(date, 1, date.nrows, 4)))
    return sumall


# 统计某月某列数据
def statistics(fname, month, dols):
    dict = {'总数': 0}
    data = dealexcel(fname, month - 1)
    for i in range(1, data.nrows):
        date1 = data.row_values(i)
        if date1[1] in dict:
            dict[date1[1]] += date1[dols]
        else:
            dict[date1[1]] = date1[dols]
        dict['总数'] += date1[dols]
    return dict


# 统计衣服每月销售量
def clothing(fname, num1, num2, dols):
    dict = {}
    for i in range(num1, num2 + 1):
        temp = statistics(fname, i, dols)
        for keys, values in temp.items():
            if i not in dict:
                dict[i] = {keys: values}
                continue
            if keys not in dict[i]:
                dict[i].update({keys: values})
    return dict


def printcloth(fname, num1, num2, dols):
    dict = clothing(fname, num1, num2, dols)
    list1 = []
    for i in range(num1, num2 + 1):
        for j in list(dict[i].keys()):
            if j not in list1:
                list1.append(j)
    for m in list1:
        for n in range(num1, num2 + 1):
            if m == '总数':
                continue
            if m in dict[n]:
                print('%s%d月的销售占比:' % (m, n), dict[n][m] / dict[n]['总数'])
        print()
    return 0


# 输出占比
def scale(dict):
    total = 0
    for i, j in dict.items():
        if i == '总数':
            total = j
            continue
        print('%s销售占比%s' % (i, j / total))
    return 0


# 统计销售占比
def alldata(fname, num1, num2, dols):
    dict = {}
    for i in range(num1 - 1, num2):
        dict1 = statistics(fname, i, dols)
        for keys, values in dict1.items():
            if keys in dict:
                dict[keys] += values
            else:
                dict[keys] = values
    return dict


# 统计售价
def alltype(fname, num1, num2, dols):
    dict = {}
    for i in range(num1 - 1, num2):
        dict1 = statistics(fname, i, dols)
        for keys, values in dict1.items():
            if keys == '总数':
                continue
            if keys in dict:
                continue
            else:
                dict[keys] = values
    return dict


# 输出销售额占比
def sales(dict1, dict2):
    # print(dict2)
    dict = {}
    num = sum(list(dict2.values()))
    for i, j in dict1.items():
        if i in dict2:
            dict[i] = dict1[i] * dict2[i]
            print('%s的销售额占比:' % i, dict[i] / (dict1['总数'] * num))
    return dict


# 计算最值
def contrast(dict, type=0):
    list1 = list(dict.values())
    del list1[0]
    if type == 0:
        temp = max(list1)
    elif type == 1:
        temp = min(list1)
    else:
        print('类型选择错误')
        return -1
    for keys, values in dict.items():
        if values == temp:
            return keys


fname = r'F:\2020年每个月的销售情况.xlsx'
print('总销售额:', addall(fname, 1, 12))  # 总销售额
print('总销售占比:')
scale(alldata(fname, 1, 12, 4))  # 销售件数占比
for i in range(12):  # me
    print('%d月的衣服销售占比:' % (i + 1))
    scale(statistics(fname, i, 4))
printcloth(fname, 1, 12, 4)  # 衣服月销售占比
sales(alldata(fname, 1, 12, 4), alltype(fname, 1, 12, 2))
print('最畅销的衣服是', contrast(alldata(fname, 1, 12, 4), 0))
for j in range(1, 5):
    k = 3 * (j - 1) + 1
    print('第%d季度最畅销的衣服是' % j, contrast(alldata(fname, k, k + 2, 4), 0))
print('全年销量最低的衣服是', contrast(alldata(fname, 1, 12, 4), 1))
