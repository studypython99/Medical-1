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

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source,"lxml")
trs = soup.find_all("tr")[1:] # 등수 한줄
for tr in trs:
    td = tr.find_all("td") # 한줄 내용 123567
    #1.순위
    rank = int(td[1].find("span","rank").text)
    print("순위: ",rank)
    #2.변동순위
    v_rank = td[2].find("span","rank_wrap").text
    if "단계 하락" in v_rank:
        v_rank = int(td[2].find("span","rank_wrap").text.split('단계 하락')[1].strip())
        print("변동순위 1: ",v_rank)
        print("변동순위: ",int(v_rank)*-1)
    elif "단계 상승" in v_rank:
        print("변동순위 2: ",v_rank)
        v_rank = int(td[2].find("span","rank_wrap").text.split('단계 상승')[1].strip())
        print("변동순위: ",int(v_rank))
    else:
        print("변동순위 3: ",v_rank)
        v_rank = ''
        print("-") #변동없음
    # print("변동순위: ",td[2].find("span","rank_wrap").text)
    #3.이미지
    img = td[3].find("img")["src"]
    print("이미지: ",img)
    #4.제목
    title = td[5].find("a").text.replace("'", '`') # 제목에 ' 가 들어가있는걸 `로 바꿔준다
    print("제목: ",title)
    #5.가수
    singer = td[5].find("span","checkEllipsis").text
    print("가수: ",singer)
    #6.좋아요
    likenum = int(td[7].find("span","cnt").text.split("총건수")[1].strip().replace(",", ""))# 총건수제거,[1]숫자부분 공백제거,콤마제거
    print("좋아요: ",likenum)
    print("-"*50)
    # for i in td:
    #     print("-"*50)
    #     print(i.text.replace(" ",""))
    #     print("-"*50)
    # find, find_all
    
    sql = f'''
    insert into melon values(melon_seq.nextval,
    '{rank}',nvl('{v_rank}',0),'{img}','{title}','{singer}','{likenum}') 
    '''# nvl: null값을 0으로 변경
    cursor.execute(sql)
cursor.execute('commit')
cursor.close()
conn.close()

# 1. 야놀자 홈페이지 이동
# 2. 검색창에 호텔 입력,
# 3. 날짜선택
# 4. 6월 5일,6일 클릭
# 5. 확인버튼 클릭
# 6. 검색창 클릭 > enter키 입력
# 7. 검색 진행
# 8. 스크롤 이동 반복
# 9. 정보창이 뛰워지면, 이미지,제목,평점,평가수,금액 저장하시오.
# yanolja 테이블
# yno,img,title,grade,grade_num,price