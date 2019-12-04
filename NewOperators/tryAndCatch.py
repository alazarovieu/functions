# You TRY to run some code and if there is an ERROR,
# you catch an EXCEPTION

try:
    n = input("Please enter a number: ")
    number = int(n)
except ValueError:
    print("Boy!!! You did not enter an input :(")

# List of standard exceptions in PYTHON
# https://www.tutorialspoint.com/python/standard_exceptions.htm
