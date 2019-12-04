def fun2(number, odd=True):
    if number % 2 == 0:
        odd = False
        print(number, "is an even number!")
    else:
        print(number, "is an odd number")


i = input("Please enter a number: ")
n = int(i)
fun2(n)