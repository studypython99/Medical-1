#   자바같은 경우, 매개변수 개수에 따라 다른 함수 일정
#   파이썬 이름은 무조건 달라져야 함

# def func1(num1,num2,num3):     #   함수 이름이 같으면 안됨
#     print(num1)
# def func2(num1,num2):
#     print(num1,num2)
    
# func(1)
# func2(1,2)

def func2(num1,num2=10,num3 =3):   #   키워드 매개변수 값이 들어오지 않으면 default 값으로
    print(num1,num2,num3)   #   100 10 3
    
func2(100)