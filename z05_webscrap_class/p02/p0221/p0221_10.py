#   변수 3개를 만들어서 name, city, fruit
#   아래와 같이 출력해보세요
#   저의 이름은 name 입니다.
#   저는 city에서 태어났습니다.
#   저는 fruit을 좋아합니다.

# p0221_04.py 파일 참고 github
# a=input("이름은?")
# b=input("도시는?")
# c=input("좋아하는 과일은?")
# print("저의 이름은",a,"입니다")
# print("저는",b,"에서 태어났습니다.")
# print("저는",c+"을(를) 좋아합니다.")

# a=input("이름은?")
# b=input("도시는?")
# c=input("좋아하는 과일은?")
# print('{}은 {}를 좋아하고 {}에 살아요."'.format(a,c,b))

# 변수 선언
name="홍길동"
city="부산"
fruit="딸기"

# 출력 input() > 내가 입력한 값을 변수로 사용한다.
name=input("이름은?")
city=input("사는곳은?")
fruit=input("좋아하는 과일은?")
print('저의 이름은',name,'입니다.')
print('저는',city+'시에서 태어났습니다.')
print('저는',fruit+'를 좋아합니다.')