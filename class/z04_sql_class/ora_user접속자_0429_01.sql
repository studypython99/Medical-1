
--무결성 제약조건: 부적합한 자료가 입력되지 않도록 하기위한 규칙.
--not null, unique, primary key, foreign key, check
create table member(
memno number(4) not null,
id varchar2(30) primary key,
pw varchar(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in ('남자','여자')),
mdate date default sysdate
);

--데이터 입력, 출력, 수정, 삭제
insert into member (memno,id,pw,name,gender,mdate) values(
1,'aaa','111','홍길동','남자',sysdate
);
insert into member(memno,id,pw,name,gender) values(
2,'bbb','111','유관순','여자'
);
select*from member;

--테이블 생성
create table board(
bno number(4) primary key,
id varchar2(30), -- 외래키 등록
btitle varchar2(1000),
bcontent varchar2(1000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- 외래키(foreign key)의 별칭 : fk_id
references member(id) -- member table의 primary key 로 id가 되어있을 때 외래키 등록
);

--primary key를 삭제하려면 foreign key 등록되어 있는 데이터를 우선 삭제해야함
--primary key 삭제되면 모두삭제 -on delete cascade
--                    모두존재 - on update cascade
--데이터 입력
insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','제목입니다','내용입니다.',sysdate,board_seq.currval,0,0,1,''
);
--데이터 입력
insert into board values(
board_seq.nextval,'aaa','제목입니다3','내용입니다.3',sysdate,board_seq.currval,0,0,1,''
);

select*from board;
select*from member;
--삭제
delete board where bno=3;
commit;

delete member where id='aaa';


--decode(switch일치하는지 여부 확인), case(if조건문 사용가능) 논리연산자
--decode조건문
select emp_name, department_id,
decode(department_id,
10,'총무기획부',
20,'마케팅',
30,'구매/생산부',
40,'인사부'
)
from employees
order by department_id asc;

select department_id, department_name from departments;

select *from stu_score
order by avg desc;
--90a 80b 70c, like 사용불가
select avg, decode(avg,
'9%','A',
'8%','B',
'7%','C',
)
from stu_score
order by avg asc;

--sh_clerk*15%, ad_asst*10% MK_rep*5%;
--decode, like사용불가
select*from employees;
select job_id,salary,
decode(job_id,
'%CLERK', salary*(1.15),
'%ASST', salary*(1.10),
'%REP', salary*(1.05)
) as sall
from employees
order by job_id asc;

--job_id, clerk이 들어가있는 job_id를 검색하시오
select job_id from employees;
select job_id from employees
where job_id like '%clerk';

--case문
select name, avg from stu_score;

select name, avg,
case 
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
else 'F'
end as grade
from stu_score;


select department_id, department_name from departments;
--case구문, department_id 이름
select department_id from employees
order by department_id asc;

select department_id, department_name,
case
when (select department_id from departments) = (select department_id from employees)
then (select department_name from  departments)
end as ii
from departments;

--월급을 출력하시오
--job_id
--clerk 포함: salary*15%, ad_asst*10%, rep포함*5%, man포함*2%
--case
select job_id, salary from employees;
select job_id, salary,
case
when job_id like '%CLERK' then salary*1.15
when job_id like '%ASST' then salary*1.10
when job_id like '%rREP%' then salary*1.05
when job_id like '%MAN%' then salary*1.02
end as sal_up
from employees
order by job_id asc;

--월급 평균 이하는 0.15, 평균이상 0.05% 인상해서 출력하세요
--case 여러개 사용하기
select emp_name,
case
when salary > (select avg(salary) from employees) then 'up'
else 'down'
end as sal_updown
,
case
when salary > (select avg(salary) from employees) then salary*1.05
else salary*1.15
end 
from employees;

--rank
select total, rank from stu_score
order by total desc;
--order by total desc의 형태로 rank()를 정의
select total,rank,rank() over(order by total desc) from stu_score;
--rank update
update stu_score a
set rank = (
select ranks from(
select no, rank() over(order by total desc) as ranks from stu_score
) b
where a.no = b.no
)
;
commit;
select no, rank from  stu_score
order by no asc;
-----------------------------------------------------------
--join

select department_id, department_name from departments;
select emp_name,department_id from employees;
-- 두개 테이블 조인
select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id;

--그룹함수: sum, avg, count, max, min stddev표준편차, variance분산

--월급 총합
select sum(salary) from employees;
--국어점수 합계
select sum(kor) from stu_score;

select count(*) from employees; --107
select count(*) from employees
where department_id = 50; --45

--커미션을 받는 사원의 수
select count(commission_pct) from employees; --35
select emp_name, commission_pct from employees
where commission_pct is not null; --35

--group by, 그룹함수에만 쓰인다
--전체 사원 수
select count(*) from employees;
--부서번호 50번 사원 수
select count(*) from employees
where department_id = 50;
--부서번호별로 사원 수
select department_id, count(department_id) from employees
group by department_id
order by department_id asc;

--avg grade
--stu_score 90점이상 A, 80점이상 B, 70점이상 C, 60점이상 D, 나머지 F
select*from stu_score;

select grade, count(grade)
from(select avg,
case
when avg like '9%' then 'A'
when avg like '8%' then 'B'
when avg like '7%' then 'C'
when avg like '6%' then 'D'
else 'F'
end as grade
from stu_score) 
group by grade;

--kor 10점대별로 출력
--trunc(kor,-1)을 사용한 group by
select trunc(kor,-1), count(trunc(kor,-1))from stu_score
group by trunc(kor,-1);
--as k_kor, as k_count 로 변경하기
select k_kor, count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score) --10점대별로 출력한 별칭을 사용
group by k_kor;

--그룹지어져 있어야한다. 그룹함수 group by 사용
select department_id,count(*) from employees
group by departnemt_id
order by department_id;

select emp_name,count(emp_name) from employees
group by emp_name;

--부서별 평균 월급을 구하시오
select * from employees;
--부서를 기준으로
select department_id,round(avg(salary),2) from employees
group by department_id
order by department_id;

--CLERK이 포함되어있는, REP, MAN 별 월급 평균
select job_id from employees;
select job_id, round(avg(salary),2)
from (select job_id from employees
where job_id like '%CLERK%')
group by job_id
order by job_id;

select job_id from employees
where job_id like '%CLERK%';

-- clerk이 포함된 갯수들
select job_id,count(job_id) from employees
where job_id like '%CLERK%'
group by job_id;

--clerk만 출력되도록
select substr(job_id,4,7) from employees;
select job_id,substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7),count(substr(job_id,4,7)) from employees
where substr(job_id,4,7)='clerk'
group by substr(job_id,4,7);

select substr(job_id,4,7),count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id,4,7)
order by c_job_id;

--부서별(group by department_id) 최대,최소,평균월급 출력
select nvl(department_id,0), count(salary), max(salary), min(salary), round(avg(salary),2) from employees
where department_id is not null
group by department_id
order by department_id;

--+@ 부서명도 같이 보고싶다.
select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

--부서별 사원 수, 커미션을 받는 사원 수 출력

--부서별 사원 수
select*from employees;
select department_id, count(department_id), count(commission_pct) from employees
where department_id is not null
group by department_id;


--단일그룹의 함수가 아닙니다 라는 오류, group by 있어야한다
select*from employees;
select department_id, count(department_id), count(commission_pct) from employees
where department_id is not null;

--having: group by 조건절, where: 일반 컬럼의 조건절
select department_id, round(avg(salary),2) from employees
group by department_id;

--emp_name 두번째가 a로 시작하지 않는것만
select emp_name from employees
where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000;

--평균월급보다 작은 그룹의 평균만 출력
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'--일반조건
group by department_id
having avg(salary) >= (select avg(salary) from employees); --그룹조건

--부서별 최대월급이 8천 이상인 부서, 최대월급 출력
select nvl(department_id,0), max(salary) from employees
group by department_id
having max(salary) >= 8000
order by department_id;

--join rdbms, 관계형db
select emp_name, department_id,salary from employees;

select department_id, department_name from departments;

select *from employees, departments;

select count(*) from employees; --107
select count(*) from departments; --27

--equi join
--두 테이블 간 같은 컬럼을 가지고 비교해서, 해당되는 데이터를 출력
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id;

select department_id, department_name from departments;

select*from member;
select*from board;

-- board의 id를, member의 name으로 변경하기
select bno,name,btitle,bcontent, bdate, bgroup, bstep, bindent, bhit, bfile from board, member
where member.id = board.id
;

update member set name='홍길자'
where id = 'aaa';
select * from member;

select *from stu_score;
select*from employees;
select department_id, avg(salary), max(salary), min(salary) from employees
        group by department_id
        ;
select name, avg,
case
when avg >= 60 then '60이상'
else '60이하'
end as grade
from stu_score
order by grade;

--사원번호, 사원명, 부서번호, 부서명
select employee_id, emp_name, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id;

--그리고, 이름 두번째 자리에 a가 들어가는 사원
select emp_name from employees
where emp_name like '_a%';

--월급이 평균이상인 사람
select salary from employees
where salary >=(select avg(salary) from employees);

select*from employees;
select*from jobs;
select*from departments;
--사원번호, 사원명, 부서번호, 부서명, 직급번호, 직급명 출력
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id;

--사원번호, 사원명, 월급 ,최소월급분, 직급, 직급타이틀
--최소월급 몇% 이상을 받고 있는지 출력
select employee_id, emp_name, salary, min_salary,
round(((salary-min_salary)/salary)*100,2)||'%', a.job_id,job_title
from employees a, jobs b
where a.job_id = b.job_id;

select job_id, job_title from jobs;

--job_title, manager 글자가 들어가 있는
--사원번호e, 사원명e, 직급번호e, 직급명j, 월급e, 최대월급j을 출력하시오???????????????????
select*from employees;
select*from jobs;
select*from departments;
select employee_id, emp_name, b.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id = b.job_id and job_title like '%manager%';

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);
commit;
select*from stu_grade;
select avg from stu_score;
--case when dhen grade컬럼 90점이상 A...bcdf 학점출력
select no,name,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_grade, stu_score;

--non equi join
select no,name,avg,grade
from stu_score,stu_grade --같은 컬럼이 없다, 그렇지만 join해보겠다: non equi join
where avg between low_score and high_score
order by no
;

update stu_grade set low_score=92
where grade = 'A';

--월별매출액 기준으로 고객등급
select*from kor_loan_status;
--지역별 대출 합계를 출력하시오
select region, gubun, to_char(sum(loan_jan_amt),'999,999,999')||'억원'
from kor_loan_status
group by region, gubun
order by region
;
--년도별,지역별,대출합계금액
select*from kor_loan_status;
select substr(period,1,4),region, to_char(sum(loan_jan_amt),'999,999,999')||'억원'
from kor_loan_status
group by substr(period,1,4), region
order by region
;
--시간대별,연령대별 판매량 총 합을 출력하시오
select *from lotte_product;
select time_cd, age_cd, sum(purh_amt) a
from lotte_product
group by time_cd, age_cd
order by a desc
;
--이름별,금액합계 출력
select*from shop_product;

select name, sum(amount)
from shop_product
where pdate>= '2024/03/01'
group by name
;
--customer_rank 테이블 생성
--rank, 100만 미만: bronze / 200만 미만: silver / 300미만: gold / 300만이상: platinum
create table customer_rank(
rank varchar2(2) primary key,
low_amount number(30) not null,
high_amount number(30) not null
);
insert into customer_rank values(
'B',0,999999
);
insert into customer_rank values(
'S',1000000,1999999
);
insert into customer_rank values(
'G',2000000,2999999
);
insert into customer_rank values(
'P',3000000,9999999999999
);
commit;

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
