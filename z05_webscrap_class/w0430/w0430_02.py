import oracledb
#sql
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe") # localhost: ip
cursor = conn.cursor() # 명령어를 기다림
sql = "select*from board"
cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
                        # fetchone(): 1개의 데이터 가져옴.

#이름 2번째 a가 있는 학생을 출력. 학번으로 순차정렬
# sql = "select no, name from stu_score\
#         where name like '_a%'\
#         order by no desc;"
# cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
#                         # fetchone(): 1개의 데이터 가져옴.
# print("이름 2번째 a가 있는 학생을 출력. 학번으로 순차정렬",data)
# print(sql)#????????????

#board 정보에서 id, name 포함해서 데이터를 가져와 출력
# sql = "select*from board;"
# cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
#                         # fetchone(): 1개의 데이터 가져옴.
# print("board 정보에서 id, name 포함해서 데이터를 가져와 출력",data)

#board 테이블 id 자리에, member테이블 name이 들어오도록
# sql = "select bno,id,name,btitle,bcontent,bdate,bgroup,bindent,bhit,bfile\
#         from board a,member b\
#         where a.id = b.id"# board를 a, member를 b, 로 치환
        # = board의 id는 member의 id로 바꾼다.
        
#board테이블 id포함 모든컬럼, member 테이블의 name컬럼을 가져와 출력

#stu_score avg 90점 이상 A, 80점 이상 B, ,,,
#학번, 이름, 합계, 평균, 학점 출력
# sql =   "select no, name, total, avg from stu_score"
# cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
#                         # fetchone(): 1개의 데이터 가져옴.
# print("grade 출력",data)
#학점을 파이썬에서 프로그램
#학번,이름,합계,평균,학점을 프로그램해서 출력하시오
# sql = '''
#         select no, name, total, avg from stu_score'''

# cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
# data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
#                         # fetchone(): 1개의 데이터 가져옴.
# for i in data[:10]:
#         if i[3] >= 90:
#                 print("grade:","A")
#         if i[3] >= 80:
#                 print("grade:","B")
#         if i[3] >= 70:
#                 print("grade:","C")
#         if i[3] >= 60:
#                 print("grade:","D")
#         else:
#                 print("grade:","F")
#월급의 평균
sql = """
        select round(avg(salary),2) from employees
"""
cursor.execute(sql)
data = cursor.fetchone()
print("월급의 평균: ","$",*data)
        









# print("모든 데이터 출력")
# # print(data)
# for d in data[:10]:
#     print("학번: ",d[0],end=",")# *(별) unpack :리스트가 튜플() 인 경우
#     print("이름: ",d[1],end=",")
#     print("국: ",d[2],end=",")
#     print("영: ",d[3],end=",")
#     print("수: ",d[4],end=",")
#     print("합: ",d[5],end=",")
#     print("평: ",d[6],end=",")
#     print("등: ",d[7],end=",")
#     print("날: ",d[8])
# print("-"*50)
# print("타입: ",type(data))