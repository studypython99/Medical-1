# students = [
#     [S001, '홍길동', 100, 100, 99, 299, 99.67,1],
#     [S002, '유관순', 99, 99, 98, 296, 98.67,1],
#     [S003, '이순신', 80, 80, 81, 241, 80.33,1],
#     [S004, '김구',100, 100, 90, 290, 96.67,1],
#     [S005, '김유신', 90, 70, 50, 210, 70.0,1],
#     [S006, '강감찬', 100, 100, 100, 300, 100.0,1]
#     ]
students = []
cnt = len(students)+1   #학번
while True:
    name = input(f"{len(students)+1}번째 학생의 이름을 입력하세요 (0.취소)>>")
    if name == '0':
        print("학생입력을 취소합니다.")
        break
    student = {}    #   데이터 초기화
    student["stuNo"] = "S"+"{:03d}".format(cnt)
    student["name"] = name          #    딕셔너리 추가
    kor = int(input("국어점수 입력하세요 >>"))
    student["kor"] = kor
    eng = int(input("영어점수 입력하세요 >>"))
    student["eng"] = eng
    math = int(input("수학점수 입력하세요 >>"))
    student["math"] = math
    total = kor+eng+math
    student["total"] = total
    avg = total/3
    student["avg"] = float('{:.02f}'.format(avg))
    students.append(student)
    cnt += 1
    print(student)
    print(students)
    '''   [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]
'''