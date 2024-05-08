import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5500/stock.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})#클래스로 찾는방법

trs = type_tr.find_next_siblings("tr")
print("find_next_siblings: ",trs[1].a["href"]) #/item/main.naver?code=005930

t_table = soup.find("table",{"class":"type_5"})
print("class:type_5:",t_table.a["href"]) #/item/main.naver?code=005930