import re 

f = open("grams_clusters.txt")
data = f.readlines()

def lengths():
    
    lens = []
    for line in data:
        l = re.split(r":|\s", line)
        i = int(l[2])
        if int(i/10) not in lens:
            lens.append(int(i/10))
    lens.sort()
    print(lens)

def clus(k):
    
    cl = open("clusters/" + str(k) + "_groups.txt", "w")

    for line in data:
        l = re.split(r":|\s", line)
        i = int(l[2])
        if int(i / 10) == k:
            cl.write(l[0] + "\n")
        

    cl.close()
    f.close()
