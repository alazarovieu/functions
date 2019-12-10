from pathlib import Path

try:
    filename = Path("/Users/alazarov/PycharmProjects/IN_CLASS_HW/HarryPotter.txt")
    print("File found!")
    f = open(filename)
    new_f = open("hangManDictionary.txt", "a")

    signs = [",", ".", ":", ";", "!", "?", '"', ")", "(", ".", "...", "???", "[", "]", "\n"]
    dictionary = list()

    for line in f:
        for sign in signs:
            line = line.replace(sign, "")
        line_words = line.split()
        for word in line_words:
            word = word.lower()
            length = 0
            for i in word:
                length += 1
            if length > 3 and word[-1] != "," and word not in dictionary:
                dictionary.append(word)

    for word in dictionary:
        new_f.write(word + "\n")

    print("Done!")
except FileNotFoundError:
    print("Could not find the file you are looking for...")


