import requests
from bs4 import BeautifulSoup #웹의 형태를 html로 변경
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

print(type(res.text)) #<class 'str'>

soup = BeautifulSoup(res.text,"lxml")#text를 html로 파싱
print(type(soup))

print("<title>: ",soup.title)#태그를 입력
print("<title> text: ",soup.title.get_text())#태그의 글자를 가져옴.
print("<title> text: ",soup.title.text)#태그의 글자를 가져옴.
print("<a> : ",soup.a)#태그의 글자를 가져옴.
print("<a> : ",soup.a.attrs)#속성값 모두 가져옴

print("<a>[속성]: ",soup.a["href"])#태그의 1개 속성 가져옴
