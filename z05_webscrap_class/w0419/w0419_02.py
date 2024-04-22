import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# with open("google1.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
####################################################################################
#print(soup)
best_div = soup.find("div","best-list")

#1번상품
li01 = best_div.find("li")
print("li01 순위: ",li01.p.text)# 1
print("제목: ",li01.find("a","itemname").text)
print("가격: ",li01.find("div","s-price").strong.text)

#1~n번 상품
lis = best_div.find_all("li")
print("갯수: ",len(lis))
for li in lis[:4]:
    
    print("순위: ",li.p.text)# 1
    print("제목: ",li.find("a","itemname").text)
    print("가격: ",li.find("div","s-price").strong.text)
    print('-'*50)

# item = best_div.next()
# for i in item:
#     if i.find
#     print(i.text)
# print('-'*50)

#     if i.find("td","no"):
#         # filter: 조건을 만족하는 경우에만 가져온다, map: 각 요소마다 적용 >>>모두 list로 감싸준다
#         tr_list=list(filter(lambda x : x.text.strip() != '', i.find_all('td'))) #텍스트가 없다면 가져오지 않겠다. 리스트의 요소 하나하나 적용시킴
#         tr_list=list(map(lambda x : x.text, tr_list))# 텍스트만 추출
#         tr_list=list(map(lambda x : x.strip(), tr_list))# 추출한 데이터의 공백을 제거