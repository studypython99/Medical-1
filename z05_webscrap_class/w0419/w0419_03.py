import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# with open("cupang.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
####################################################################################
#제목 가격 평점 평점카운트

nb_ul = soup.find("ul","search-product-list")
# print(nb_ul.text)
# li01 = nb_ul.find("div","name")
# print("노트북 이름: ",li01.text)

# li01 = nb_ul.find("em","sale")
# print("가격 : ",li01.text.strip())

# li01 = nb_ul.find("em","rating")
# print("평점 : ",li01.text)

# li01 = nb_ul.find("span","rating-total-count")
# print("평점인원 : ",li01.text)


nb_ul = soup.find("ul","search-product-list").find_all("li")# ul위치를 잡아주고/ 그 아래 li를 가져온다
for idx, li in enumerate(nb_ul[:20]):
    if "search-product__ad-badge" in li["class"]:   #   광고상품 문구가 클래스에 있니?
        continue                                    #   있으면 안녕~
    
    #평점 5.0 이상, em:str,, 따라서 float적용으로 실수
    if float(li.find("em","rating").text) < 5.0:
        continue
    print("번호: {}".format(idx+1))
    print("노트북 이름: ",li.find("div","name").text.strip())
    print("가격 : ",li.find("em","sale").text.strip())
    if(li.find("em","rating") is not None): #평점이 없는경우 is not None: 예외처리
        print("평점 : ",li.find("em","rating").text) # 있으면 참
    else:
        print("평점없음")
    #평점인원 200명 이상인 경우만 출력
    if int(li.find("span","rating-total-count").text[1:-1]) < 200:
        continue
    print("평점인원 : ",li.find("span","rating-total-count").text.replace('(', '').replace(')', '')+'명')
    print('-'*50)
