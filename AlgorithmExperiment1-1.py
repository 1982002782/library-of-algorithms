from random import *
import time
import matplotlib.pyplot as plt
import matplotlib

n = [10, 100, 200, 400, 500, 600, 800, 1000]
MAX = int(input("请输入数字的上限"))
times = []  # 用于存放每个问题规模实验一千次时每次所需要的平均时间


def fun1(n, MAX):  # 用于生成一个n个数字的随机数列表
    list1 = []
    for i in range(n):
        r = randint(0, MAX)
        list1.append(r)
    return list1


def fun2(list2):  # 用于找出列表list2内的最大值
    Maxnum = list2[0]
    for num in list2:
        if num > Maxnum:
            Maxnum = num
    return Maxnum


for numbers in n:
    timelist = []
    Maxlist = []
    for i in range(1000):
        oldtime = time.perf_counter()
        list1 = fun1(numbers, MAX)  # 获取随机数列表
        Maxlist.append(fun2(list1))
        timelist.append(time.perf_counter() - oldtime)  # 一次实验所需的时间
    times.append(sum(timelist) / len(timelist))
print(times)
plt.style.use("seaborn")
matplotlib.rc("font", family='FangSong')
plt.xlabel("数字个数")
plt.ylabel("运行时间")
plt.plot(n, times)
plt.show()
