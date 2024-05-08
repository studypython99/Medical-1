#     관계연산자
#     어떤것이 크거나 작거나 같은지를 비교
#     참은 True, 거짓은 False로 표시
#     주로 조건문, 반복문에서 사용.
#     수식1 == 수식2: 수식1과 2가 같은지 평가
#     수식1 != 수식2: 수식1과 2가 다르다 ( !는 not의 표현)
print(3==6) #False
print(3!=6) #True

#     수식1 > 수식2: 등호평가 (>작은가, >=작거나 같은가)

num=95
print(num>90)     #True
print(num<=90)    #False
print(num==90)    #False
print(num!=90)    #True

print(90 <=num<100)

#     논리연산자
#     and, or, not 세가지가 있다.
#     and 둘다 참이어야 참
#     or 둘중 하나라도 참이면 참
#     not 참이면 거짓, 거짓이면 참
kor=90
avg=90
print(kor>80)     #     True
print(avg>90)     #     False
print(kor>80 and avg>90)      #False, T and F = F
print(kor>80 or avg>90)       #True, T and F = T
print(not avg>=90)
