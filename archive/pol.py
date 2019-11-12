import re

f = open("pol")
data = f.readlines()
 
d = {}
o = open("clusters.txt", "w")
last = ''
for line in data:
    words = re.split(r'\t', line)
    if len(words) > 1:
        words = re.split(r' ', words[1])
        if len(words) > 1:
            if words[1]!=last:            
                if words[1][0] not in "aeiouAEIOU":
                    w = re.split(r'[aeiouyąęó]', words[1])
                    #o.write(words[1] + " " + w[0] + "\n")
                    if w[0] not in d.keys():
                        d[w[0]] = 1
                    else:
                        d[w[0]] = d[w[0]] + 1
                last = words[1]
        else:
            if words[0] != last:  
                if words[0][0] not in "aeiouAEIOU":
                    w = re.split(r'[aeiouyąęó]', words[0])
                    #o.write(words[0] + " " + w[0] + "\n")
                    if w[0] not in d.keys():
                        d[w[0]] = 1
                    else:
                        d[w[0]] = d[w[0]] + 1
                last = words[0]

for x in d.keys():
    o.write(x +": " + str(d[x]) + "\n")                
o.close()

