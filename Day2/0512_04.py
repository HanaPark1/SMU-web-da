import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

input("키보드 클릭")