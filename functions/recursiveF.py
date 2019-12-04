def fun(a, b):
    for i in range(b):
        if b == 0:
            return 1
        elif b == 1:
            return a
    return fun(a, b-1)*a


print(fun(5, 6))
