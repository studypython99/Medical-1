# #   빈 리스트 생성
# cont = []

# c1 = cont.append(input('1. 나라를 입력해주세요 >>'))
# c2 = cont.append(input('2. 나라를 입력해주세요 >>'))
# c3 = cont.append(input('3. 나라를 입력해주세요 >>'))
# c4 = cont.append(input('4. 나라를 입력해주세요 >>'))

# print(cont[:]) # [미국, 영국, 일본, 중국] 이렇게 되도록
# print(type(cont))
# print('{}-{}-{}-{}'.format(cont[0],cont[1],cont[2],cont[-1]))

f = [] #    과일리스트
#   내가 입력한 과일들로 리스트를 채워보세요. 과일 3개 이상
f.append(input('과일이름을 입력하세요 >>'))
f.append(input('과일이름을 입력하세요 >>'))
f.append(input('과일이름을 입력하세요 >>'))
print('내가 좋아하는 과일은',f[0],f[1],f[2],'입니다.')

#   내가 좋아하는 과일은 a, b, c 입니다.