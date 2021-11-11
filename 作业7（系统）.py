city = {
    "北京":{
        "昌平":{
            "八达岭":["八达岭长城"],
            "回龙观":["永旺超市","永辉超市","呷哺呷哺"]
        },
        "朝阳":{
            "景观":["玉渊潭公园"]
        },
        "海淀":{
            "高校":["清华","北大"],
            "公园":["香山","植物园"],
            "博物馆":["军事博物馆","国家地质公园"]
        }
    },
    "上海":{
        "黄浦区":{
            "景观":["景观","上海城隍庙"]
        },
        "长宁区":{
            "博物馆": ["上海消防博物馆", "上海儿童博物馆"],
            "公园":["上海中山公园","儿童交通公园"]
        },
        "虹口区":{
            "博物馆": ["上海鲁迅纪念馆"],
            "公园": ["上海鲁迅公园"]
        }
    }
}

goods = {'1号':{'羽绒服', 253.6, 500, 10},
         '2号':{'牛仔裤', 86.3, 600, 60},
         '3号':{'风衣', 96.8, 335, 43},
         '4号': {'皮草', 135.9, 855, 63},
         '5号':{'T血', 65.8, 632, 63},
         '6号':{'衬衫', 49.3, 562, 120},
         '7号':{'牛仔裤', 86.3, 600, 72},
         '8号':{'羽绒服', 253.6, 500, 69},
         '9号':{'牛仔裤', 86.3, 600, 35},
         '10号':{ '羽绒服', 253.6, 500, 140}}


def showCity(data):
    for i in data:
        print(i)


def souvenir(goods):
    for i in goods:
        print(i)


while True:
    print("---------------欢迎来到Jason旅行社-----------------")
    print("有以下城市可以去：")
    showCity(city)
    print("请输入您要去的城市：")
    chose = input("")

    if chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    elif chose not in city:
        print("输入非法！请重新输入：")
    else:
        showCity(city[chose])
        chose2 = input("请输入您要去二级城市：")
        if chose2 == "q" or chose2 == "Q":
            print("欢迎下次光临！")
            break
        elif chose2 not in city[chose]:
            print("输入错误，别瞎弄！")

        else:
            showCity(city[chose][chose2])
            print("请输入要去的具体景点：")
            chose3 = input("")
            if chose3 == "q" or chose3 == "Q":
                print("欢迎下次光临！")
                break
            elif chose3 not in city[chose][chose2]:
                print("不好意思，没有这个景点！别瞎弄！")
            else:
                showCity(city[chose][chose2][chose3])
                print("每张票1000元/人！")
                
                print("有以下纪念品可以可以选择：")
                souvenir(goods)
                print("请输入您要选择的纪念品：")
                lis = input("")

                if lis == "y" or lis == "n":
                    print("欢迎下次光临！")
                    break
                elif lis not in goods:
                    print("输入非法！请重新输入：")
                else:
                    souvenir(goods[lis])
                break
            break