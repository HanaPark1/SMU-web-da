import requests
from bs4 import BeautifulSoup
import csv

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

ff = open("Day1/stock_info.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(ff)
ths = soup.thead.find_all("th")

fileName = []
# for th in ths:
#     print(th.get_text(),end="\t")
    # fileName.append(th.get_text())
    
tds = soup.tbody.find_all("td")
for td in tds:
    print(td.get_text(), end='')
    fileName.append(td.get_text())
    
writer.writerow(fileName)

ff.close
print("파일 저장 완료")