students = [
    [1, '홍길동', 100, 100, 99, 299, 99.67,1],
    [2, '유관순', 99, 99, 98, 296, 98.67,1],
    [3, '이순신', 80, 80, 81, 241, 80.33,1],
    [4, '김구',100, 100, 90, 290, 96.67,1],
    [5, '김유신', 90, 70, 50, 210, 70.0,1],
    [6, '강감찬', 100, 100, 100, 300, 100.0,1]
    ]
while True:
    search = input('삭제하려는 학생의 이름을 입력하세요.')
    
    #   이름찾기
    cnt = 0
    for stu in students:
        if stu[1] == search:    #   만약, 검색한 이름이 있다면
            break   #   맞으면 브레이크, 빠져나옴
        cnt += 1
        print('{} 학생을 찾았습니다'.format(search))
            #   여기까지 하면 홍길동 찾고 이후 else 까지 모두 실행
    if cnt == len(students):    # 학생수만큼 채워지면 이후에 검색자가 없다  
            print('{} 학생이 없습니다'.format(search))
    else:
        print('{} 학생을 찾았습니다'.format(search))
    print('찾은 위치: ',cnt)
    del students[cnt]
    print(students)
    print('-'*40)