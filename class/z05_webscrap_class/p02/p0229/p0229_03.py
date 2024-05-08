#   반복문 for / while
'''
for i in range(시작, 끝+1, step):
    수행할 문장
    
while 조건식: # 이 조건이 참일 때
    실행할 문장
    
변수 = 시작값
while 변수 < 끝값 : # 이 조건이 참일 때
    반복구문
    변수 = 변수 + 증가값
    
'''

#   for 문으로 안녕하세요 3회 출력
for i in range(3):
    print('for: 안녕하세요')
    
#   while 문으로
i = 0
while i < 3 :
    print('wile: 안녕하세요')
    i += 1
    
#   for 문으로 0~10까지 출력
for i in range(11):
    print('for:',i,end=' ')
print()
#   while 문으로 0~10까지 출력
i = 0
while i < 11 :
    print('while:',i,end=' ')
    i += 1
    
#   while을 사용
#   1~10사이의 3의 배수를 출력
print()
i = 0
while i < 11:   #for i in range(1,11):
    i += 1
    if i % 3 == 0:
        print(i)
        
#   1~100사이의 홀수 출력
# for i in range(1,101):
#     if i % 2 == 1:
#         print(i,end=' ')
        
i = -1
while i < 100:
    i += 2
    print(i,end=', ')
print()    
sum1 = 0
j = 1
while j <= 100:
    sum1 += j
    j += 1
print(sum1)

# while True: #   무한히 반복시키고자 할 때
#     print('z',end='')        

#   break문 / continue문
#   break문: 반복문을 빠져나와, 다음단계를 수행한다.
n = 0
while n < 100:
    print(n)
    if n == 4:  #   4가 되면 여기 ㄲㅏ지만 실행됨
        break   #------------------------------------------
    n = n + 1   #   4가 되면 여기서부터는 실행안됨
    print('-'*20)
    
breakletter = []

while True:
    n = input('숫자를 입력해주세요(종료: 0)')
    print(n)
    if n == '0':
        print('종료되었습니다.')
        break
print('프로그램이 종료되었습니다.')
