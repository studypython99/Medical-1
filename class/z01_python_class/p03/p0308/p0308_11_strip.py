#   자바, 스크립트에도 같이 쓰인다.

#   strip() 공백제거(양쪽 모두)
ss = "apple은 당도가 높고, apple은 빨강 녹색이 있다."
s1 = " 파이썬"
s2 = "파이썬"
s3 = "파        이썬"   #   사이에 있는 공백은 x

#   replace 대체하다, 문자열을 다른 문자열로 대체한다.
print(s3.replace(" ",""))       #   공백 제거
print(s3.replace("파","하"))    #   글자 변경
print(ss.replace("apple","사과"))    #   글자 변경

if s1.strip() == s2:
    print("yes")
else:
    print("no")
    
#   lstrip()    왼쪽 공백제거
s1 = "      파이썬"
s2 = "파이썬"

if s1.lstrip() == s2:
    print("yes")
else:
    print("no")


#   rstrip()    오른쪽 공백제거
s1 = "파이썬       "
s2 = "파이썬"

if s1.rstrip() == s2:
    print("yes")
else:
    print("no")
    
# s_input = input("현재 배우는 과목은 >>").strip()    #   스페이스 실수 방지

news = "정용진 신세계그룹 총괄부회장이 8일 회장 자리에 올랐다. 2006년 부회장에 오른 후 18년 만에 이뤄진 승진 인사다. 지난해 이마트 창립 이후 적자를 기록했고, 신세계그룹 매출이 감소하는 등 사업 환경이 악화하면서 위기 극복을 위한 새로운 리더십을 내세웠다."
print(news.strip())
print(news.replace(" ",""))
print(news.replace("그룹","group"))
