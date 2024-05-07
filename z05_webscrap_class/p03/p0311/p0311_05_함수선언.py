#   함수선언
def plus(n1,n2):    #   def plus/함수이름 (n1,n2)/매개변수
    result = 0
    result = n1 + n2
    print("결과값: ",result)
    
plus(10,20) #   함수호출, 매개변수가 2개면, 2개가 들어와야한다. 
plus(1,2) #   함수이름(매개변수 개수를 맞춰야한다.)

#   함수를 사용하지 않는다면, 이런식으로 반복한다.
n1,n2 = 10,20
result = 0
result = n1 + n2
print("결과값: ",result)

n1,n2 = 1,2
result = 0
result = n1 + n2
print("결과값: ",result)

n1,n2 = 10,20
result = 0
result = n1 + n2
print("결과값: ",result)