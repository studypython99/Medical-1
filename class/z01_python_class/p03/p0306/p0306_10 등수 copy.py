students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]

#   등수처리: 합계로 비교한다.
for i, s_dic in enumerate(students):
    rank_cnt = 1    #   등수처리 변수
    for i_dic in students:
        if s_dic['total'] < i_dic['total']:
            rank_cnt += 1
    s_dic['rank'] =rank_cnt
print(students)