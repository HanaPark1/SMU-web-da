import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import random

## 웹스크래핑 -- Beautiful
with open("Day4/ya1.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")
    
## 검색된 리스트 전체
data = soup.find("div",{"class":""})
