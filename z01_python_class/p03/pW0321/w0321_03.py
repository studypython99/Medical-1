import requests
# User-Agent 사용방법

#   들어가려는 사이트주소
# res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/#google_vignette")
url = "https://www.melon.com/index.htm"

#   어디를 통해서 들어오는지, 파이썬인지 크롬인지, 여기서는 크롬이라고 설정해준다
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
print("코드: ",res.status_code)
res.raise_for_status()
print(res.text)



# with open("a1.html","w",encoding="utf8") as f:
#     f.write(res.text)   #   python-requests/2.31.0 이렇게 바뀜
# print("파일이 저장되었습니다.")