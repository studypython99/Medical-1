select*from employees;

--as xxx 변수명 변경하기, as 생략가능! ""추가시 이름 그대로 스크립트 반영됨
select salary, salary*1400, salary*1400*12 Y_sal from employees;

select*from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score; 

select department_id from employees;

--null : 0으로 만들기
select nvl(department_id,0) from employees;

select*from employees;

--월급계산, comission_pct가 null로 표시된다
--별칭: as사용, "": 키워드를 있는 그대로 사용
select salary, salary + (salary*nvl(commission_pct,0)) as "Realsal" from employees;

select salary as 년봄 from employees;--웬만하면 영문으로...

select*from departments;
--부서번호, 부서이름을 출력하시오
select department_id, department_name from departments;

--concat: 여러개의 데이터를 1개로 합쳐서 넘겨야 할 경우 사용 || (shift+\)
--ex) 홍길동, 유관순, 이순신, 강감찬, 김구 
--split(): 분리 리스트 배열로 저장

select*from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

--중복제거: distinct
--where: 조건절 // not 제거하고 검색: is not null
select DISTINCT department_id from employees where department_id is not null;

--manager_id
select DISTINCT manager_id from employees where manager_id is not null;

select*from employees;

--id: 200번의 급여를 보고싶다. 200,201,202
select employee_id, salary from employees
where employee_id = 200 or employee_id = 201 or employee_id = 202;

--200이상 203이하
select*from employees
where employee_id >=200 and employee_id <=203;

--150이하 200이상
select*from employees
where employee_id <=150 or employee_id>=200;

--department_id 10,30,50에 해당하는 사원을 출력
select*from employees
where department_id=10 or department_id=30 or department_id=50;

--월급 6000~9000인 사원을 출력하시오
select*from employees
where salary>= 6000 and salary<=9000;

--월급 6,7,8000인 사원
--정렬: order by 컬럼, asc:순차정렬, desc:역순정렬
select*from employees
where salary=6000 or salary=7000 or salary=8000
order by salary desc;

--부서번호(department_id)가 50번이면서, 월급(salary)이 8000이상인 사원
select*from employees
where department_id=50 and salary >=8000;

--입사일자 순차(asc)정렬
select hire_date from employees
order by hire_date ASC;

--입사일자 역순(desc)정렬
select hire_date from employees
order by hire_date desc;

--02/01/01부터 입사일자 정렬
select emp_name, hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc;

select hire_date, hire_date+100 from employees;
--반올림 round(숫자,자릿수까지)
select round(sysdate-hire_date,2) from employees;

select*from employees;
--문자합치기는 ||명령어 사용, (+안됨;;)
select emp_name||email from employees;

--입사일 05년 이상 06년 이하이면서
--월급이 6000 이상인 사원의 입사일을 역순정렬하시오
select emp_name, hire_date, salary from employees
where hire_date>='05/01/01' and hire_date<'07/01/01' and salary >6000
order by hire_date desc;
