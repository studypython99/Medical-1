member = [['홍길동', 90],['이순신', 10],['유관순', 80]]

#   입력: 이름, 점수 (input 사용) ['홍길동', 90]
#   3명의 정보를 member리스트에 넣으세요.
# for i in range(3):
#     name = input('이름을 입력하세요>>') member[i][0]
#     sco = int(input('점수를 입력하세요>>'))   member[i][1]
#     ppp = [name, sco]   #   리스트는 []를 사용해야한다 !!
#     member.append(ppp)

# print(member) # [['홍길동', 90],['홍길동', 90],['홍길동', 90]]

print(member[0][0]) #   홍길동
print(member[1][0])
print(member[2][0]) # 가변(012), 불가변(이름0,점수1) 구분지어서 입력값을 조정
for i in range(len(member)):
    if member[i][1] >= 60 :
        print('{}님 {}점으로 합격입니다.'.format(member[i][0],member[i][1]))
    else:
        print('{}님 {}점으로 불합격입니다.'.format(member[i][0],member[i][1]))