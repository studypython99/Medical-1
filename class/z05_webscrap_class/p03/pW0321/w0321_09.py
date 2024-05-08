import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%93%B1%EC%B4%8C%EC%A3%BC%EA%B3%B5+%EB%B6%84%EC%96%91"
headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# with open("jugong.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())

#   매매시세, 전세시세 출력  

real = soup.find("ol",{"class":"list_place"})  #    등촌주공의 위치
li_list = real.find_all("li") #li = 주공 3,5,10단지
print(len(li_list)) #   3

for i in range(len(li_list)):

    #   단지이름
    title = li_list[i].find("div",{"class":"wrap_tit"}).a.text.strip()
    print(title)

    #   매매, 전세시세
    dd_list = li_list[i].find_all("dd",{"class":"f_red"})   #매매시세,전세시세
    print("매매시세: ",dd_list[0].text)
    print("전세시세: ",dd_list[1].text)
    print("_"*50)
print("종료")
