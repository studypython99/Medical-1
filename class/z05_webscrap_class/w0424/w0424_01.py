import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

url = "http://google.com"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#파일에서 가져오기1
# with open("google.html","w",encoding='utf8') as f:
#     f.write(soup.prettify())

#파일에서 가져오기2
# page = open('google.html','r',encoding='utf8')    
# soup = BeautifulSoup(page,'lxml')
# page.close()

print("타이틀: ",soup.find("title"))