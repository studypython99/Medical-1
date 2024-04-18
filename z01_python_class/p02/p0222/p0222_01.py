#   변수, 함수

#   a=1 변수, 변수선언
#   a() 함수, 함수는 중괄호를 사용 ex) print(), 파이썬에서 기본적으로 제공

print('hello world!') # 문자열 출력
print(20)
print(100+200) #    숫자, 사칙연산
print("10",20) #   "10" 문자, 20 숫자
#print("10"+10) #    +사용시 같은 타입만 출력
print(int("10")+10) # 20 출력
print("10"+str(10)) #   10+10 출력

print('hello'*20) # 문자를 n번 반복해서 출력

# %d 정수, %f 실수, %s 문자열
print('%d,%d'%(5,2))
print('%d,%f,%s'%(2,4.12,"ddd")) #  type에 맞춰서 작성해야한다.

#   소수점 둘째자리까지 출력
print('%.2f'%(234.23432))

#   총 10자리 빈칸은 0 소수점은 3자리까지
print('%010.3f'%25.05)
print('%010s'%'python')
print('{:.1f},{},{}'.format(432.22,23,'string'))
print('파이썬 수업을 진행합니다.\n파이썬 기본편입니다.') #  줄바꿈
print('파이썬 수업을 진행합니다.\t파이썬 기본편입니다.') #  tab 들여쓰기
print('파이썬 수업을 진행합니다.\
    \n파이썬 기본편입니다.') #  너무 길면 \ 로 줄바꿔서 작성

#   print ",' 사용하기
print("산에올라 '야호' 한다.")
print('산에올라 "야호" 한다.')
print('산에올라 \'야호\' 한다.')