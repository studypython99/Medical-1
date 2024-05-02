import oracledb


conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() #커서생성, 명령어 입력받는 함수


# sql = ""

# #insert 저장하기
# sql = '''
# insert into member values(member_seq.nextval,'ggg',1111,'김유신','남자',sysdate)
# '''
# cursor.execute(sql)
# cursor.execute('commit')

# #update 저장하기
# sql = '''
# update member set name='홍길동' where id='aaa'
# '''
# cursor.execute(sql)
# cursor.execute('commit')

#select 읽어오기
sql = '''
    select * from member'''
cursor.execute(sql)
data = cursor.fetchall() #fetchall: 여러개, fetchone: 한개
for i in data:
    print(i)
#입력






















cursor.close()