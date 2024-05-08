students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]
# print(students[5]['name'])  #[i(0,1,2...)][key] = value

#   모든 학생의 국어점수를 출력하시오
'''
[국어점수]
0.  홍길동: 100
1.  유관순: 98
'''
print('[국어점수]')
for i, stu in enumerate(students):  #   i로 사용해서 숫자: 0,1,2,3... // stu로 사용해서 딕셔너리: 0,1,2,3...
    print('{}. {}: {}'.format(i,stu['name'],stu['kor']))

# #   김구 국어+영어점수 합계 출력
# print(students[3]['kor']+students[3]['eng'])

# #   이순신의 국어점수를 100점으로 변경
# print("변경전: ",students[2]['kor'])
# students[2]["kor"] = 100
# print("변경후: ",students[2]['kor'])

# #   이름을 모두 출력하자
# for i, s_dict in enumerate(students):
#     print("{}. {}".format(i,s_dict['name']),end=', ')    