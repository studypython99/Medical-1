import oracledb
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

while True:
        search = input("찾고자 하는 이름을 입력하세요(취소:-1) >>")
        if search == '-1':
                break
        # 홍길동, 홍 하면 홍이 포함된 모든 글자 검색
        sql = f"""
                select * from stu_score
                where name like '%{search}%'"""
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        

conn.close()