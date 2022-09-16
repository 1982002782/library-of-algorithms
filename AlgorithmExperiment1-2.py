import time
from random import *
import matplotlib.pyplot as plt
import matplotlib

N = [10, 100, 500]
MAX = int(input("请输入数字的上限:"))
time1 = []
time2 = []


def fun1(N, MAX):  # 获取随机数列表
    list1 = []
    for i in range(N):
        r = randint(0, MAX)
        list1.append(r)
    return list1


def BubbleSort(list):  # 冒泡排序
    long = len(list) - 1
    flag = 1
    while long > 0 and flag == 1:
        flag = 0
        for i in range(long):
            if list[i] > list[i + 1]:
                flag = 1
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
        long = long - 1


def AdjustArray(list, l, h):  # 返回调整后基准数的位置
    i = l
    j = h
    x = list[l]
    while i < j:
        # 从右往左找小于x的数填入list[i]
        while i < j and list[j] >= x:
            j = j - 1
        if i < j:
            list[i] = list[j]
            i = i + 1
        # 从左往右找大于x的数填入list[j]
        while i < j and list[i] < x:
            i = i + 1
        if i < j:
            list[j] = list[i]
            j = j - 1
    # 退出时，i等于j。将x填到这个坑中。
    list[i] = x
    return i


def QuickSort(list, l, h):  # 快速排序
    if l < h:
        i = AdjustArray(list, l, h)
        QuickSort(list, l, i - 1)  # 递归调用
        QuickSort(list, i + 1, h)


def Experiment1():
    for num in N:
        timelist = []
        for i in range(10):
            old_time = time.perf_counter()
            BubbleSort(fun1(num, MAX))
            timelist.append(time.perf_counter() - old_time)
        time1.append(sum(timelist) / len(timelist))
    print("冒泡排序的平均时间为：", end=" ")
    print(time1)

def Experiment2():
    for num in N:
        timelist = []
        for i in range(10):
            old_time = time.perf_counter()
            list = fun1(num, MAX)
            QuickSort(list, 0, len(list) - 1)
            timelist.append(time.perf_counter() - old_time)
        time2.append(sum(timelist) / len(timelist))
    print("快速排序的平均时间:", end=" ")
    print(time2)


if __name__ == '__main__':
    Experiment1()
    Experiment2()
    plt.style.use("seaborn")
    matplotlib.rc("font", family='FangSong')
    plt.xlabel("数字个数")
    plt.ylabel("运行时间")
    plt.plot(N, time1)
    plt.plot(N, time2)
    plt.show()
