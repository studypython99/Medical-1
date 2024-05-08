import requests
url="http://www.google.com"
res = requests.get(url)
res.raise_for_status()

print("현재 페이지의 글자수: ",len(res.text))
print("웹페이지 소스코드: ",res.text) #타입: str
#파일저장
with open("google1.html","w",encoding="utf8") as f: # 실행해야 파일이 생긴다
    f.write(res.text)