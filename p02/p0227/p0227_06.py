#   이름, 아이디, 비밀번호 입력받기 input
#   5명을 입력받아서 member리스트를 만드세요
member = [] #   [[홍길동,aaa,111],[유관순,bbb,222],[이순신,ccc,333]]
'''
이름    아이디  비번
홍길동  aaaa    1111
이순신  bbbb    2222
'''
for i in range(3):
    na = input('이름을 입력하세요 >>')
    id = input('아이디를 입력하세요 >>')
    pw = input('비밀번호를 입력하세요 >>')  #   입력을 받으면 이걸 저장할 수 있는
    li = [na,id,pw]                         #   개인의 리스트가 따로 존재해야한다
    member.append(li)                       #   개인의 리스트를 전체 리스트로 옮겨준다
print('-'*20)
print('이름\t아이디\t비밀번호')     #   반복이 필요 없는 친구는 for 밖으로 
for i in range(len(member)):
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2]))



