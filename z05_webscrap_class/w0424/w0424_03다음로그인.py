import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://www.daum.net/"
#크롬브라우저 열기
browser = webdriver.Chrome()
#다음페이지 이동
browser.get(url)
time.sleep(3)
#로그인 버튼 선택
elem = browser.find_element(By.CLASS_NAME,'btn_login')
elem.click()
time.sleep(random.randint(2,5))
#아이디입력
elem = browser.find_element(By.CLASS_NAME,'tf_g')
elem.click()
time.sleep(random.randint(2,5))
#비번입력
elem = browser.find_element(By.CLASS_NAME,'btn_login')
elem.click()
time.sleep(random.randint(2,5))

time.sleep(100)