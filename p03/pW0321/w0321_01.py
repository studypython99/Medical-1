import requests
#   웹에 접근해서 html소스를 가져옴
# res = requests.get("https://www.google.com/")
res = requests.get("https://www.melon.com/index.htm")
#   200: 정상 / 403,404: 페이지 없음 / 500: 프로그램에러
print(res)  #   코드상태: <Response [200]> 정상
print(type(res))    #   <class 'requests.models.Response'>


if res.status_code == requests.codes.ok:
    print("정상출력")
else:
    print("접근 불가",res.status_code)
    
print("코드: ",res.status_code) #상세코드를 출력해서 알려줌
res.raise_for_status() # 코드가 200이 아니면 예외처리해서 자동멈춤

print("-"*40)
print(len(res.text))   
print(res.text) #   텍스트의 내용을 모두 가져온다