import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://www.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem = browser.find_element(By.ID,'query')
elem.send_keys('네이버 항공권')
elem.send_keys(Keys.ENTER) #input박스에서 enter키 입력

# Keys.PAGE_DOWN
browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
#for문 응용
for c in range(0,5):
    browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
time.sleep(100)

'''
1. 네이버 페이지 이동
2. 검색창 네이버 항공권 입력
3. 검색창 엔터키 입력
--네이버 항공권 검색 이동
4. 네이버항공권 클릭
--네이버 항공권 페이지 이동
5. 출발지역 선택: 김포
6. 도착지역 선택: 제주
7. 가는날 오는날 선택
8. 항공권 검색 버튼 클릭
9. 검색대기
10. 스크롤 이동
11. 13만원 이하 저장'''