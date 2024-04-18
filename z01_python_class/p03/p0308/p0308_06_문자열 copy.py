#   인덱싱[0], 슬라이싱[0:4], 
#   len 문자열 길이
#   upper, lower, swapcase, title 대소문자 변환

# shape_list = ["spade","diamond","heart","clover"]
# for i in shape_list:
#     print(i.upper())    #   SPADE   
#     print(i.title())    #   Spade
#     print(i.swapcase()) #   Spade > sPADE
#     print(i.lower())    #   SPADE > spade


# title = "안녕하세요"
# #   역순출력 >> 요세하녕안
# for i in range(len(title)):
#     print(title[-(1+i)])

# a = [1234,11111,1,145,20,1323456547]
# #   리스트 각 숫자의 길이를 출력하시오

# for i in a:
#     if i % 2 ==0:
#         print("숫자: {}, 길이: {}".format(i,len(str(i))))

# #   한글자씩 출력을 해보세요        
# title = "혼자공부하는파이썬수업"
# for i in range(len(title)):
#     print(title[i])
# '''
# 혼
# 자
# 공
# 부
# 하
# 는
# 파
# 이
# 썬
# 수
# 업
# '''
    
#   짝수만 문자길이를 출력하시오


# a = input("문자를 입력하세요 >>")
# print("현재 입력한 문자 길이: ",len(a))
# a = "안녕"
# b = 100
# c = 200
# d = "1000"
# print(a+d)
# #   str에만 len