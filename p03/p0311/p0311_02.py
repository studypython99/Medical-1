students = [
    [1, '홍길동', 100, 100, 99, 299, 99.67,1],
    [2, '유관순', 99, 99, 98, 296, 98.67,1],
    [3, '이순신', 80, 80, 81, 241, 80.33,1],
    [4, '김구',100, 100, 90, 290, 96.67,1],
    [5, '김유신', 90, 70, 50, 210, 70.0,1],
    [6, '강감찬', 100, 100, 100, 300, 100.0,1]
    ]
#   csv파일
students = "1, '홍길동', 100, 100, 99, 299, 99.67,1"    #   문자열로 가져온다
s_list = students.split(",")#   ,로 구분지어서 가져온다 / 문자열 분리함수
print(s_list)   #   ['1,', "'홍길동',", '100,', '100,', '99,', '299,', '99.67,1']