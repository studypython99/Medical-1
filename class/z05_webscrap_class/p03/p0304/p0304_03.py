#   학생 2명의 국어, 영어, 수학을 입력받아
#   합계를 출력하시오
students = []   #   for 밖에서는 누적되도록
 
for i in range(3):  
    student = []    #   한번씩 다시 할 때마다 리셋되도록
    student.append(input('이름을 입력하시오.'))
    #   kor = int(input('국어점수를 입력하세요.))
    student.append(int(input('국어점수를 입력하시오.')))
    student.append(int(input('영어점수를 입력하시오.')))
    student.append(int(input('수학점수를 입력하시오.')))
    sum = student[1]+student[2]+student[3]  #   student[0]= 이름
    student.append(sum)
    student.append('{:.2f}'.format(sum/3))  #   평균, 소숫점 2자리까지
    students.append(student)

#   전체학생출력
print('[학생성적 출력]')
print('-'*50)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*50)
for stu in students:
    for s in stu:
        print(s,end='\t')
    print()
print('-'*50)

#   2차원 리스트는 for문을 2번 사용함.
#   3명의 국어점수 합계, 평균을 출력하시오
kors = 0
engs = 0
maths = 0
totals = 0
avgs = 0

for stu in students:
#   for i, stu in enumerate(students): ??? i는 사용하는곳이 없는데;;
    kors += stu[1]
    engs += stu[2]
    maths += stu[3]
    totals += stu[4]
        
avgs = totals/len(students)
print(kors, engs, maths, totals,avgs)

