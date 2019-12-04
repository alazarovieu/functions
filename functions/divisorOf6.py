def fun():
    try:
        n = int(input("Please enter a multiple of the number 6: "))
        print("")
        divisors = []

        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        for i in divisors:
            try:
                if 6 == divisors[i]:
                    print("Well done!", n, "is a multiple of 6.")
                    return divisors
            except IndexError:
                return print(n, "is not a multiple of 6")

    except ValueError:
        print("")
        print("A multiple implies that not only it has to be \n"
              "a number but the result of its division with the number 6 has to be 0.")


print(fun())
