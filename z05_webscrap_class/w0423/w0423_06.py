# https://jumin.mois.go.kr/ageStatMonth.do


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

# 서울, 인천, 경기도 3개의 인수를 웹스크랩, 합계
people = 0
table_p = soup.find("table","tbl_type1").find_all("tr")
for idx, i in enumerate(table_p):
    if (idx == 4 or idx == 7 or idx == 12):
        print("지역: ",i.find("td","td_admin th1").text)
        print("인구수: ",i.find("td",{"title":"2024년 03월 / 계"}).text,"명")
        people += int(i.find("td",{"title":"2024년 03월 / 계"}).text.replace(",",""))
        print("-"*50)
print("인구 합계: ",format(people, ','),"명")