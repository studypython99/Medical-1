students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]
subject = ['순번','학번','국어','영어','수학','합계','평균','등수']
s_title = ['','국어','영어','수학']
# students = []
# cnt = len(students)+1   #학번
#   찾는 프로그램 작성
while True:
    search = input('찾을 학생의 이름을 입력하세요 (0.취소)>>')
    chk = 0
    if search == '0':
        break
    for i in students:
        if i['name'] == search:
            break
        chk += 1
    
    print("찾고자 하는 학생의 위치:",chk)

    if chk >= len(students):
        print("찾는 학생이 없습니다.")
    else:
        print("{} 학생을 찾았습니다.".format(search))
        s_input = (input("{} 학생 성적을 삭제하시겠습니까? (0.취소)".format(search)))
        #   삭제
        if s_input != '1':
            print('삭제를 취소합니다.')
            #break??
        else:
            del students[chk]
            print('{}학생의 성적이 삭제되었습니다.'.format(search))
            