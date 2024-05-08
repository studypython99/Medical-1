import requests
from bs4 import BeautifulSoup
url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text,"lxml")


movie_list = soup.find("ol",{"class":"movie_list"})

# print(movie_list)   #   ol에 대한 내용만 있다.
m_list = movie_list.find_all("li")

for i,m in enumerate(m_list):
    if i == 5: break
    print(f"번호 {i+1}")
    print("-"*50)
    img_screen = m.find("img")["data-original-src"]
    print(m.find("img")["data-original-src"])
    #   파일로 저장하기. 열기 쓰기 닫기
    #   파일열기
    with open(f"movie_{i}.jpg","wb") as f: #텍스트가 아니라서 인코딩 필요없다
        re_img=requests.get(img_screen)
        f.write(re_img.content) #파일이름의 내용을 저장
print("개수: ",len(m_list))