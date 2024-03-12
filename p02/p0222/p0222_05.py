#   국어, 영어, 수학 점수를 입력받아서 평균을 출력하세요.
#   출력: 평균은 99점 입니다.
#   변수: kor, eng, math

kor=int(input('국어점수는?'))
eng=int(input('영어점수는?'))
math=int(input('수학점수는?'))
print('평균은 {:.2f}입니다.'.format((kor+eng+math)/3))