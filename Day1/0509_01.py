## 웹스크래핑 라이브러리 설치
# pip install requests
# pip install beautifulsoup4
# pip install lxml

import requests

# 사이트를 접속하여 html 소스 가져옴
# res = requests.get("https://www.naver.com/")

#파이썬에서 웹스크래핑 -> 웹접근 제한을 진행
res = requests.get("https://www.melon.com/") #접근제한

if res.status_code == 200:
    print("정상 프로그램 진행")
    print(res)
    print("응답 코드: ",res.status_code)
    res.raise_for_status() #에러시종료
    # print(res.text)
else:
    print("프로그램 종료")
