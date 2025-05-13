import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import csv
import time


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 티 안 나게
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# 브라우저 실행
browser = webdriver.Chrome(options=options)

# 페이지 접속
url = "https://www.naver.com/"
browser.get(url)
time.sleep(2) # 페이지 로딩 대기 -> 읽어오는 시간이 필요하기 때문에 필요

# elem = browser.find_element(By.CLASS_NAME,"MyView-module__naver_logo____Y442")
# elem.click()

elem = browser.find_element(By.ID,"query")
elem.send_keys("네이버 로그인")
time.sleep(2)

#엔터클릭이벤트
elem.send_keys(Keys.ENTER)

#클릭이벤트
elem = browser.find_element(By.CLASS_NAME,"logo_slogan")
elem.click()
time.sleep(2)

#크롬브라우저 탭을 처음으로 이동
browser.switch_to.window(browser.window_handles[0])

# 뒤로가기
browser.back()
time.sleep(2)
browser.back()




input("프로그램 종료 엔터>>>>>")