import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
#print(res.text)
soup = BeautifulSoup(res.text,"lxml")
with open("test.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
print("-"*50,"soup.title.text")
print(soup.title.text)      #soup 태그 사용해서 text글자를 출력
print("-"*50,"soup.a")
print(soup.a)               # soup 태그사용
print("-"*50,"attrs")
print(soup.a.attrs)         # soup a태그의 속성값 모두 출력
print("-"*50,"href")
print(soup.a["href"])       # soup a태그 선택속성값 출력
                            # a태그 링크태그 a 이하의 페이지로 이동하라.
print("-"*50,"soup.div")
print(soup.div)             #특정검색으로 찾기  <div id="wrap">
print("-"*50,"footer")
print(soup.find("div",attrs={"id":"footer"}))   #   soup에서 find태그, 속성 모두를 출력

