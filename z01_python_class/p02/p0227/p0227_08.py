#   반복문
'''
for 변수 in range(시작값, 끝값+1, 증가값):
'''
# for i in range(3):  # i = 0,1,2
#     print('안녕')
#     #   i = 0 일 때  >>안녕
#     #   i = 1 일 때  >>안녕
#     #   i = 2 일 때  >>안녕
    
# for i in range(100):
#     print(i+1)
    
# sum1 = 0
# for i in range(1,6,1):
#     sum1 = sum1 + i
    
#   숫자 한개를 입력받아서 1부터 입력한 수 까지의 합을 구하세요.
# n1 = int(input('숫자를 입력하세요 >>'))
# summ = 0
# for i in range(1,n1+1):
#     summ += i
# print(summ)
    
#   짝수의 합만 구함 (2+4+6+8+...+)
# n1 = int(input('숫자를 입력하세요 >>'))
# summ = 0
# for i in range(1,n1+1):
#     if i % 2 == 0 :
#         summ += i
# print(summ)

#   1~10까지의 곱
xxx = 1
for i in range(1,11):
    xxx *= i
print(xxx)