import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://watcha.com/browse/webtoon"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#화면스크롤 내리기
#현재스크롤 높이검색
prev_h = browser.execute_script("return document.body.scrollHeight")
print("최초높이: ",prev_h)
#스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    #재 조정된 스크롤 높이
    curr_h = browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    if prev_h == curr_h:
        break
    prev_h = curr_h # 스크롤 한번 내리고 시작점을 다시 잡아준다
    
#데이터 찾기    
soup = BeautifulSoup(browser.page_source,"lxml")
sections = soup.find_all("section","custom-11ytuur e1134x5i3")

time.sleep(100)