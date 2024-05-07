'''
역대 관객순
year    title   num     평점
2019 극한직업   1626    3.6
2020    남산의 부장들   475     3.5
2021    모가디슈    361     3.6
2022    범죄도시2   1269    3.5
2023    서울의 봄   1312    4.1
'''
data = {
    'year':[]
}
import pandas as pd
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
list1 = []
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
for i in range(5):
    url = f"https://search.daum.net/search?w=tot&q={2023-i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(1)

    soup = BeautifulSoup(browser.page_source,'lxml')
    title = soup.find("strong","tit-g clamp-g").text.replace(" ","")
    print(title)
    # list1.append(title)
    count = soup.find("p","conts-desc clamp-g").text.replace(",","")[3:-3]
    print(count)
    # list1.append(count)
    browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[1]/c-thumb/div/a').click()
    time.sleep(1)
    #원본창[0], 새창[1], 그다음 새창[2]
    browser.switch_to.window(browser.window_handles[-1])
    
    #평점 가져오기
    soup = BeautifulSoup(browser.page_source,'lxml')
    point = soup.find("span","gem-star-point").text[2:5]
    print(point)
    list1.append([2023-i,title,count,point])
    time.sleep(1)
    browser.back()
    time.sleep(1)
print(list1)

# selenium
# elem = browser.find_element(By.XPATH,'//span[text()=""]')
# browser.find_elements(By.XPATH,'//button[@class=""]')
# elem.click(), 
# elem.send_keys('시가총액')
# elem.send_keys(Keys.ENTER) 

#list 타입 저장
