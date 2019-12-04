# Functions transform inputs into outputs


def Name(n):
    """
    :simulates a conversation
    """
    print("- My name is ", n)
    print("+ Nice to meet you!")


i = input("+ Please enter your name: ")
Name(i)
print("")

# Recurrent functions intro!!!


def introduce(name):
    """
    :parameter name: a regular string
    :return: prints the name
    """
    print("The name is:", name)


def bond(first_name="james", last_name="bond"):
    """
    Cool function
    :param first_name: first name, default "james"
    :param last_name: last name, default "bond"
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return last_name+","+" "+first_name+" "+last_name


introduce(bond())
