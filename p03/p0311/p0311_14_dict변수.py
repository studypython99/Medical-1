def stu_update(student):    #   지역변수 > 주소값이 저장되어있다.
    student['stuNo'] = 2
    student['name'] = "유관순"
    student['total'] = student['kor'] + student['eng'] + student['math']
    student['avg'] = student['total']/3
#   return이 없어도 리스트형식으로 값을 전달할 수 있다.
#   갯수가 많다면 리스트로 받는것이 편하다.
#   한개라면 return으로 받는다.
#   호출하는 방법만 다르고 리스트와 동일한 구조

student = {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 0, 'avg': 0}  #   2개 이상의 변수

#   함수호출
stu_update(student) #   전역변수,  6번줄 리턴을 받는 순서도 중요하다


print("학생1: ",student)  #   학생1:  1 홍길동 100 100 100 300 100.0