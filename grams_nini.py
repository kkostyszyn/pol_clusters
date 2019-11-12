import re

f = open("grams")
data = f.readlines()

o = open("grams.txt", "w")
last = ''

for line in data:
    words = re.split(r'\t', line)
    o.write(words[0] + "\n")

o.close()
