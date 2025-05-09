import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.naver"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text,"lxml")

data = soup.find("div",{"class":"box_type_l"})

trs =data.tbody.find_all("tr")
# print(trs[2])
# for i in range(10):
#     # print(i)
#     # print(trs[i])
#     print(trs[i].find_all("td"))
    
# .find_all("a",{"class":"title"})
print(trs)
# print(trs[6].find_all("td"))