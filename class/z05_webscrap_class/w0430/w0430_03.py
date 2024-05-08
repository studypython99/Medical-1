import oracledb
#DB connect연결
conn = oracledb.connect(user="ora_user2",password="1111",dsn="localhost:1521/xe") # localhost: ip
cursor = conn.cursor()

#sql실행
#employees 테이블에서, 사번,이름,월급,실제월급
# sql = """
#         select employee_id, emp_name, round(salary,-1), to_char(salary*(1+nvl(commission_pct,0))*1410,'999,999,999')
#         from employees
# """
# cursor.execute(sql)
# data = cursor.fetchall()

# print("데이터출력")
# for d in data:
#         print("사번: ",d[0],end="\t")
#         print("이름: ",d[1],end="\t")
#         print("월급: ＄",d[2],end="\t")
#         print("실급: ￦",d[3].strip())
#         print()
        
#부서별 평균,최대,최소월급

sql = """
        select department_id, round(avg(salary),-1), max(salary), min(salary) from employees
        where department_id is not null
        group by department_id
        order by department_id
        
"""
cursor.execute(sql)
data = cursor.fetchall()

print("데이터출력")
for d in data:
        print("부서: ",d[0],end="\t")
        print("평균: ",d[1],end="\t")
        print("최대: ",d[2],end="\t")
        print("최소: ",d[3])
        print()

