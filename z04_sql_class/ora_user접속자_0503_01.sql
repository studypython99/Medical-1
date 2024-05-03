-- non-equi join
select no,name,avg,grade 
from stu_score,stu_grade
where avg between low_score and high_score
order by no
;
--name,sum(amount),rank출력
select*from shop_product;

select name, s_amount,rank 
from (select name, sum(amount) as s_amount from shop_product where pdate>='2024/03/01' group by name),customer_rank
where s_amount between low_amount and high_amount
;
--t
select name,s_amount,rank from (select name,sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name),customer_rank
where s_amount between low_amount and high_amount
;
select name,sum(amount) s_amount from shop_product group by name;

--순번을 새롭게 부여해서 출력해주는 함수 rownum, row_number()
--마지막에 번호가 부여됨 rownum
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product
;
--11번부터 시작하면 문제가 발생, rownum은 1번부터 시작함;;
select rownum rnum,b.* 
from
(
select rownum rnum,a.* from lotte_product a --번호를 미리 붙여놓는다
)b
where rnum >=11 and rnum <=20;
--order by 때문에 번호가 꼬이는것을 미연에 방지하기 위해 미리 order를 진행시킨 후 rownum실행
select rownum,b.*
from (select * from lotte_product order by std_ym) b
;

select rownum,a.*
from lotte_product a
where rownum <= 10 --10개만 가져오기
;

select*from stu_score 
order by no
;
--kor 점수 21~30등 출력
select rownum, b.* from(select rownum rnum,a.* from stu_score a order by kor desc)b;
select c.* from(select rownum rnum, b.* from(select rownum rnum,a.* from stu_score order by kor desc)a)b)c where rnum >=21 and rnum <=30;
--!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
/* 1: select * from stu_score a order by kor desc;
   2: select rownum rnum, a.* from(select * from stu_score a order by kor desc)a */
select * from (select rownum rnum, a.* from(select * from stu_score a order by kor desc)a) where rnum >=11 and rnum <=30;

--drop table students;
select*from students;
update students set id='aaa',name='홍길동', gender='m' where id='Claire' and pw='7577';--2명
update students set id='bbb',name='유관순', gender='m' where id='Koralle';
update students set id='ccc',name='이순신', gender='f' where id='Cornall' and pw='1997'; --2명
update students set id='ddd',name='강감찬', gender='m' where id='Zitella';
update students set id='eee',name='김구', gender='f' where id='Sutton';
update students set id='fff',name='김유신', gender='m' where id='Alanah';
update students set id='ggg',name='홍길자', gender='f' where id='Cirstoforo';
commit;
rollback;
--새롭게 순차적 번호생성: rownum
--1. select 구문
select a.* from students a;
--2. rownum 함수 실행
select rownum, a.* from students a;
--3. order by 구문 실행
select rownum, a.* from students a
order by grade;

--1.select 2.order by 구문 3.rownum
select * from students
order by grade;

select rownum, a.* from
(
select * from students
order by grade;
)a;

--평균 85이상, no 500보다 큰 수 검색
select a.* from stu_score a
where avg >= 85 and no>500
order by no;
--위와 동일
select * from
(
select*from stu_score where avg >=85
) where no>=500
;
--이름별, 구매내역 합계
select*from shop_product;
select neme, amount, pdate from shop_product
where pdate >='2024-03-01';
--equi join: 컬럼이 2개의 테이블에 각각 존재, 2개의 컬럼을 이용해서 검색하는 방법
--non equi join: 같은 컬럼이 없으면ㅅ ㅓ2개의 테이블을 사용해 검색하는 방법
select name, s_amount, rank 
from (select name, sum(amount) as s_amount from shop_product where pdate >='2024/03/01' group by name), customer_rank
where s_amount between low_amount and high_amount
;--non equi join

select name, sum(amount) as s_amount from shop_product
where pdate >='2024/03/01'
group by name;

select rownum, a.* from students a
order by id;

select * from(select rownum rnum, b.* from (select *from students order by id)b) where rnum>=11 and rnum <=20;

select row_number() ober(order by id) as rnum,a.*
from students a)
where rnum>=11 and rnum<=20;
--self join, 이름을 오른쪽 끝에 한번 더 붙이고 싶다
select employee_id,emp_name,a.department_id, department_name, a.manager_id from employees a, departments b
where a.department_id = b.department_id
order by a.department_id;

-- cross join 107 * 107
-- self join,equi-join 함께 사용
-- equi join : 2개 테이블에 같은 컬럼을 가지고 검색
select a.employee_id, a.emp_name, a.department_id, department_name, a.manager_id, b.emp_name
from employees a,employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
--매니저 아이디와 같은 직원 아이디를 가져와서 b.emp_name을 입력해라
--자기 상사 찾아서 기록해놓기
;
--self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

--'Guy Himuro'과 동일한 부서에 근무하는 사람을 출력하시오
--컬럼: 사원명, 부서번호, 동일팀 사원명 부서번호
--1. john 부서 출력
--2. 같은 부서번호의 사람들 출력
select * from employees;
select a.emp_name, a.department_id, b.emp_name, b.department_id
from employees a, employees b
where a.emp_name like 'Guy Himuro' and a.department_id = b.department_id
;

select*from member;

insert into member values(
member_seq.nextval,'ddd',1111,'강감찬','남자',sysdate
);
commit;
desc member;
update member set name='홍길동' where id='aaa';
rollback;

select * from employees;

select a.emp_name,a.department_id,c.department_name,b.emp_name 
from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name = 'Pat Fay'
and a.department_id = c.department_id
;
select*from member;
--hhh,1111,홍길자,여자

--테이블 생성
create table mem(
id varchar2(30) primary key,
pw number,
name varchar2(30),
mdate date
);

select*from mem;
--drop table mem;

create table yeogi(
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);
select * from yeogi;

--2개 ㅌㅔ이블: department_id

select * from employees;
select * from departments;
--department_id 두개를 연결짓는다
select employee_id, emp_name, department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;

select * from stu_score;
select * from students;
--컬럼 추가
alter table students add no number(38);
--자료 추가
insert into students(no) select no from stu_score;
--rownum으로 만들어진 번호를 no에 넣기
select rnum from(select rownum rnum, a.* from students a); --1
update students b set no = (select rnum from(select rownum rnum,id from students )a)
where a.id = b.id
;
update students b
set no = ()
from(select rownum rnum, id from students)a
;


--홍길동 학생, 학생성적의 모든 내용과 전번, 이메일, 과, 학년
select no, name, kor, eng, math, total, avg, rank, c_date from stu_score
where name='홍길동';

select no,id,a.name,phone,email,major,grade from students a, stu_score b
where a.name='홍길동' and a.name = b.name;

--drop table stu_score;

--equi join
--2개의 테이블 join 1개의 동일한 컬럼이 있어야 한다.
--동일한 컬럼은 중복이 없어야한다, 
--2개 중 한개의 테이블에서는 primary키가 사용되어야 한다.
select a.id, a.name, phone, total, avg from students a, stu_score b
where a.id = b.id
;

--self join
--동일한 테이블 2개를 가지고 서로 join, 상사찾기
select a.employee_id, a.emp_name, a.department_id, a.job_id, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id
order by department_id;

--drop table students;

select * from students;
select * from stu_score;
desc students;
--stu_score, rank 입력하기
update stu_score a
set rank = (select ranks from (select no,id,rank() over(order by total desc) as ranks,rank, total from stu_score)b--2포함,3
where a.no = b.no)
;
--rank
select rank() over(order by total desc) as ranks,rank, total from stu_score--1
select ranks from (select no,id,rank() over(order by total desc) as ranks,rank, total from stu_score)b--1포함,2
;

select * from member;

alter table member add no number;
--rank, id 가져오기
select rownum rnum, id from member;
                        --rownum을 rnum으로 변경, 
update member a set no = (select rnum from(select rownum, a.* from member)b where a.id = b.id)
;

update stu_score set rank=0;
commit;
--total 순으로 내림차순 정렬, =곧 등수를 말함
select total, rank from stu_score
order by total desc;

select total, rank() over(order by total desc) ranks from stu_score;
select row_number() pver(order by total desc) rnum, total from stu_score;

--stu_score, rank 순위를 모두 update하시오
select total, rank() over(order by total desc) ranks from stu_score

;

--update방법
update stu_score set rank = 1
where no=1;
select * from stu_score;
--????????????????????????????????????????
update stu_score set rank=(select rank from(select no, rank() over(order by total desc) ranks from stu_score)
where a.no = b.no)

--
    select * from stu_score order by total desc  --1
    (select rownum rnum,a.* from( select * from stu_score order by total desc )--1+2
    select * from(select rownum rnum,a.* from( select * from stu_score order by total desc ) a) where rnum>=11 and rnum<=20 --1+2+3
;
select * from (
select row_number() over(order by total desc) rnum,a.* from stu_score a
)
where rnum>=11 and rnum<=20
;

--
select employee_id, emp_name,manager_id from employees
order by employee_id;

--self join manager_id, 이름 가져오기
--값이 충족되지 않아도 출력되도록 outer join
--null값이 있는 반대편 항목에 (+)기호를 넣는다
--null값을 만나도 반대편 (+)가 있는 쪽에 추가해줘
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+) -- a에 없는걸 b에 추가한다
;

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

--outer join, 부서번호는 10~110번까지 있다. =employees 10~110
--없는부서(120~270)도 표시는 해주세요. == departments 10~270
-- null값을 추가해줌 (+)
select emp_name,a.department_id, department_name 
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id
;
--부서번호는 10~270까지 있다.
select department_id from departments;

-- ANSI JOIN
select * from employees cross join departments;
select * from employees, departments;

--equi join 동일한 여러가지 방법
select a.department_id, department_name --부서번호, 부서이름을 나타낸다
from employees a, departments b --사원테이블a, 부서b 로부터
where a.department_id = b.department_id 
;
--ansi inner join
select a.department_id, department_name from employees a inner join departments b
on a.department_id = b.department_id
;
--ansi inner join - using 제일 좋은부분
select department_id, department_name
from employees join departments
using (department_id)
;
-- natural join ?????????????????????????????????
select employees.department_id, departments.department_name
from employees natural join departments b;

-- ansi outer join, left outer join, right outer join, full outer join 4가지 가능
select a.emp_name, a.manager_id, b.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id;
--기본 sql left,right,full 불가;;
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id(+) = b.employee_id;


--이름검색 a가 들어간 모두, 10개씩 가져오기
select * from stu_score where id like '%a%'
order by no
;
--row_number() over()
--11~20까지 출력하기
select rownum, id  from stu_score
where rownum >=11 and rownum <=20
;
select rownum rnum a.* from (select * from stu_score)a where rownum >=11 and rownum <=20;

select rownum,a.* from stu_score a order by no;
select row_number() over(order by no) rnum, a.* from stu_score a; -- 1
select *from(select row_number() over(order by no) rnum, a.* from stu_score a where id like '%a%')where rnum >=11 and rnum <=20;


select count(*) from stu_score where id like '%a%';


--멜론
create table melon (
mno number primary key,
rank number,
v_rank number,
img varchar2(300),
title varchar2(100),
singer varchar2(100),
likeNum number --쉼표 빼고 넣어야한다
);

create table yanolja (
yno number primary key,
img varchar2(300),
title varchar2(100),
grade number,
grade_num number,
price number
);
desc melon;
select * from melon;
--drop table melon;

--[1]사원정보(employees)테이블에서
select * from employees;
select * from departments;
--사원번호, 이름, 급여, 부서, 입사일, 상사의 사원번호를 출력하시오
--이때 이름은 이름과 직급을 연결하여 Name이라는 별칭으로 출력하시오
select employee_id, job_id||','||emp_name as name, salary, a.department_id, department_name, hire_date, a.manager_id 
from employees a, departments b
where a.department_id = b.department_id
;

--[2]사원정보(employees)테이블에서
select * from employees;
--사원의 이름과 성은 Name, 업무는 Job, 급여는 Salary, 연봉에 $100 보너스를 추가하여
--계산한 값은 Increase Ann_Salary,
--급여에 $100보너스를 추가하여 계산한 연봉은 Increase Salary라는 별칭을 붙여 출력하시오
select emp_name as name, job_id as job, salary, to_char(salary+100,'$999,999,999') as "Increase Ann Salary",
to_char((salary+100)*12,'$999,999,999') as "Increase Salary"
from employees;

--[ 3 ] H R 부서에서 예산 편성 문제로 급여 정보 보고서를 작성하려고 한다. 
select * from employees;
--사원정보(Employees) 테이블에서 급여가 $7,000~$10,000 범위 이외인 사람의 
--이름과 성(Name으로 별칭) 및 급여를 급여가 적은 순서로 출력하시오(75행).
select emp_name as name, salary
from employees
-- 이내의 범위 where salary >= 7000 and salary <= 10000 
where salary <= 7000 or salary >= 10000  --이외의 범위
order by salary;
-- +@not을 이용한 반대범위
select emp_name,salary from employees
where salary not between 7000 and 10000 --이외의 범위
order by salary;

--[ 4 ] 사원의 성(last_name) 중에 ‘e’ 및 ‘o’ 글자가 포함된 사원을 출력하시오. 
--이때 머리글은 ‘e or o Name’이라고 출력하시오(8행).
select emp_name "as e or o name"
from employees
where emp_name like '%e%o%'
order by emp_name;

--[ 5 ] 이번 분기에 60번 IT 부서에서는 신규 프로그램을 개발하고 보급하여 회사에 공헌하였다. 
--이에 해당 부서의 사원 급여를 12.3% 인상하기로 하였다. 
--60번 IT 부서 사원의 급여를 12.3% 인상하여 정수만(반올림) 표시하는 보고서를 작성하시오. 
--보고서는 사원번호, 성과 이름(Name으로 별칭), 급여, 인상된 급여(Increase Salary로 별칭)순으로 출력하시오(5행).
select * from employees;
select employee_id, emp_name as name, department_id, salary, round(salary*1.123,-1) as "Increase Salary"
from employees
where department_id = '60';

--[ 6 ] 모든 사원의 연봉을 표시하는 보고서를 작성하려고 한다. 
--보고서에 사원의 이름과 성(Name으로 별칭), 급여, 수당여부에 따른 연봉을 포함하여 출력하시오. 
--수당여부는 수당이 있으면 “Salary + Commission”, 수당이 없으면 “Salary only”라고 표시하고, 
--별칭은 적절히 붙이시오. 또한 출력 시 연봉이 높은 순으로 정렬하시오(107행).
select * from employees;
select emp_name as name, salary, commission_pct, to_char(salary*(1+nvl(commission_pct,0)),'$999,999,999') as True_sal,
--case when then
case
when commission_pct is null then 'Salary only'
--when commission_pct is not null then 'Salary+Commission' else대신 이것도 가능
else 'Salary+Commission'
end as "commission sal?"
from employees
order by  salary
;
-- +@ decode
select emp_name as name, salary, commission_pct, to_char(salary*(1+nvl(commission_pct,0)),'$999,999,999') as True_sal,
--decode 사용방법, decode(salary,3000,'A',salary,4000,'B')(컬럼,1조건,1조건해당,컬럼,2아닌조건,2아닌조건해당)
decode(commission_pct, null,'Salary only','Salary+Commission')--(컬럼,조건,해당,외)
from employees
order by salary desc;


--[ 7 ] 각 사원이 소속된 부서별로 급여 합계, 급여 평균, 급여 최댓값, 급여 최솟값을 집계하고자 한다. 
--계산된 출력값은 여섯 자리와 세 자리 구분기호, $ 표시와 함께 아래와 같이 출력하시오. 
--단, 부서에 소속되지 않은 사원에 대한 정보는 제외하고, 출력 시 머리글은 다음 그림처럼 별칭(alias) 처리하시오(11행).
select * from employees;
select department_id, 
to_char(sum(salary),'$999,999') as summ, 
to_char(round(avg(salary),-1),'$999,999') as avgg, 
to_char(max(salary),'$999,999') as maxx, 
to_char(min(salary),'$999,999') as minn
from employees
group by department_id;

--[ 8 ] 사원들의 @직급(job_id)별 전체 급여 평균이 $10,000보다 큰 경우를 조회하여 @업무별 @급여 평균을 출력하시오.
-- 단 업무에 사원(CLERK)이 포함된 경우는 제외하고 전체 급여 평균이 높은 순서대로 출력하시오(7행).
select * from employees;
-- T
select avg(salary) from employees
;
select job_id, avg(salary) salary from employees
--where: 일반컬럼의 조건을 넣는 곳
where job_id not like '%CLERK%'
group by job_id
--having: 그룹컬럼의 조건을 넣는 곳 
having avg(salary)>10000
;

--[ 9 ] 각 사원과 직속 상사와의 관계를 이용하여 다음과 같은 형식의 보고서를 작성하고자 한다.
--(예) 홍길동은 허균에게 보고한다 → Eleni Zlotkey report to Steven King
--어떤 사원이 누구에게 보고하는지 위 예를 참고하여 출력하시오. 
--단, 보고할 상사가 없는 사원이 있다면 그 정보도 포함하여 출력하시오(107행).
--outer join: (+)
--T
select a.employee_id, a.emp_name, a.manager_id, b.emp_name 
--self join 직원 아이디가 관리자 아이디로 들어가야한다
from employees a, employees b
where a.manager_id = b.employee_id(+) --b이름을 a관리자에 입력해줘, (+)null값도 찾아줌
;

--[ 10 ] Employees, Departments 테이블의 구조를 파악한 후 
--사원 수가 다섯 명 이상인 부서의 부서이름과 사원 수를 출력하시오. 
--이때 사원 수가 많은 순으로 정렬하시오(5행).
select * from employees;
select * from departments;
--T
select department_id, count(department_id)
from employees
group by department_id
having count(department_id) >= 5
order by count(department_id) desc -- 사원수가 많은 순서 desc
;

-- [ 추가 ] HR 부서의 어떤 사원은 급여정보를 조회하는 업무를 맡고 있다.
-- Tucker가 포함된 사원보다 급여를 많이 받고 있는 사원의 이름, 업무, 급여를 출력하시오(15행).
select salary from employees
where emp_name like '%Tucker%'
; -- 1. 이름에 Tucker가 들어간 사람의 급여
select salary from employees
where salary > (select salary from employees where emp_name like '%Tucker%') --1.보다 큰 급여
;

-- [ 추가 ] 모든 사원의 소속부서 평균연봉을 계산하여 사원별로 이름, 업무,
-- 급여, 부서번호, 부서평균연봉(Department Avg Salary로 별칭)을 출력하시오(107행).
--T
select department_id, round(avg(salary),2) from employees
group by department_id
;

--부서별 평균급여
select avg(salary) from employees group by department_id;
--부서별 평균급여로부터
select emp_name, job_id, salary, department_id, 
(select round(avg(salary),2) from employees where department_id = e.department_id) as "Department Avg Salary"
from employees e;

--join select를 테이블로 사용 가능하다
select salary,a.department_id,round_salary
from employees a, (select department_id,round(avg(salary),2) round_salary from employees group by department_id ) b
where a.department_id = b.department_id
;
-- equi join
select salary, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id
;

create table daum_movie(
dno number primary key,
title varchar2(100),
img varchar2(300),
audience number(30),
ddate date
);
select * from daum_movie;