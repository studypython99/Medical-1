import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

#selenium 자동화 프로그램

browser = webdriver.Chrome()
browser.get("https://news.naver.com/main/ranking/popularDay.naver")
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")

#뉴스 가져오기
officeCard = soup.find("div","_officeCard _officeCard0")
ranks = officeCard.find_all("div","rankingnews_box")
print("갯수: ",len(ranks))
for i in ranks:
    lis = i.find_all("li")
    print("제목: ",lis[0].find("a","list_title").text)
    print("-"*50) # 각 뉴스사별 상위 뉴스제목 가져오기





# newss = soup.find("ul","rankingnews_list").find_all("li")
# for i in newss:
#     print("-"*50)
#     print("번호: ",i.find("em","list_ranking_num").text)
#     print("제목: ",i.find("div","list_content").text)
#     print("-"*50)
