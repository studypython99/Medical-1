import requests # 웹 정보, 소스 가져오는 라이브러리
#기본구문 3줄 url,res,res.raise_for_status()
url = "http://www.google.com"
res = requests.get(url)
res.raise_for_status()#에러코드 발생시 프로그램을 종료.
#res = requests.get("http://www.melon.com")
# print(res.status_code) # 200
# print(res) # Respnse [200] : 정상

#if res.status_code == requests.codes.OK: # 응답코드: 200 ??
if res.status_code == 200: # 응 200 같은말
    print("정상적인 페이지 호출")
else:
    print("접근할 수 없음 [에러코드: ",res.status_code,"]") # 멜론 406번
    