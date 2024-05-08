import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

#selenium 자동화 프로그램

browser = webdriver.Chrome()
url = "http://www.naver.com"
#브라우저 페이지 열기
browser.get(url)
# id = "query"
#네이버 로그인 클릭, 뒤로가기, 새로고침
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem .click()
time.sleep(3)
browser.back() #뒤로가기 browser.forward() 앞으로가기
browser.refresh() # f5 새로고침

#네이버 검색부분에 검색어 send_keys("주식")입력
# elem = browser.find_element(By.ID,'query')
# elem #선택되어 있는 elem요소를 보여줌
# elem.send_keys("주식")

# soup = BeautifulSoup(browser.page_source,"lxml")