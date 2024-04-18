import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5500/stock.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#태그로 찾는 방법, title, get_text(), text, a.attrs, a["href"]
#class로 찾는 방법

# print(soup)
#print(soup.find(attrs={"class":"box_type_l"}))
# print(soup.find("tr",attrs={"class":"type1"}))
type_tr = soup.find("tr",{"class":"type1"})#클래스로 찾는방법
print("1st th: ",type_tr.th) # 제일 처음 만난 th를 찾음
print("all th: ",type_tr.find_all("th"))# 모든 th

ths = type_tr.find_all("th")
for th in ths:
    print("제목: ",th.text) # ths들 중에서 th의 text부분만 가져온다