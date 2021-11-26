"""
厨师：每造一个蛋挞放到柜子里，
如果已经满了停3秒然后在造。
柜子里面只能放500个
"""
from threading import Thread

import time

eggpool = 0  # 全局变量 蛋挞池子


class cooker(Thread):  # 定义一个厨师类
    cooker_name = ""
    eggpool_sum = 0

    def run(self) -> None:
        global eggpool
        start = time.time()
        while True:
            end = time.time()
            if (end - start) < 60:
                if eggpool < 500:
                    self.eggpool_sum = self.eggpool_sum + 1
                    eggpool = eggpool + 1
                else:
                    time.sleep(3)
            else:
                break
        return self.eggpool_sum


class customer(Thread):  # 定义一个顾客类
    customer_name = ""
    money = 5000.0
    many = 0

    def run(self) -> None:
        global eggpool
        start = time.time()  # 开始时间
        while True:
            end = time.time()  # 结束时间
            if end - start < 60:  # 时间60秒
                if eggpool > 0:

                    if self.money >= 3:
                        self.money = self.money - 3
                        eggpool = eggpool - 1
                        self.many = self.many + 1
                    else:
                        break
                else:
                    time.sleep(2)
            else:
                break
        # print(self.customer_name,"一共抢了",self.many,"个蛋挞")
        return self.many


cooker1 = cooker()
cooker1.cooker_name = "厨师1"

cooker2 = cooker()
cooker2.cooker_name = "厨师2"

cooker3 = cooker()
cooker3.cooker_name = "厨师3"

customer1 = customer()
customer1.customer_name = "顾客1"

customer2 = customer()
customer2.customer_name = "顾客2"

customer3 = customer()
customer3.customer_name = "顾客3"
customer3.money = 5000

customer4 = customer()
customer4.customer_name = "顾客4"

customer5 = customer()
customer5.customer_name = "顾客5"

customer6 = customer()
customer6.customer_name = "顾客6"

cooker1.start()
cooker2.start()
cooker3.start()
customer1.start()
customer2.start()
customer3.start()
customer4.start()
customer5.start()
customer6.start()

cooker1.join()
cooker2.join()
cooker3.join()
customer1.join()
customer2.join()
customer3.join()
customer4.join()
customer5.join()
customer6.join()

print(cooker1.cooker_name, "做出了", cooker1.eggpool_sum, "个蛋挞!", "工资", cooker1.eggpool_sum * 1.5)
print(cooker2.cooker_name, "做出了", cooker2.eggpool_sum, "个蛋挞!", "工资", cooker2.eggpool_sum * 1.5)
print(cooker3.cooker_name, "做出了", cooker3.eggpool_sum, "个蛋挞!", "工资", cooker3.eggpool_sum * 1.5)
print(customer1.customer_name, "一共抢了", customer1.many, "个蛋挞")
print(customer2.customer_name, "一共抢了", customer2.many, "个蛋挞")
print(customer3.customer_name, "一共抢了", customer3.many, "个蛋挞")
print(customer4.customer_name, "一共抢了", customer4.many, "个蛋挞")
print(customer5.customer_name, "一共抢了", customer5.many, "个蛋挞")
print(customer6.customer_name, "一共抢了", customer6.many, "个蛋挞")
