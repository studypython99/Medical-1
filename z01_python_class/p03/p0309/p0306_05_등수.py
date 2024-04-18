students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33,'rank':0}, 
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67,'rank':0}, 
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67,'rank':0}, 
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0,'rank':0}, 
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67,'rank':0}
]
cnt = len(students)+1
print(cnt)
while True:
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')  
    print('-'*40)
    choice = input('프로그램 번호를 입력하세요 >>')
    print('-'*40)
    if not choice.isdigit():
        print("숫자만 입력하세요.")
        continue
    choice = int(choice)
    
    #   5. 등수
    if choice == 5:
        print('5. 등수처리')
        for i in students:
            rank_cnt = 1
            for j in students:
                if i['total'] < j['total']:
                    rank_cnt += 1
            i['rank'] = rank_cnt
    print(students)