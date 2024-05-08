import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 파일에서 가져오기
with open("flight1.html","r",encoding='utf8') as f:
    soup = BeautifulSoup(f, 'lxml')
# 287개 항공권 조회
flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("항공권 개수 : ",len(flights))
print("-"*40)
airline_name = flights[0].find("b",{"class":"airline_name__Tm2wJ"})
print("항공사 : ",airline_name.text.strip())
route_times = flights[0].find_all("b",{"class":"route_time__-2Z1T"})
print("출발시간 : ",route_times[0].text.strip())
print("도착시간 : ",route_times[1].text.strip())
air_price = flights[0].find("i",{"class":"domestic_num__2roTW"})
print("가격 : ",air_price.text.strip())

# for문 287개 출력
# 100,000원 이하만 출력될수 있도록 하시오.
for i , flight in enumerate(flights):
    air_price = int(air_price.text.strip().replace(",",""))
    air_price = flight.find("i",{"class":"domestic_num__2roTW"})
    air_price_int = int(air_price.text.strip().replace(",",""))
    if (air_price_int > 100000):
        print("10만원 이상인 항공권")
        continue
    print((i+1),"번째")
    airline_name = flight.find("b",{"class":"airline_name__Tm2wJ"})
    print("항공사 : ",airline_name.text.strip())
    route_times = flight.find_all("b",{"class":"route_time__-2Z1T"})
    print("출발시간 : ",route_times[0].text.strip())
    print("도착시간 : ",route_times[1].text.strip())
    air_price = flight.find("i",{"class":"domestic_num__2roTW"})
    print("가격 : ",air_price.text.strip())
    print("-"*40)
    "abc".replace()