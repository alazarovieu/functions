def fun(text_file):
    f = open(text_file)
    signs = [",", ".", ":", ";", "!", "?", '"', "'", ".", "...", "???", "[", "]", "\n"]
    words = list()
    for line in f:
        for sign in signs:
            line = line.replace(sign, "")
        line_words = line.split()
        for word in line_words:
            length = 0
            for i in word:
                length += 1
            if length == 3 and word[0] == "b" and word not in words:
                words.append(word)

    print(words)


fun("HarryPotter copy.txt")
