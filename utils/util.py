file = open("utils\\test.txt")
text = file.read()
file.close()
text = text.strip().split()
write = ""
for idx, element in enumerate(text):
    write += "\"" + text[idx] + "\","

file = open("utils\\test.txt", "w")
file.write(write)
file.close()
