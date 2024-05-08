ss = "파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다"
#   count()   존재하는 문자가 몇번 나왔는지 확인
print(ss.count("공부"))         #   2   있을 때
print(ss.count("자바"))         #   0   없을 때

#   find()  존재하는 문자열의 위치값 출력
print(ss.find("공부"))          #   4(0,1,2,3,4)위치
print(ss.find("자바"))          #   없을 때 -1
print(ss.find("공부",7))          #   문자열 7 >> 시작위치

print(ss.rfind("공부"))         #   r오른쪽부터(뒤에서부터) 찾는다

#   find와 비슷하지만 없을 때 에러가 표시된다
print(ss.index("공부"))         #   
print(ss.index("공부"))         #   
# print(ss.index("자바"))          #  없을 때 에러표시 error

#   시작하는 문자열이
print(ss.startswith("파이썬"))   #   맞으면 True
print(ss.startswith("자바"))   #   틀리면 False

#   끝나는 문자열이
print(ss.endswith("않습니다"))  #맞으면 True


