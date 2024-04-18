import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5500/stock.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

type_tr = soup.find("tr",{"class":"type1"})#클래스로 찾는방법

print("th: ",type_tr.th)
print("find_next_sibling: ",type_tr.th.find_next_sibling("tr"))