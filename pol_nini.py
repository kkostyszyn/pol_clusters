import re

f = open("pol")
data = f.readlines()

o = open("pol.txt", "w")
last = ''

for line in data:
    words = re.split(r'\t', line)
    if len(words) > 1:
        words = re.split(r' ', words[1])
        if len(words) > 1:     
            if words[1]!=last:  
                o.write(words[1] + "\n")  
                last = words[1]
        else:
            if words[0] != last:
                o.write(words[0] + "\n")  
                last = words[0]


o.close()
