import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#화면대기함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)
#요소선택 xpath-By, XPATH, class-By, CLASS_NAME, id-By.ID, name-By.NAME
#requests, BeautifulSoup: find,find_all
#selenium: find_element, find_elements
#XPATH ex): '//b[text()="국내"]' >> '국내'를 검색
#           //b[contains(text(),"국")] >>'국'에 해당하는 내용 모두 검색
#           //b[@class="send"], //b[@class="send"]

#출발지 선택
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]') #텍스트로 찾는방법
elem.click()
time.sleep(1)

#국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')#// 모든페이지에서 찾아주세요
elem.click()
time.sleep(1)

#김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(), "김포국제공항")]')#// 모든페이지에서 찾아주세요
elem.click()
time.sleep(1)

#도착지 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
elem.click()
time.sleep(1)

#국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')#// 모든페이지에서 찾아주세요
elem.click()
time.sleep(1)

#제주 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
elem.click()
time.sleep(1)

#가는날 선택
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]')
elem.click()
time.sleep(1)

#날짜 선택, 여러개 elements 14일을 선택, 월마다 14일이 존재함;
#가는날 
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
time.sleep(1)
elem[1].click() #1번째 14일이 선택됨
time.sleep(1)
#오는날
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
time.sleep(1)
elem[1].click() #1번째 14일이 선택됨
time.sleep(1)

#인원선택
elem = browser.find_element(By.XPATH,'//button[contains(text(),"성인")]')
elem.click()
time.sleep(1)
#인원추가
elem = browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]')
elem.click()
time.sleep(1)

#항공권 검색
elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
elem.click()#한번하면 인원선택창 사라짐
time.sleep(1)
elem.click()#두번째에 검색창 누름
time.sleep(10)#검색시간이 꽤 있음;;
#화면대기함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#최대 30초까지 대기, 모든 요소가 위치에 도달할때 까지
# elem = WebDriverWait(browser,30).until
# (EC.presence_of_all_elements_located
#  (By.XPATH,'//div[@class=""]'))@@@
# elem.send_keys(Keys.PAGE_DOWN)

##화면 스크롤 내리기
#현재높이
prev_height = browser.execute.script("return document.body.scrollHeight")
print("최초높이: ",prev_height)
#스크롤 이동
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    #현재높이, 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break #같으면 중단
    prev_height = curr_height

input("Enter키 입력시 종료")
#창 닫기
browser.quit()


time.sleep(100)






# elem = browser.find_element(By.CLASS_NAME,"link_name")
# elem.click()
# time.sleep(3)

# #원본창[0], 새창[1], 그다음 새창[2]
# browser.switch_to.window(browser.window_handles[-1])
# #출발도착 가는날오는날 2명 항공권검색
# # time.sleep(10000)
# elem = browser.find_element(By.CLASS_NAME,'start')
# elem.click()#출발  
# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF')
# elem.send_keys('김포')
# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_search_item__2WRSw')
# elem.click()#김포클릭
# time.sleep(3)

# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'end')
# elem.click()#도착             
# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF')
# elem.send_keys('제주')
# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'autocomplete_search_item__2WRSw')
# elem.click()#제주클릭
# time.sleep(3)
# elem = browser.find_element(By.CLASS_NAME,'select_Date__1aF7Y')
# elem.click()# 가는날 선택
# time.sleep(3)

# #출발일자 도착일자
# elem = browser.find_elements(By.TAG_NAME,'table')[1]
# elem = elem.find_elements(By.TAG_NAME,'button')[14]
# elem.click()#출발일자             
# time.sleep(3)
# elem = browser.find_elements(By.TAG_NAME,'table')[1]
# elem = elem.find_elements(By.TAG_NAME,'button')[15]
# elem.click()# 일자             
# time.sleep(3)
# #######################################################################


# time.sleep(100)