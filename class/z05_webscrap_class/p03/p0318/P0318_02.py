class Car:  #   명사, 동사에 따라 형태구분
    car_name = ""
    color = ""
    door = 0
    length = 0
    width = 0
    speed = 0   #   함수로 정의
    def up_speed(self,s):   # 클래스 내부의 함수는 self 필수
        self.speed += s

c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = "white"
c1.door = 5
c1.length = 2000
c1.width = 1400
c1.up_speed(60) #   현재속도"0"에서 60을 더해줌 > "60"
c1.up_speed(40) #   현재속도는? 100 #누적
c1.up_speed(50) #   현재속도는? 150 #누적
c1.speed = 50   #   현재속도는? 50  #새롭게 정의됨  #   직접변경
# color = "red"
# speed = 60
# #   철수의 차 1대 생산
# car_name = "드뉴아반떼"
# color = "white"
# door = 5
# length = 2000
# width = 1000
# speed = 0

# color = "red"
# speed = 60

# print("철수 차: ",car_name,color,door,length,width,speed)

# #   영희의 차 1대 생산, color: 그린, speed: 100, 나머지 동일

c2 = Car()
c2.car_name = "드뉴아반떼"
c2.color = "green"
c2.door = 5
c2.length = 2000
c2.width = 1400
c2.up_speed(100)

# car_name = "드뉴아반떼"
# color = "green"
# door = 5
# length = 2000
# width = 1000
# speed = 100

# print("영희 차: ",car_name,color,door,length,width,speed)

# #   디올뉴그랜저, 화이트펄, 길이: 2500, 폭: 1400, speed: 150
c3 = Car()
c3.car_name = "디올뉴그랜저"
c3.color = "화이트펄"
c3.door = 5
c3.length = 2500
c3.width = 1400
c3.up_speed(150)
# car_name = "디올뉴그랜저"
# color = "화이트펄"
# door = 5
# length = 2500
# width = 1400
# speed = 150

# print("반장 차: ",car_name,color,door,length,width,speed)
print("철수: ",c1.car_name,c1.color,c1.color,c1.door,c1.length,c1.width,c1.speed)