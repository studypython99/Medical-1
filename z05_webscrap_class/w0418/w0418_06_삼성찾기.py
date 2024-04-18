import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5500/stock.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
#삼성 가져오기
t_table = soup.find("table",{"class":"type_5"})
#print(t_table)
trs = t_table.find_all("tr")
#print(trs) # 리스트[]형태로 tr을 모두 찾아줌
tds = trs[2].find_all("td") #trs[2]삼성이 있는 모든 td를 찾아주세요.
for td in tds:
    print(td.text.strip(),end="\t") #tds의 text만 찾아주세요.
