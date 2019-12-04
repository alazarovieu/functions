import random


def fun():
    total = 0
    for i in range(0, 11):
        i = random.randint(0, 1000)
        total += i

    print("The total sum of the 10 numbers is: ", total)

fun()
