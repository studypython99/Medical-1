
student = []

#   두명 이상 학생의
#   이름, 국, 영, 수 점수를 입력받아
stu1 = []
stu1.append(input('이름을 입력하세요 >>'))
stu1.append(int(input('국어점수를 입력하세요 >>')))
stu1.append(int(input('영어점수를 입력하세요 >>')))
stu1.append(int(input('수학점수를 입력하세요 >>')))
print(stu1)
stu2 = []
stu2.append(input('이름을 입력하세요 >>'))
stu2.append(int(input('국어점수를 입력하세요 >>')))
stu2.append(int(input('영어점수를 입력하세요 >>')))
stu2.append(int(input('수학점수를 입력하세요 >>')))
print(stu2)
#   리스트를 생성 후,
#   student 리스트에 넣어주세요
student.append(stu1) #  한 list씩 입력해야한다.
student.append(stu2)
#   student 리스트 전체 출력
print('{}\n{}'.format(student[0],student[1]))






student = []
# 튜플 (), 딕셔너리 {}, 리스트 []
# 두명 이상의 학생의 
# 이름, 국, 영, 수 점수를 입력받아 input()사용 
# 리스트를 생성 후, 
# student리스트에 넣어주세요
# 학생1명
# stu1 = ['',0,0,0] # 기본값 설정 길이 설정 
# # stu1 = [] 로 설정 후 아래 사용할 경우 오류 
# stu1[0] = input('이름을 입력하세요 >> ') # 이름을 넣을예정
# stu1[1] = int(input('국어점수를 입력하세요 >> '))# 국어
# stu1[2] = int(input('영어점수를 입력하세요 >> '))# 영어
# stu1[3] = int(input('수학점수를 입력하세요 >> '))# 수학 
# print(stu1)
name = input('1. 이름을 입력하세요 >> ')
kor = int(input('국어점수를 입력하세요 >> '))
eng = int(input('영어점수를 입력하세요 >> '))
math = int(input('수학점수를 입력하세요 >> '))
# 리스트에 값 넣기 
# 방법 1
stu1 = [name, kor, eng, math]
stu1.append(kor+eng+math) # 총점
stu1.append((kor+eng+math)/3) # 평균
student.append(stu1)
print(student)


# 방법 2
# stu1 = [] # 빈리스트를 만들고
# stu1.append(name)
# stu1.append(kor)
# stu1.append(eng)
# stu1.append(math)
# print(stu1)

stu2 = []
name = input('1. 이름을 입력하세요 >> ')
kor = int(input('국어점수를 입력하세요 >> '))
eng = int(input('영어점수를 입력하세요 >> '))
math = int(input('수학점수를 입력하세요 >> '))
stu2 = [name, kor, eng, math]
stu2.append(kor+eng+math) # 총점
stu2.append((kor+eng+math)/3) # 평균
student.append(stu2)
print(student)



# student 리스트 전체 출력 
print(student)
#[['홍길동',100,100,100 ],['유관순',100,100,90]]