# A string is a collection of characters
# Non-scalar object
# Indexing a STRING returns another STRING

name = "Alberto"
print(name[1])  # Prints SECOND character, first is: n[0]
print(name[-1])  # Prints FIRST character starting from the END
print("")

# You can use some operators with string
n = name
n2 = " is handsome"
print(n+n2)
print(n*3+n2)
print("")

# There are a lot of BUILT-IN functions for STRINGS
# len() is one of the most used ones
print("The length of n is", len(n))
print("The length of n + n2 is ", len(n+n2))
print("")

# Slicing = taking bits and pieces of strings
# STRING[start, stop] including start and EXCLUDING END
print(n[1:3])
print(n[2:])  # From second character to the end
print(n[::2])  # In STEPS of 2
print(n[::-1])  # Reversed string

# strings CAN be COMPARED returning a T or F value
print(n == n2)
print(n > n2)  # Here we are comparing alphabetically
# UPPERCASE letters are smaller than LOWERCASE letters
print("")
print('z' > 'a')  # Z is greater than A in value (24th letter)
print('A' > 'z')
print("")

# You can take a substring and check whether it is in the string
print("ber" in n)
print("xx" in n)
print("")

# A method is called by appending = string_value.method()
print(n.lower())
print(n2.capitalize())
print("The number of characters for n is: ", n.count(" "))
b = n+n2
print("Now we will replace As for $s: ", b.replace("a", "$"))
print(b.split())
print("")

# Parsing strings using string methods
s = "http://google.com and http://bing.com y tambien http://okdiario.es"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:  # This means that is has reached the end of string
        break  # escape gateway
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end
print("")

# STRINGS ARE IMMUTABLE, YOU CANNOT CHANGE THEM
# n = 'Alberto' if i try: n[2] = "x", ERROR

# FORMAT OPERATOR %s, %d (integer), %g (float), %x (hexadecimal)
# It allows us to construct new strings by replacing parts of
# the original string with the data stored in variables
template = "Today is %s"
print(template)
template = template % "Tuesday"
print(template)
# If there are more than one format sequence, the arguments must
# be placed between ()
template = "Today is %s, day number %d"
print(template)
template = template %("Friday", 28)
print(template)
print("")

# FILES
# to open a file_object = file_object.open(f_name) [predetermined (r)]
# to open a file .open("name", [r; w (write = from scratch);
# x (exclusive creation); a (append = add); b (binary); t (text);
# + (read & write)]
