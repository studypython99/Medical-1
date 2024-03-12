students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 100, 'math': 99, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 99, 'eng': 99, 'math': 98, 'total': 296, 'avg': 98.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 80, 'eng': 80, 'math': 81, 'total': 241, 'avg': 80.33}, 
            {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 90, 'total': 290, 'avg': 96.67}, 
            {'stuNo': 'S005', 'name': '김유신', 'kor': 90, 'eng': 70, 'math': 50, 'total': 210, 'avg': 70.0}, 
            {'stuNo': 'S006', 'name': '강감찬', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0}]

# students = []
# cnt = len(students)+1   #학번
# while True:
#    전체 출력
while True:
    count = input("학생성적 전체출력 (1.확인 2.취소) >>")
    if count == 2:
        break
    print(('[학생성적전체출력]'))
    print('-'*55)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균')
    print('-'*55)
    for i in students:
        # print(i)    #   i = student[{0번째},{1번째}..{n번째}]
        for j in i:
            print(i[j],end="\t")    #   dict 형태일 때, i 키의 [j] 벨류값을 가져온다. 
        print()

