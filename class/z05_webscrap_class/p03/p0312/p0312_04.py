#   매개변수의 순서, 타입이 중요하다.

def str_print(txt,num): #   순서, 타입도 맞아야한다
    # for i in range(num):
    #     print(txt,end='')
    x = txt*num
    print(x)

txt = input("출력하고 싶은 글자를 입력하세요 >>")
num = int(input("출력하고 싶은 글자 반복횟수 >>"))
str_print(txt,num)  #   순서, 타입도 맞아야한다

#   안녕하세요 3회
#   안녕하세요안녕하세요안녕하세요

