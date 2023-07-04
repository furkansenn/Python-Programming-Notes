import requests
from bs4 import BeautifulSoup

link="https://www.imdb.com/chart/top/"

baglan=requests.get(link)

kod=baglan.content

parser=BeautifulSoup(kod,"html.parser")

tr=parser.find("tbody",{"class":"lister-list"}).findAll("tr")

for i in tr:
    baslık=i.find("td",{"class":"titleColumn"}).find("a").string
    print(baslık)



