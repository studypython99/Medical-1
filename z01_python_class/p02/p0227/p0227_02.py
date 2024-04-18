'''
조건문

if 조건문1 :
    실행문1
[]    
elif 조건문2 :
    실행문2
else:
    실행문3
] 필요에 따라 생략이 가능
조건문1이 참이면 실행문1 실행
조건문1이 거짓이고 조건문 2가 참이면 실행문2 실행
조건문1,2가 거짓이면 실행문3 실행

elif, else 생략할 수 있다.

if 조건문:
    pass >> 조건을 지나치게 한다. 실행문을 비우고 싶을 때
'''

# a = 3
# if a == 0 :
#     print('if문 실행')
#     print('들여쓰기 중요')
#     print('들여쓰기된 전체 실행')
# elif a == 1 :
#     print('첫번째 elif문 실행')
# elif a == 2 :
#     print('두번째 elif문 실행')
# elif a == 3 :
#     print('세번째 elif문 실행')
# else:
#     print('else문 실행')
    
#   중첩 if문
#   0보다 크면 양수, 작으면 음수를 출력하고
#   양수 중에서 10보다 작으면 [10보다 작음], 크면 [10보다 큼]을 출력

# n = 8 # int타입의 변수
# if 8 >= 0 :
#     print('양수')
#     if n >= 10:
#         print('10보다 큼')
#     else:
#         print('10보다 작음')
# else:
#     print('음수')
    
# if n >= 0 and n <= 10 :
#     print('양수')
#     print('10보다 작음')
# elif n >= 0 and n >10 :
#     print('양수')
#     print('10보다 큼')
# else:
#     print('음수')

# #   quiz
# #   숫자를 한개 입력받아서 짝수면 [짝수] 홀수면 [홀수]
# #   입력: 숫자 1개 (input 이용)
# #   출력: [짝수] or [홀수]

# n = input('숫자를 입력하세요 >>')
# if int(n) % 2 == 0 :
#     print('짝수',n)
# else:
#     print('홀수',n)
    
#   조건: 점수가 90점 이상 A, 이하는 F를 출력
#   A+(98이상), A0(), A-(93이상) 구간을 나누어 출력

p = 92
if p >= 90 :
    #print('A')
    if p >= 98 :
        print('A+')
    elif p >= 93 :
        print('A-')
else:
    print('F')                  #####   선생님이 하신거 붙여넣기 end='' 들어간것