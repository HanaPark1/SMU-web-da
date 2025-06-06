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

time.sleep(3)

soup = BeautifulSoup(broswer.page_source,"lxml")

## 페이지 저장
with open("Day2/melon1.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())

## 페이지 읽어오기
with open("Day2/melon1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")