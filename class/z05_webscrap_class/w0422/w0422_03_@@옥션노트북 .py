import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())
# with open("auctionNB.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
####################################################################################
#이름 평점 평가수 가격 사진

# print(soup.find("div",{"id":"section--inner_content_body_container"}))
print('-'*50)
section = soup.find("div",{"id":"section--inner_content_body_container"}) # 내용 전체묶음
# print(section.find("div",{"class","section--itemcard"}))
print('-'*50)
#복수개 찾기 find_all
itemcards = section.find_all("div",{"class","section--itemcard_info"}) # 내용 각각의 위치
print('-'*50)
print(itemcards[2].text)
print('-'*50)
for i, itemcard in enumerate(itemcards[0:10]): # 10번째까지
    print('-'*50)
    print("[",i+1,"번째]")
    print("이름: ",itemcard.find("span",{"class","text--title"}).text)
    #2,900,000 > 2900000 이렇게 변환, replace함수: replace(",","") 쉼표를 없앤다
    price = int((itemcard.find("strong",{"class","text__price-seller"}).text).replace(",","")) 
    print("금액: ",itemcard.find("strong",{"class","text__price-seller"}).text)
    
    #후기평점, 구매건수
    list_score = itemcard.find("ul",{"class","list--score"})
    lis = list_score.find_all("li")
    print("li갯수: ",len(lis))# 0~3까지,, 후기,평점,구매
    if len(lis)==0:
        print("후기평점, 구매건수: 없음")
    elif len(lis)==1:
        buycnt = int(lis[0].find("span",{"class","text--buycnt"}).text[3:])
        print("구매건수: ",buycnt)
    else: # li가 3개 있는 경우
        for_ally = float(list_score.find("span",{"class","for-a11y"}).text[5:-1])   # 숫자로 형변환
        print("후기평점: ",for_ally)
        buycnt = int(lis[2].find("span",{"class","text--buycnt"}).text[3:])
        print("구매건수: ",buycnt)
    print('-'*50)
    
    
    
    
    
    
    
    
    # if itemcard.find("ul",{"class","list--score"}).text =="":
    #     print("후기평점: 없음")
    # else:
    #     list_score = itemcard.find("ul",{"class","list--score"})
    #     if list_score.find("span",{"class","for-a11y"}).text[5:-1] != "":
    #     #후기평점 4.9 이상
    #         for_ally = float(list_score.find("span",{"class","for-a11y"}).text[5:-1])   # 숫자로 형변환
    #         if for_ally > 4.5:
    #             print("후기평점: ",for_ally)
    #         else:
    #             print("후기평점: 미달")
    #     else:
    #         print("후기평점: 없음")
        

        
    #     #구매건수비교
    #     buycnt = int(list_score.find("span",{"class","text--buycnt"}).text[3:])
    #     if buycnt >2:
    #         print("구매건수: ",buycnt)
    #     else:
    #         print("구매건수: 미달")
        

        
        




# nb_div = soup.find("div","itemcard").find_all("div","section--itemcard_info_major")
# # print(nb_div)
# print("상품명: ",nb_div("span","text--title"))
# print("가격: ",nb_div("strong","text__price-seller"))