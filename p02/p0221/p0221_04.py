
print("안녕하세요 제 이름은 홍길동입니다.")
print("저는 21살 입니다.")

#홍길동 > 이순신, 21 > 30 으로 변경
print("안녕하세요 제 이름은 이순신입니다.")
print("저는 30살 입니다.")

print("안녕하세요 제 이름은","홍길동","입니다")
print("저는", 21,"살 입니다.")

name="홍길동" #다양하게 사용 가능하다
age=21
print("안녕하세요 제 이름은",name,"입니다")
print("저는",age,"살 입니다.")

#   변수 입력
str1="hello"
print(str1)
var1=2
print(var1)
str2="world"
print(str1,str2)
print(str1+str2) #띄어쓰기 없다
print(str1+' '+str2) #띄어쓰기 있다

var4=100
var3=var4 # 모두 100
var2=var3
var1=var2
print("var1 :", var1)
var4=200
print("var4 :", var4)
print("var1 :", var1)
# var4 는 바뀌었지만 순차연산은 하지않는다

#   변수를 이용해서 다음 문장을 출력해보세요
#   변수명: fruit
#   "포도", "딸기", "수박"순으로 입력
fruit1="포도"
fruit2="딸기"
fruit3="수박"
print(fruit1,fruit2,fruit3) #   띄어쓰기o
print(fruit1+fruit2+fruit3) #   띄어쓰기x
#   출력문장 >> 나는 포도를 좋아합니다.
print("나는",fruit1+"를 좋아합니다.")

#   변수명: city
#   출력할 문장: 나는 서울시에 살고 있습니다.
city="서울시"
print("나는",'('+city+')'+"에 살고 있습니다.")

#   변수명: animal
#   출력할 문장: (판다)가 제일 좋아요
animal="판다"
print('('+animal+')'+"가 제일 좋아요.")