import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# DB연결부분
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# ;;; 한 페이지만 가능함;; 후.... 하나 열고 하나 닫고 3번 반복
for j in range(3):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
    browser = webdriver.Chrome()
    browser.maximize_window()
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={j+1}&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
    browser.get(url)
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source,"lxml")

    ul = soup.find("ul","search-product-list")
    print(len(ul))
    lis = ul.find_all("li")
    for i in lis:
        print("페이지번호: ",j+1)
        title = i.find("div","name").text
        print("제목: ",title)
        img = i.find("img")["src"]
        print("이미지: ",img)
        price = int(i.find("strong","price-value").text.replace(",",""))
        print("금액: ",price)
        
        if i.find("span","star") == None: # 평점이 없으면 pass
            pass
        else:
            grade = float(i.find("span","star").text) # 아니면 표시,
            print("평점: ",grade)
            if i.find("span","rating-total-count").text[1:-2] =="":
                    pass
            else:
                eval_num = int(i.find("span","rating-total-count").text[1:-2]) # 평점은 있는데, 평가인원이 없을 수 있다;; 무슨말이지;;
                print("평가수: ",eval_num)

        print("-"*50)
        browser.quit() # 너무 느림...;;

'''
if itemcard.find("ul",{"class":"list--score"}).text == "":
    print("후기평점 : 없음")
else: 
    list_score = itemcard.find("ul",{"class":"list--score"})
    # 후기평점 4.9점 이상 출력
    if list_score.find("span",{"class":"for-a11y"}).text[5:-1] != "":
        for_a11y = float(list_score.find("span",{"class":"for-a11y"}).text[5:-1])
        if for_a11y > 4.5:
            print("후기평점 : ",for_a11y )
        else:
            print("후기평점 : 미달")
    else:
        print("후기평점 : 없음")        
'''
'''
[ 2. 쿠팡 - 노트북   ]
검색 - 노트북으로 해서
총 1,2,3페이지 까지 검색해서
콘솔에 출력하고, db에 저장하시오.
- coupang 테이블
cno 시퀀스
title 문자타입(100)
img 문자타입(100)
price 숫자타입(10)
grade 숫자타입(10)
eval_num 숫자타입(10)
제목, 이미지, 금액, 평점, 평가수'''