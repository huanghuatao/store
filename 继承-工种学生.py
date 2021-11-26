'''
i.	人：年龄，性别，姓名。
ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''


class oldwork:
    username = ""
    age = 0
    sex = ""
    work = ""

    def do(self, work):
        print("现在有个工种:", self.work, "姓名:", self.username, "，年龄", self.age, "，性别", self.sex, "，正在", work)


class newwork(oldwork):
    number = ""
    work = ""

    def do(self, work):
        super().do(work)


p = newwork()
p.username = "张三"
p.age = 20
p.sex = "男"
p.work = "学生"
p.do("学习，唱歌")
