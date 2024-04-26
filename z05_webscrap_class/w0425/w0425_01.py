import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "http://naver.com"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#요소선택
elem = browser.find_element(By.NAME,"query")
elem.send_keys('네이버항공권')
elem.send_keys(Keys.ENTER)

elem = browser.find_element(By.CLASS_NAME,"link_name")
elem.click()
time.sleep(3)

#원본창[0], 새창[1], 그다음 새창[2]
browser.switch_to.window(browser.window_handles[-1])
#출발도착 가는날오는날 2명 항공권검색
# time.sleep(10000)
elem = browser.find_element(By.CLASS_NAME,'start')
elem.click()#출발  
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF')
elem.send_keys('김포')
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_search_item__2WRSw')
elem.click()#김포클릭
time.sleep(3)

time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'end')
elem.click()#도착             
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_input__1vVkF')
elem.send_keys('제주')
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_search_item__2WRSw')
elem.click()#제주클릭
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,'select_Date__1aF7Y')
elem.click()# 가는날 선택
time.sleep(3)

#출발일자 도착일자#######################################################################
elem = browser.find_elements(By.TAG_NAME,'table')[1]
elem = elem.find_elements(By.TAG_NAME,'button')[14]
elem.click()#출발일자             
time.sleep(3)
elem = browser.find_elements(By.TAG_NAME,'table')[1]
elem = elem.find_elements(By.TAG_NAME,'button')[15]
elem.click()# 일자             
time.sleep(3)



time.sleep(100)