students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]

cnt = len(students)+1
# 학생번호 사용
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
    choice = input('원하는 번호를 입력하세요:  ')
    print('-'*40)
    if not choice.isdigit():
        print('숫자만 입력 가능합니다.')
        continue # 반복문 계속실행
    choice = int(choice)
    
    if choice == 1:
        print('1. 학생성적입력')
        while True:
            name = input('이름을 입력하세요 (0.취소) >>')
            if name == 0:
                break
            student = {}
            student["stuNo"] = 'S{:03d}'.format(cnt)
            student["name"] = name
            kor = int(input('국어점수 입력 >>'))
            student["kor"] = kor
            eng = int(input('영어점수 입력 >>'))
            student["eng"] = eng
            math = int(input('수학점수 입력 >>'))
            student["math"] = math
            total = kor+eng+math
            student["total"] = total
            avg = total/3
            student["avg"] = float('{:.2f}'.format(avg))
            student["rank"] = 1
            students.append(student)
            cnt += 1
            print(student)
            print(students)

    if choice == 2:            
        print('2. 학생성적전체출력')
        print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
        for i in students:
            for j in i:
                print(i[j],end='\t')
            print()
            
    if choice == 3:
        print('3. 검색출력')
        search = input('검색 학생 이름을 입력하세요 (0.취소) >>')
        if search == '0':
            break
        for i, stu in enumerate(students):
            if search == stu['name']:
                print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(*stu[i]))
                # print(stu['stuNo'],stu['name'],stu['kor'],stu['eng'],stu['math'],stu['total'],stu['avg'],end='')
        print()
                