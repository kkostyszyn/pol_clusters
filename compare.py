import re

def ratio(x, y):
    if x == "u":
        x = u_total
        x_c = u_comp
    elif x == "n":
        x = n_total
        x_c = n_comp
    elif x == "j":
        x = j_total
        x_c = j_comp
        
    if y == "u":
        y = u_total
        y_c = u_comp
    elif y == "n":
        y = n_total
        y_c = n_comp
    elif y == "j":
        y = j_total
        y_c = j_comp
        
    for i in x_c:
        if i in y_c:
            print(i + ": " + str((x_c[i]/x)/(y_c[i]/y)))

#open all files
#U are files from Ryan Cotterel's Unimorph project, using conjugated and declined forms to find
#clusters that may not appear in lemma form
u_file = open("pol_clusters.txt")
u = u_file.readlines()

#This corpus is from internet posts made in 2008 and totals over 10 million unique tokens. 
n_file = open("grams_clusters.txt")
n = n_file.readlines()

#Finally, bigrams from Jarosz's child derived speech corpus, which needs modification to remove
#affricates and rewrite retroflex as post-alveoar, etc.
j_file = open("jar_clusters.txt")
j = j_file.readlines()

u_comp = {}
u_total = 0
for line in u:
    i = re.split(r":|\s", line)
    u_comp[i[0]] = int(i[2])
    u_total += int(i[2])

j_comp = {}
j_total = 0
for line in j:
    i = re.split(r":|\s", line)
    if 'ʂ' in i[0]:
        i[0] = re.sub('ʂ', 'ʃ',i[0])
    if 'ʐ' in i[0]:
        i[0] = re.sub('ʐ', 'ʒ',i[0])  
    if 'ɡ' in i[0]:
        i[0] = re.sub('ɡ', 'g',i[0])  
    j_comp[i[0]] = int(i[1])
    j_total += int(i[1])

n_comp = {}
n_total = 0
for line in n:
    i = re.split(r":|\s",line)
    n_comp[i[0]] = int(i[2])
    n_total += int(i[2])
    
c = open("comparison.txt", "w")

found = False
alph = n_comp.keys()
alph = list(alph).sort()
for i in sorted(n_comp):
    txt = i + ",\n\tNGRAM: " + str(n_comp[i]) + " (" + str(n_comp[i] / n_total) + "%), "
    if i in u_comp:
        found = True
        txt = txt + "\n\tUNI: " + str(u_comp[i]) + " (" + str(u_comp[i] / n_total) + "%), "
    else:
        txt = txt + "\n\tUNI: 0, "
    if i in j_comp:
        found = True
        txt = txt + "\n\tJAROSZ: " + str(j_comp[i]) + " (" + str(j_comp[i] / n_total) + "%)\n"
    else:
        txt = txt + "\n\tJAROSZ: 0\n"
    if found:
        c.write(txt)
    found = False
