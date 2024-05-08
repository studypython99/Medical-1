import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/bestChallenge"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#전부 볼 수 없다, 동기,비동기식이 혼합되어 구성됨; requests는 동기식 ajax는 비동기식
with open("webtoon.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
