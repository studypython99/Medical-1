import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
# F9 = reddot
#크롬브라우저 열기
browser = webdriver.Chrome()
url = "https://www.naver.com/"
#네이버 페이지 이동
browser.get(url)
time.sleep(3)
#로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
elem.click()
time.sleep(random.randint(2,5))

#js구문
input_js = 'document.getElementById("id").value="{id}";\
            document.getElementById("id").value="{pw}";\
            '.format("aaa","111")#s네이버 idpw
time.sleep(random.randint(2,5))

#js명령어 실행
browser.execute_script(input_js)
#아이디 입력창 선택
elem = browser.find_element(By.ID,'id')
#아이디 입력
elem.send_keys("aaa")
#비밀번호 입력창 선택
elem = browser.find_element(By.ID,'pw')
#비밀번호 입력
elem.send_keys("1111")

#로그인버튼
elem = browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(100)