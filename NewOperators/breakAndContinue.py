# BREAK terminates the loop without finishing
# CONTINUE skips the rest of the suite and goes back to testing
# the initial expression from THE BEGINNING

while True:
    num = input("Give me a number or type quit to exit: ")
    num2 = input("Give me another number or type quit to exit:")
    if num == "quit" or num2 == "quit":
        break

    num = int(num)
    num2 = int(num2)

    if num2 == 0:
        print("You cannot divide by Zero")
        continue

    print("The division result of", num, "and", num2, "is", num/num2)