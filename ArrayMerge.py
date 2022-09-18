def print_list(lst):
    for i in range(len(lst)):
        if i != len(lst) - 1:
            print(lst[i], end=' ')
        else:
            print(lst[i])


T = int(input())
C = []
i = 0
j = 0
for t in range(T):
    A = [int(num) for num in input().split()]
    A.sort()
    B = [int(num) for num in input().split()]
    B.sort()
    ALen = len(A) - 1
    BLen = len(B) - 1
    while i <= ALen and j <= BLen:
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i <= ALen:
        C.append(A[i])
        i += 1
    while j <= BLen:
        C.append(B[j])
        j += 1
    print_list(C)
