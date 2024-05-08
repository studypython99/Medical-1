import oracledb
# def connection():
#     conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
#     cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
#     return conn,cursor
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
sql = '''
create table mem(
id varchar2(30) primary key,
pw number,
name varchar2(30),
mdate date
)
'''
cursor.execute(sql)

#ddl 명령어는 commit이 없다 ex) create, alter, drop
#dml 명령어: insert, update, delete

print("테이블생성 완료")