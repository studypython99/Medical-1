import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/search?keyword=%ec%97%ac%ed%96%89&itemno=&nickname=&frm=ho[…]&arraycategory=&encKeyword=%ec%97%ac%ed%96%89&f=c:24010000"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# print(soup.prettify())
# with open("auction.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
####################################################################################
#이름 평점 평가수 가격 사진
hotel = soup.find("div","component component--item_card type--general")
# print(hotel)
print("상품명: ",hotel.find("span","text--title").text)
print("가격: ",hotel.find("strong","text__price-seller").text)
print("후기평점: ",hotel.find("span","for-a11y").text)