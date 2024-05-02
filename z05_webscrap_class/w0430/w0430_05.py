import oracledb
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
#평균점수를 입력받아 입력한 평균점수 이상의 학생을 출력
#반복진행, -1입력시 종료
search = input("평균점수를 입력하세요 (취소:-1) >>")
print(type(search))
 #"""""" <<< 이걸로 sql 구문 감싸기
# sql = f"""
#         select * from stu_score
#         where avg >='{search}'
#         """
# cursor.execute(sql)
# data = cursor.fetchall()
# print(data)
        
# 점수 입력받으면 그 이상, 이하 나눠서 출력하기
sql = f'''
select name, avg,
case
when avg >= {search} then '{search}이상'
else '{search}이하'
end as grade
from stu_score
order by grade
'''
cursor.execute(sql)
data = cursor.fetchall()
print(*data)

