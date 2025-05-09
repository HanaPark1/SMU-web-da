import requests
from bs4 import BeautifulSoup

# 쿠팡 접근해서 res.text 출력

#res = requests.get("https://www.daum.net/")

#url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
#url = "https://www.daum.net/"
url = "https://n.news.naver.com/article/018/0006008786?ntype=RANKING"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
if res.status_code == 200 :
    print("성공")
    print(res.status_code)
    print(res.text)
else:
    print("실패")
    print(res.status_code)