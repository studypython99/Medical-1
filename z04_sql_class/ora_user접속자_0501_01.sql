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