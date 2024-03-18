#   class: 사용자 정의 변수, 함수도 포함
#           설계도에 한번 선언해주고, 가져와서 사용한다.
class Car:      #   첫글자 대문자를 사용하세요. Car
    color = "white"
    door = 5
    length = 4710
    width = 1800
    displace = 1600
    speed = 0

def upspeed(self, sp) :    #   함수
    self.speed += sp
    
def downspeed(self,sp):
    self.speed -= sp
    
#   ex)자동차 생산: 객체선언c1을 할 때마다 제품(Car)이 한개씩 생산
c1 = Car()  #   클래스 객체선언, Car클래스에 있는 모든 변수를 사용하겠다.
print(c1.color)
print("전 색상 : ",c1.color)    #   white
c1.color = "red"
print("후 색상: ",c1.color)    #   red
c2 = Car()
print("색상: ",c2.color)    #   white
c2 = Car()
c2 = Car()

a_l1 = 4710
a_w1 = 1800
a_d1 = 1600

a_l2 = 4710
a_w2 = 1800
a_d12 = 1600

a_l3 = 4710
a_w3 = 1800
a_d13 = 1600