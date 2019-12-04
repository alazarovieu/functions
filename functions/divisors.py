def fun(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        print(" It is a prime number!")
        return divisors

    return divisors


print(fun(23))
