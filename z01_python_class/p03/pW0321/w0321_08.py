import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# print(soup)
#   url 주소의 자료를 soup를 이용해서 text 글자 출력
#-----------------------
# soup에서 find 찾는다 <div class=
s_all = soup.find("div",{"class":"box_type_l"})
with open("stock_list","w",encoding="utf8") as f:
    f.write(soup.prettify())
tr_list = s_all.find_all("tr")  #tr 모두를 들고온다. / 3번째에 삼성전자가 나옴
tr_list[0]
print(tr_list[0].find_all("th"))
title_list = []
for tr in tr_list[0]:
    if tr.text.strip() != '':
        title_list.append(tr.text.strip())
    #   select("tr th") 바로 원하는 위치까지 찾아간다.
print(title_list)
print("_"*50)

print(tr_list[0].th.text.strip(),end="\t")
for i in range(2,15):
    stock = tr_list[i]
    # print(stock)
    # stock = tr_list[2]
    td_lsit = stock.find_all("td")    #td를 모두 들고온다.
    if len(tr_list) <= 1:
        pass
    for j in range(0,12):
        if 5<j<10:
            pass 
        print(td_lsit[j].text.strip(),end="\t") # text만 뽑아온다.










