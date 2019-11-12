import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

alpha = {
    'B': 51,
    'C': 46,
    'D': 60,
    'F': 30,
    'G': 38,
    'H': 23,
    'J': 17,
    'K': 96,
    'L': 27,
    'M': 60,
    'N': 69,
    'P': 199,
    #'Q': 1, -?
    'R': 62,
    'S': 111,
    'T': 46,
    #  V: 2 -?
    'W': 87,
    #X: 1-?
    'Z': 78 }
    
al = {'B' : 51}

#entries start at line 385-409-454 for all entries? what about partial pages?
#how to turn beautifulsoup into writable string? 

url = "https://sjp.pwn.pl/sjp/lista/"
#tag = "B;2"
url2 = ".html"

count = 0 
for x in alph.keys():
    f = open("pwn_" + x + ".txt", "w")
    for i in range(alpha[x]):
        print(url + x + ";" + str(i+1) + url2)
        website = requests.get(url + x + ";" + str(i+1) + url2)
        #webContent = response.read()
        soup = BeautifulSoup(website.content)
        """
        wc = soup.readlines()
        while count < 454:
            if count > 385:
                f.write(str(wc))
            count += 1
        count = 0    
        """
        f.write(str(soup))

