import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%EB%8B%AC%EB%9F%AC+%ED%99%98%EC%9C%A8&oq=&gs_lcrp=EgZjaHJvbWUqCQgAECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxBFGDsYwgPSAQg2ODlqMGoxNagCCLACAQ&sourceid=chrome&ie=UTF-8"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
with open("google1.html","w",encoding="utf8") as f:
    f.write(soup.prettify())
####################################################################################

#환율 1달러 가져오기
title = soup.find("div","b1hJbf")
print(title.text)
#해당태그 출력
print("tag_all: ",soup.find("input","lWzCpb ZEB7Fb"))
print('-'*50)
#해당태그의 속성값 모두 출력
print("value_all: ",soup.find("input","lWzCpb ZEB7Fb").attrs)
print('-'*50)
#해당태그의 특정속성값(value) 1개 출력
print("value_select: ",soup.find("input","lWzCpb ZEB7Fb")["value"])
print('-'*50)