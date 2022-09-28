import random
import time
import matplotlib.pyplot as plt
import matplotlib


def fun(n, MAX):
    list = []
    for i in range(n):
        r = random.randint(0, MAX)
        list.append(r)
    return list


def Swap(list, x, y):
    temp = num[x]
    num[x] = num[y]
    num[y] = temp


def Partition(list, p, r):
    i = p
    j = r
    x = list[p]
    while True:
        while list[j] > x:
            j -= 1
        while list[i] < x and i < r:
            i += 1
        if i >= j:
            break
        Swap(list, i, j)

    list[p] = list[j]
    list[j] = x
    return j


def QuickSort(list, p, r):
    if p < r:
        q = Partition(list, p, r)
        QuickSort(list, p, q - 1)
        QuickSort(list, q + 1, r)


def SearchMax(list):
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max


if __name__ == '__main__':
    num = []
    n = 100
    MAX = 10000000000
    time1 = []
    for i in range(50):
        oldtime = time.perf_counter()
        num = fun(n, MAX)
        QuickSort(num, 0, len(num) - 1)
        time1.append(time.perf_counter() - oldtime)
    averagetime = sum(time1) / len(time1)
    maxtime = SearchMax(time1)
    print(time1)
    print(averagetime)
    print(maxtime)
    matplotlib.rc("font", family='FangSong')
    plt.xlabel("第n次")
    plt.ylabel("运行时间")
    plt.plot(time1, marker="o")
    plt.show()
