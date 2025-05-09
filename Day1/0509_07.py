import requests
from bs4 import BeautifulSoup

with open("Day1/게시판3.html","r", encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
# 태그 출력
# 속성 출력
#find(), find_all()