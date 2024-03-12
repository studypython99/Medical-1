students = [[1,'홍길동',100,100,100,300,100],
            [2,'유관순',100,100,100,300,100],
            [3,'이순신',100,100,100,300,100]] 

#   찾는 학생의 이름

#   찾고자 하는 학생 찾기
while True:
    search = input('검색하고 싶은 학생 이름을 입력하세요.(0. 취소)')
    check = 0   #   찾는 정보확인
    count = 0
    if search == '0':
        break
    for stu in students:
        if search in stu:
            check = 1   #   정보를 찾았을 때 정보확인을 1로 변경
            break
        count += 1  #   홍길동이면 0 에서 멈춤, 
    if check == 1:
        print('[{} 학생성적 출력]'.format(search))
        print('{}의 학생정보를 찾았습니다.'.format(search))
        print('-'*50)
        print('번호\t이름\t국어\t영어\t수학\t합계\t평균')
        print('-'*50)
        for i in students[count]:
            print(i,end='\t')
        print()
    else:
        print('찾는 학생이 없습니다.')
        