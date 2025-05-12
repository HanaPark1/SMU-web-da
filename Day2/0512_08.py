from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import csv

# 크롬 옵션 설정
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# 브라우저 실행
broswer = webdriver.Chrome(options=options)

url = "https://www.melon.com/chart/index.htm"
broswer.get(url)

time.sleep(3)

soup = BeautifulSoup(broswer.page_source,"lxml")

ff = open(f"Day2/images/result/melon_chart.csv","w",encoding="utf-8",newline="")
writer = csv.writer(ff)
# 1~100등
# 순위 제목 가수  좋아요 이미지링크
# 1   너닿 10cm 59060 http;;;
# 좋아요 총 개수: 합계
# 파일 melon1~100.jpg

data = soup.find("tbody")
trs = data.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    rank = tds[1].find("span",{"class":"rank"}).get_text() #순위
    title = tds[5].find("div",{"class":"rank01"}).a.get_text() #제목
    singer = tds[5].find("div",{"class":"rank02"}).a.get_text() #가수
    like = tds[7].find("span",{"class":"cnt"}).get_text().strip()[3:].strip() #좋아요
    like = int(like.replace(",",""))
    imgUrl = tds[3].img["src"] #이미지 링크
    print(f"{rank}, {title}, {singer}, {like}, {imgUrl}")
    img_res = requests.get(imgUrl)
    with open(f"Day2/images/melon_chart{rank}.jpg","wb") as f:
        f.write(img_res.content)
    
    song = [rank,title,singer,like]
    writer.writerow(song)
    

ff.close()        
input("종료 엔터>>")