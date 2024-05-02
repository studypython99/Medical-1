import oracledb
def connection():
    conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor() # 커서생성 - 명령어 입력받는 함수
    return conn,cursor
id_list = []
while True:
    conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()
    #자료 입력하기
    #hhh,1111,홍길자,여자
    id = input("아이디를 입력하세요(-1.취소)>>")
    if id == '-1':
        break
    #id를 검색해서 중복인지 아닌지 확인하기
    sql = f'''
    select * from member where id='{id}'
    '''
    conn,cursor = connection()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data) # 이 자료가 한줄 있다.
    print("id갯수: ",len(data))
    if len(data) ==1:# 자료가 있다면, 다른 아이디를 입력해야한다
        continue    #다시 위로 올라갑시다
    pw = input("패스워드를 입력하세요>>")
    name = input("이름을 입력하세요>>")
    gender = input("성별을 입력하세요>>")
    #db연결, 해제
    sql = f'''insert into member values(member_seq.nextval,'{id}',{pw},'{name}','{gender}',sysdate)'''
    cursor.execute(sql)
    cursor.execute("commit")
    print('입력이 완료되었습니다.')


cursor.close()
conn.close()