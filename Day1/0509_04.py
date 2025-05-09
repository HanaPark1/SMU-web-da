import requests
from bs4 import BeautifulSoup

# url=""
# headers=""
# res = requests.get(url, headers=headers)
# soup = BeautifulSoup(res.text, "lxml")

with open("Day1/a.html","r",encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# print(soup.title.get_text())
# print(soup.h2)
# print(soup.find_all("h2"))
# print(soup.find("p",{id:"p1"}))
print(soup.find("div",{"class":"c2"}).find("ul").find("li"))
print(soup.find("ul").find_all("li")[1].get_text())
print(soup.find("div",{"class":"c2"}).find("ul").get_text())