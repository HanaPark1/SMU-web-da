import requests
from bs4 import BeautifulSoup

with open("Day1/게시판3.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# data = soup.find("div",{"id":"input"}).find("div").get_text()
# print(data)

trs = soup.find("thead").find_all("th")
for tr in trs:
    print(tr)