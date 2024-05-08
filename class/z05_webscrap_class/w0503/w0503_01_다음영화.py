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

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
for j in range(3):
    url = f"https://search.daum.net/search?w=tot&q={2023-j}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source,"lxml")

    #역대 영화
    #이미지, 
    # 제목 strong tit-g clamp-g, 
    # 누적관객수 p conts-desc clamp-g, 
    # 날짜 span conts-subdesc clamp-g
    #2023,22,21,20
    #콘솔에 출력, DB에 저장
    #daum_movie 테이블
    ul = soup.find("ul","c-list-basic ty_flow35")
    lis = ul.find_all("li") #페이지당 10개씩 
    for i in lis:
        print(f"{2023-j}년도")
        img = i.find("img")["src"]
        print("이미지: ",img)
        title = i.find("strong","tit-g clamp-g").text
        print("제목: ",title)
        audience = int(i.find("p","conts-desc clamp-g").text.replace(",","")[3:-3])*10000
        print("누적관객: ",audience)
        ddate = i.find("span","conts-subdesc clamp-g").text.replace(".","-")[0:-2]
        print("날짜: ",ddate)
        print("-"*50)
        sql = f'''
        insert into daum_movie values(dno_seq.nextval,'{title}','{img}','{audience}','{ddate}')
        '''
        cursor.execute(sql)
cursor.execute('commit')
cursor.close()
conn.close()

'''
dno 시퀀스
title varchar2(100),
img varchar2(100),
audience number(10)
ddate date
with open(f"movie_{i}.jpg","wb") as f:
re_img = requests.get(img_screen) #url링크를 다시 읽어와야 함.
f.write(re_img.content) # 파일이름의 내용을 저장
'''