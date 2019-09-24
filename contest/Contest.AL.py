file=open("text.txt", "r")
counter=0
vowels="aeiou"
alphabet=" abcdefghijklmnopqrstuvwxyz"
text=""

for line in file:
    counter=0
    for c in line:
        if c in vowels:
            counter+=1
    text = text + alphabet[counter]

print(text)