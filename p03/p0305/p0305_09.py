'''
딕셔너리
쌍, 2개가 하나 키key:값(value)
딕셔너리변수 ] {키1:값1,키2:값2...키n:값n}
'''
#   리스트는 대괄호, 출력 index 번호를 사용해서 출력
a = ["새우깡",90,1200]
print(a[0])

#   딕서너리 중괄호, 출력 key를 사용해서 출력
product = {"name":"새우깡","무게":90,"금액":1200}
print(product["name"])


students = {"stuNo":1,"name":"홍길동","kor":100,"eng":100,"math":100,"sci":99}

#   딕셔너리 추가하기
students["총합"] = 399
print(students) 
#   {'stuNo': 1, 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 100, 'sci': 99, '총합': 399}