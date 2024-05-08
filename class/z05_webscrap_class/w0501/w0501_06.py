import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
#브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

for i in range(5):
    url = f"https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-24&checkOut=2024-06-28&personal=2&freeForm=true&page={i+1}"
    browser.get(url)

    # 데이터 찾기
    soup = BeautifulSoup(browser.page_source,"lxml")
    
    
    
    # hotels = soup.find("a","gc-thumbnail-type-seller-card css-wels0m")
    # print("전체 갯수: ",len(hotels))
    
    #################################################
    title = soup.find_all("h3","gc-thumbnail-type-seller-card-title css-1asqkxl")
    locate = soup.find_all("span","css-1rzfout")
    point = soup.find_all("span","css-9ml4lz")
    people = soup.find_all("span","css-oj6onp")
    price = soup.find_all("span","css-5r5920")
    img = soup.find("img")["src"]
    for idx,(a,b,c,d,e,f) in enumerate(zip(title,locate,point,people,price,img)):
        print("페이지번호: ",i+1)
        print("호텔번호: ",idx+1)
        print("호텔: ",a.text)
        print("위치: ",b.text)
        print("평점: ",c.text)
        people = int(d.text[:-4].replace(",",""))
        print("평점인원: ",people)
        price = int(e.text.replace(",",""))
        print("가격: ",price)
        print("이미지: ",img)
        print("-"*50)
    time.sleep(1)
    
#     sql = f'''
#     insert into yeogi values (yeogi_seq.nextval,'{title}','{locate}','{point}','{people}','{img}','{price}')
#     '''
#     cursor.execute(sql)

# cursor.execute("commit")
# cursor.close()
# conn.close()

