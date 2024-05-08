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
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
# 1. 야놀자 홈페이지 이동
url = "https://www.yanolja.com/search?tab=place"
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,'lxml')

# 2. 검색창에 호텔 입력
elem = browser.find_element(By.CLASS_NAME,"SearchInput_input__342U2")
elem.send_keys("호텔")
elem.send_keys(Keys.ENTER)
time.sleep(5)
# 3. 날짜선택

# 4. 6월 5일,6일 클릭
# 5. 확인버튼 클릭
# 6. 검색창 클릭 > enter키 입력
# 7. 검색 진행
# 8. 스크롤 이동 반복
# 9. 정보창이 뛰워지면, 이미지,제목,평점,평가수,금액 저장하시오.
#이미지 url[28:] 28번부터 끝까지, loc = url.find("http") // print("위치값:", loc)
#http의 위치를 항상 확인가능
# yanolja 테이블
# yno,img,title,grade,grade_num,price