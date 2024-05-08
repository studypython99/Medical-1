#   학생성적프로그램
print('-'*35)
print('\t[학생성적프로그램]')
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생성적전체출력')
print('5.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

st_num1=input('번호')
st_name1=input('이름')
st_kor1=int(input('국어'))
st_eng1=int(input('영어'))
st_math1=int(input('수학'))
st_sum1=int((st_kor1+st_eng1+st_math1))
st_avg1=int((st_sum1/3))
st_rank1=1

st_num2=input('번호')
st_name2=input('이름')
st_kor2=int(input('국어'))
st_eng2=int(input('영어'))
st_math2=int(input('수학'))
st_sum2=int((st_kor2+st_eng2+st_math2))
st_avg2=int((st_sum2/3))
st_rank2=2


print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
    st_num1,st_name1,st_kor1,st_eng1,st_math1,st_sum1,st_avg1,st_rank1
))
print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
    st_num2,st_name2,st_kor2,st_eng2,st_math2,st_sum2,st_avg2,st_rank2
))

#   홍길동  100 100 100
#   유관순  90  100 90