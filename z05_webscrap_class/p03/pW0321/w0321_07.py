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
samsung = tr_list[2]
td_lsit = samsung.find_all("td")    #td를 모두 들고온다.
print(td_lsit[10])





# #   2,3,4,5,6 하면 1,2,3,4,5등
# print("순위\t종목\t\t검비\t현재가")

# print("_"*50)
# # print(sk_list)

# for i in range(2,7):
#     jj = tr_list[i]
#     jj_list = jj.find_all("td")
# # print("_"*50)
# # print(jj_list[1].a.text)
#     # jj_list[i-1].text
#     #jj_list[i-1].find("a",{"class":"tltle"}).text
#     print(  jj_list[i-2].text,
#             jj_list[i-1].a.text,
#             jj_list[i].text,
#             jj_list[i+1].text)






