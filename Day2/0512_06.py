from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

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

time.sleep(5)

soup = BeautifulSoup(broswer.page_source,"lxml")
data = soup.find("tbody")
trs = data.find_all("tr")

for tr in trs:
    tds = tr.find_all("td")
    for td in tds:
        rank = td.find("span",{"class":"rank"}.get_text().strip())
        print(rank)

input("종료시 엔터>>>")