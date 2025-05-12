import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver?&page=1"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

data = soup.find("tbody")
trs = data.find_all("tr")

# print(trs[2].get_text())

for tr in trs:
    tds = tr.find_all("td")
    if len(tds) <= 1:
        continue
    for i,td in enumerate(tds):
        if i==3:
            em1 = td.find("em").get_text().strip()
            span1 = td.find("span",{"class":"tah"}).get_text().strip()
            print(em1 + span1)
            continue
        print(td.get_text().strip(),end="\t")
    print()
    print("-"*50)
#     print(td.get_text(),end="\t")
