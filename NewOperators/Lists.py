# A list is a non-scalar object
# A list is a sequence of values

print("")
print("START")
print('')

a = []
# EMPTY LIST

a.append("Alberto")
a.append("Candela")
a.append(19)
a.append(18)

print(a)
print(a[2])
print("")
print("MUTABILITY")
# LISTS ARE MUTABLE

a[0] = "Albertin"
a[1] = "Candelita"
print(a)
print("")
print("SLICING")

# LISTS CAN BE SLICED
print(a[1:])
print(a[::-1])
print(a[1:3])
print("")
print("OPERATORS")

# OPERATORS: + and *
b = ["avion", "coche", "moto"]
print(b)
print(b*2)
print(a+b)
print("The length of a is: ", len(a))
print("The len of a+b is: ", len(a+b))
print("")
print("ITERATIONS")

# LISTS ARE ITERABLE
n = 1
item = "item ", n
for i in b:
    print(i)
print(b)
print("")
print("METHODS")

# LISTS ARE NON-SCALAR OBJECTS AND HAVE METHODS
a.extend(b)
print(a)
del a[3::]
print(a)
x = a.pop(0)
print(a)
print(x)
print(a)
a.remove(19)
print(a)