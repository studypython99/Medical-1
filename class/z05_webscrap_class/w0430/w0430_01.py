import oracledb
#sql
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe") # localhost: ip
cursor = conn.cursor() # 명령어를 기다림
sql = "select*from stu_score"
cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값: list)
data = cursor.fetchall()# fetchall(): 모든 데이터 가져옴,
                        # fetchone(): 1개의 데이터 가져옴.

#이름 2번째 a가 있는 학생을 출력. 학번으로 순차정렬
sql = "select no, name from stu_score\
        where name like '_a%'\
        order by no desc;"
        
print(sql)








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