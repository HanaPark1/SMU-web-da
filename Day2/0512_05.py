import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv
import time
# 셀레니움 크롬자동화 프로그램
# user-agent 변경
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64),\
   Accept-Language: ko-KR,ko;q=0.9,Referer: https://www.coupang.com/')
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",\
#                      "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
browser = webdriver.Chrome(options=options)
browser.maximize_window()
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
# 셀레니움 크롬자동화 프로그램
# browser = webdriver.Chrome()
# browser.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent")
input("종료시 엔터>> ")