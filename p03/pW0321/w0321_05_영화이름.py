import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text,"lxml")
with open("movie_name","w",encoding="utf8") as f:
    f.write(soup.prettify())

movie_list = soup.find("ol",{"class":"movie_list"})

# print(movie_list)   #   ol에 대한 내용만 있다.
m_list = movie_list.find_all("li")
name_list = soup.find_all('div',{"class":"info_tit"})
# print(name_list)
# movie_name = []
# for i, m in enumerate(m_list):
#     name = m.find("div",{"class":"info_tit"}).a.text
# #     movie_name.append(name)
# # print(movie_list)





for name in name_list[:len(m_list)]:    #영화갯수만큼까지 가져오겠다.
    print(name.get_text().strip(""),end=",")
# print(name)