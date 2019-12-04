# DICTIONARIES LOOK LIKE LISTS
d = {'one': 'uno', 'two': ' dos', 'three': 'tres'}
# d[1] will give an ERROR because there IS NOT AN ORDER
# IT IS LIKE A HASH-MAP, 1 Key = 1 value, multiple keys can have the same value
print(d['two'])
print("")

# IT IS ITERABLE
for n in d:
    print(d[n])

# it is MUTABLE
d["four"] = "cuatro"
print(d)
del(d["two"])
print(d)
print("")

# YOU CAN HAVE A DICTIONARY OF DICTIONARIES
dictionaries = {"spanish": {'one': 'uno', 'dos': 'two'}, "german": {'one': 'ein', 'two': 'zwei'}}
print(dictionaries["german"]["two"])
dictionaries["german"]["three"] = "drei"
print(dictionaries["german"])
print("")

# IN can be used to check whether a value exists or not. RETURNS TRUE OR FALSE
print("Portuguese" in dictionaries)
print("")

# keys() to retrieve an iterable list of all the keys
print(dictionaries.keys())
print("")

# get() to get a value
print(d.get("three", "NO value"))
print(d.get("two", "NO VALUE"))
print("")

