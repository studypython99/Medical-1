#   중첩 if

a = 97
if a > 90:
    print('90보다 큽니다.')
else:
    print('90보다 작습니다.')
    
if a > 90:
    print('90보다 큽니다.')
    if a < 95:
        print('95보다 작습니다.')
    else:
        print('95보다 큽니다.')
else:
    print('90보다 작습니다.')
    
#   사과의 상태가 good이며
#   1000원 이하이면 [10개 구매]
#   1000원보다 비싸면 [3개 구매]를 출력

# apple = 'good'
# price = 3000
# hi_price = 2000 #
# low_price = 300
# if apple == 'good':
#     if hi_price > price:
#         if price <= 1000:
#             print('10개 주세요.')
#         else:
#             print('3개 주세요.')
#     else:
#         print('너무 비싸요.')
# else:
#     print('안사요.')

#   숫자 하나를 입력받아서
#   100보다 큰 수 이면서 짝수면 [짝수], 홀수면 [홀수] 출력
#   100보다 작은 경우 [100보다 작다] 출력
#   num = 102 > [짝수] num = 4 [100보다 작다]

num = int(input('숫자를 입력하세요 >>'))
if num > 100:
    if num % 2 == 0:
        print('100보다 큰 수이며, 짝수 입니다.')
    else:
        print('100보다 큰 수이며, 홀수 입니다.')
else:
    print('100보다 작습니다.')