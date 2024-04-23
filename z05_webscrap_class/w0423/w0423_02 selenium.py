import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

#selenium 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
# with open("webtoons2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")
webtoon = soup.find("ul","AsideList__content_list--FXDvm AsideList__challenge--HeKuU").find_all("li")
print("-"*50)
print(webtoon)
for i in webtoon:
    print("-"*50)
    title = i.find("span","ContentTitle__title--e3qXt").text
    print("순위: ",i.find("strong","AsideList__ranking--sNPZy").text)
    print("제목: ",i.find("span","ContentTitle__title--e3qXt").text)
    print("작가: ",i.find("a","ContentAuthor__author--CTAAP").text)
    print("이미지: ",i.find("img","Poster__image--d9XTI")['src'])
    # 이미지 추출하기
    img_url = i.find("img","Poster__image--d9XTI")['src']
    img_poster = requests.get(img_url, headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"})
    with open("webtoons_{}.jpeg".format(title),"wb") as img:
        img.write(img_poster.content)
    print("-"*50)
#requests로 정보 가져오기
# url="https://comic.naver.com/bestChallenge"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# res = requests.get(url,headers=headers)
# res.raise_for_status
# soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# with open("webtoons1.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())
# print("완료!")
