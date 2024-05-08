--테이블 생성
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--테이블 구조 및 데이터 복사하기
desc employees;
create table emp02 as --2. emp02에 입력
select*from employees; --1. 여기의 전부를

--따라서, 아래 두개는 같다.
select*from emp02;
select*from employees;

--테이블 구조만 복사하기
create table emp03 as --2. 구조는 같도록 하자
select *from employees where 1=2; --1.하나도 안맞아서 가져올 수 없지만
--emp03은 구조0내용x
select*from emp03;
select*from employees;

--테이블이 존재하면서, 데이터만 복사하기, 테이블 구조가 다를 때
insert into emp01(emp_id,emp_name,hire_date)
select employee_id,emp_name,hire_date from employees;

select*from emp01; --컬럼 3개
select*from employees; --컬럼 14개
--1개 데이터 추가
insert into emp01 values(
207,'홍길동','2024-04-26'
);

--테이블이 존재하면서, 데이터만 복사하기
insert into emp03
select*from employees;

select*from emp03;
select*from emp01 order by emp_id desc;
select*from employees;

select*from emp01 order by emp_id desc;

--drop table s_info;
--drop table m_date;
desc member;

--컬럼 타입변경
alter table member
modify(stu_name varchar2(30));

--컬럼 삭제
alter table member
drop column pw;
desc member;

--컬럼 추가, 마지막줄에 추가추가
alter table member
add(pw varchar2(30));
desc member;

select*from member;

select mno,id,pw,stu_name,gender from member;
select*from member;

insert into member values(
seq_mno.nextval,'ggg','1111','홍길자','male' --이렇게하면 에러,(형식이 다르면)
);

--컬럼의 순서를 바꾸고싶다, 숨긴 후 추가
alter table member modify stu_name invisible; --stu 숨기기
alter table member modify gender invisible; --gen 숨기기
alter table member modify stu_name visible; --stu 나타나기
alter table member modify gender visible; --gen 나타나기
select*from member;
--컬럼 일시적 사용제한
alter table member
set unused(id);--id 사용안함
--사용제한 해제
alter table member
drop unused columns; --컬럼 사용안함을 지운다
select*from member;

--테이블삭제
--drop table emp03;

--테이블이름 변경
rename emp01 to employees01;

--무결성 제약조건

--foreign key는 다른 테이블에서 데이터 입력시,
--선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인
