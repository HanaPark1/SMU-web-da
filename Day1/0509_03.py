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
    #print(res.text)
    soup = BeautifulSoup(res.text,"lxml")
    #print(soup.title)
    #print(soup.header.div.a.attrs) #태그 속성값 출력
    #print(soup.header.div.a['href']) #태그 속성값 하나 출력
    #print(soup.header.div.a['class']) #태그 속성값 하나 출력
    
    ## find() 해당 태그를 검색할때 사용. 해당 태그의 속성값을 가지고 검색 가능
    #data1 = soup.find("header.div.a", attrs={"class":"ofhd_float_back"})
    #print(data1)
    #data2 = soup.find("h2", id = "title_area")
    #print(data2)
    #print(data2.get_text())
    
    ##find() 1개만 검색, find_all() 복수개를 검색
    ul_data = soup.find("ul",{"class":"ranking_list"})
    li_datas = ul_data.find_all("li",{"class":"rl_item"});
    print(len(li_datas))
    for li_data in li_datas:
        print(li_data.find("p",{"class":""}))
    
    
else:
    print("실패")
    print(res.status_code)