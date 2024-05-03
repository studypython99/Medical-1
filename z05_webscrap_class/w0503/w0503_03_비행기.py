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
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
browser.get(url)
time.sleep(1)

soup = BeautifulSoup(browser.page_source,"lxml")

ul = soup.find("ul","search-product-list")
print(len(ul))
lis = ul.find_all("li")
for i in lis:
    print(i.text)
    print("-"*50)
    
'''
[ 3. 네이버 항공권 ]
- 웹스크래핑을 통해
- 6/26 ~ 6/27
- 항공사 출발시간 도착시간 소요시간 금액을
- db에 저장하시오.
- db에서
- 항공사별 그룹핑해서 출력하시오.
- 시간 검색기능을 구현하시오.
( 출발하려는 시간을 입력하세요. >> )
- 시간을 입력하면 입력된 시간 이후로 검색
- 없으면 검색한 데이터가 없다고 나옴.
* flight 테이블
fno - 숫자타입(4) 시퀀스
airline - 문자타입(100)
departure_time - 날짜타입
arrival_time - 날짜타입
flight_time - 문자타입(20)
price - 숫자타입(10)'''