'''

    水杯的属性：
        高度：height
        容积：volume
        颜色：colore
        材质：material
    功能：
        能存放的液体：liquid

'''
import time


class User:
    name = ""
    height = 0
    volume = 0
    colore = ""
    material = ""
    liquid = ""

    def yanse(self):
        print("名字：", self.name,
              "，颜色：", self.colore, "黄色",
              "，材质：", self.material, "4S材质",
              "，液体:", self.liquid, "白开水",
              "，高度:", self.height, "cm",
              "，容量:", self.volume, "ml")


p = User()
p.name = "保温杯"
p.height = 15
p.volume = 1000
p.material = "材质"
p.colore = "颜色"
p.liquid = "液体"

p.yanse()

'''
    电脑的属性：
            屏幕：screen
            价格：Price
            CPU型号：model
            内存：Memory
            待机：Standby
    功能：
        打字：typing
        打游戏：games
        看视频：videos  
'''


class Computer:
    # 属性
    computer = ""
    screen = 0
    Price = 0
    model = ""
    Memory = 0
    Standby = 0

    # 行为
    typing = ""
    games = ""
    videos = ""

    def dring(self):  # 属性
        print("这是", self.computer,
              "，屏幕：", self.screen, "英寸",
              "，价格：", self.Price, "元",
              "，型号：", self.model,
              "，内存：", self.Memory, "个GB",
              "，待机时间：", self.Standby, "分钟",
              "，可以", self.typing,
              "，可以", self.games,
              "，可以", self.videos)
        for i in range(6):
            print(".", end="")
            time.sleep(1)
        print("这个平板电脑太辣鸡")


# 属性
p = Computer()
p.computer = "笔记本电脑"
p.screen = 90
p.Price = 10000
p.model = "安卓"
p.Memory = 100
p.Standby = 10
# 行为
p.typing = "打字"
p.games = "打游戏"
p.videos = "看视频"

p.dring()
