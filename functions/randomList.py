import random


def fun3():
    n = random.randint(0, 100)
    l = list()
    for i in range(0, n+1):
        n2 = random.randint(0, 1000)
        l.append(n2)
    return l


def fun4(l):
    max = 0
    for i in l:
        if i > max:
            max = i
    return max


def fun5(l):
    l.sort()
    return l


def fun6(lis):
    length = len(lis)
    found = True
    while found:
        found = False
        for i in range(0, length-1):
            if lis[i] > lis[i+1]:
                found = True
                lis[i], lis[i+1] = lis[i+1], lis[i]
    return lis


l = fun3()
print("FUN 5: ", fun5(l))
print("")
print("FUN 6:", fun6(l))

