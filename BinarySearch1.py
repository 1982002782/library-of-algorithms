n = int(input())


def input_list():
    l = []
    for num in input().split():
        if len(l) >= n:
            break
        l.append(int(num))
    return l


list = input_list()
target = int(input())


def BinarySearch(list, target):
    if len(list) == 0:
        return -1
    mid = len(list) // 2
    if list[mid] == target:
        return mid
    elif target < list[mid]:
        return BinarySearch(list[:mid], target)
    else:
        return mid + 1 + BinarySearch(list[mid + 1:], target)


mid = BinarySearch(list, target)
print(mid)
