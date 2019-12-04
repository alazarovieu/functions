# TUPLES are like a sequence of values
# You define tuples as: t = (5,) {THIS IS AN INT} like lists

a = (8, 9, 10)
print(a)
print("")

b = ("me", 69, "Alberto"+"seforra"+"$", 99)
print(b)
print("")

c = (5,)
print(type(c))
print("")

# TUPLES ARE IMMUTABLE == they cannot be changed

name = "Alberto"
t = tuple(name)
print(t)
print("")

# TUPLES can be accessed like strings or lists

print(t[2])
print("")

# TUPLES can be sliced

print(t[2::])
print("")

