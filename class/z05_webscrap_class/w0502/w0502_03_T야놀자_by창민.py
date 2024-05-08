import oracledb
import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
def sleep():
    time.sleep(random.random() + 1)
def longsleep():
    time.sleep(random.random() + 3)
# scrolling
def scroll():
    prev_height = browser.execute_script('return document.body.scrollHeight')
    browser.execute_script(f'window.scrollTo(0, {prev_height})')
    time.sleep(3)
# db 연결
def connection():
    user = "ORA_USER"
    pw = "1111"
    dsn = "localhost:1521/xe"
    return oracledb.connect(user=user, password=pw, dsn=dsn), oracledb.connect(user=user, password=pw, dsn=dsn).cursor()
conn, cursor = connection()
path = os.getcwd() + '\web_study\w0425\\'
# url = path + 'h2.html'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language':'ko,en;q=0.9,en-US;q=0.8'}
browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://www.yanolja.com/'
# url = 'https://www.yanolja.com/search/%ED%98%B8%ED%85%94?keyword=%ED%98%B8%ED%85%94&searchKeyword=%25ED%2598%25B8%25ED%2585%2594'
browser.get(url)
sleep()
# 정보 입력
elem = browser.find_element(By.CLASS_NAME, 'HomeSearchBar_searchBoxBorder__2xBZt')
elem.click()
sleep()
elem = browser.find_element(By.CLASS_NAME, 'SearchInput_input__342U2')
elem.send_keys('호텔')
sleep()
elem = browser.find_element(By.CLASS_NAME, 'NavFilterButton_container__20Hr2')
elem.click()
sleep()
elem = browser.find_elements(By.XPATH, '//td[text()="5"]')[1]
elem.click()
sleep()
elem = browser.find_elements(By.XPATH, '//td[text()="6"]')[1]
elem.click()
sleep()
elem = browser.find_element(By.CLASS_NAME, 'DateRangePicker_rangePickerConfirmButton__2c41H')
elem.click()
sleep()
elem = browser.find_element(By.CLASS_NAME, 'SearchInput_buttonSubmit__3D83k')
elem.click()
sleep()
# 스크롤 10번 반복
for _ in range(10):
    scroll()
# 데이터 크롤링
datum = browser.find_elements(By.CLASS_NAME, 'PlaceListItemText_container__fUIgA')
for data in datum:
    img = data.find_element(By.CLASS_NAME, 'PlaceListImage_imageText__2XEMn').get_attribute('style')
    img_url = img.split('"')[1]
    name = data.find_element(By.CLASS_NAME, 'PlaceListTitle_text__2511B').text
    rate = data.find_element(By.CLASS_NAME, 'PlaceListScore_rating__3Glxf').text
    cnt = data.find_element(By.CLASS_NAME, 'PlaceListScore_reviewInfo__3QSCU').text.replace('(', "").replace(')', "").replace(",", "")
    try:
        price = data.find_element(By.CLASS_NAME, 'PlacePriceInfoV2_discountPrice__1PuwK').text.replace(",", "")
    except:
        price = 0
    print(img_url, name, rate, cnt, price)
    print('-' * 50)
    # db에 저장
    sql = f"insert into yanolja values(yanolja_seq.nextval, '{img_url}', '{name}', '{rate}', '{cnt}', '{price}')"
    cursor.execute(sql)
cursor.execute('commit')
print('입력 완료')
#db 연결 종료
conn.close()
#브라우저 종료
browser.quit()