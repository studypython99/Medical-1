import requests
url="http://www.melon.com"
#나는 파이썬이 아니라 이거야
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
#res = requests.get("http://www.melon.com")
res = requests.get(url,headers=headers)
res.raise_for_status()

# with open("user_agent.html","w",encoding="utf8") as f:
#     f.write(res.text)