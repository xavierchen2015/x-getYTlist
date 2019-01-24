import requests
import os
import configparser
from bs4 import BeautifulSoup
 
config = configparser.ConfigParser()
config.read('x.ini')
xUrl = config.get('Config', 'URL')

r = requests.get(xUrl)

if r.status_code == requests.codes.ok:
  
    soup = BeautifulSoup(r.text, 'html.parser')
    stories = soup.find_all("a", {"class":"yt-uix-sessionlink"})
  
    xlist = []
    for s in stories:
        #print("網址：" + s.get('href'))

        if "/watch" in s.get('href'):
            xlist.append(s.get('href'))

#print(xlist)
#print(len(xlist))
allList = set(xlist)
print(allList)
#print(len(allList))

if os.path.exists("xx.txt"):
    os.remove("xx.txt")
else:
    print("The file does not exist")

for l in allList:
    p = open('xx.txt', 'a+')
    p.write('https://www.youtube.com'+l +"\n")
    p.close()

