'''
    老手机：
        打电话：
            姓名，电话号码，铃声，归属地
        新打电话：
            姓名，电话号码，铃声，归属地，大头贴，录音
    新手机：
'''
import time


# 老手机
class OldPhone:
    username = ""  # 姓名
    phoneNumber = ""  # 电话号码
    voice = ""  # 铃声
    address = ""  # 归属地

    def call(self, number):
        print(self.username, "，手机号号码：", self.phoneNumber, "正在给", number, "打电话！")
        for i in range(8):
            print(".", end="")
            time.sleep(1)
        print("响铃：", self.voice, "本机归属地：", self.address, "!已成功接通：")


# 新手机
class NewPhone(OldPhone):
    picture = ""
    mic = False

    def call(self, number):
        # 老功能交给老代码执行
        super().call(number)

        # 新功能自己劳作
        # 开启录音
        self.mic = True
        print("品牌为：", self.picture, "!")


p = NewPhone()
p.phoneNumber = "135522648187"
p.voice = "最炫民族风"
p.address = "北京移动"
p.username = "jason jia"
p.picture = "小米的手机很好用"

p.call("17648841550")
