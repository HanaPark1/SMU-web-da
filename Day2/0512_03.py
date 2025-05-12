import requests
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
           "Referer": "https://www.coupang.com/"}

res = requests.get(url, headers=headers)
res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# data = soup.find("tbody")
print(res.text)
