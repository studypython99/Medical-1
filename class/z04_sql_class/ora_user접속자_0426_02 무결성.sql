--무결성 제약조건

--foreign key는 다른 테이블에서 데이터 입력시,
--선언되어 있는 기존 테이블에 입력하려는 데이터가 있는지 확인
--지정된 데이터만 들어올 수 있도록 한다.

--drop table employees01;
--drop table emp02;
--drop table member;
--drop table board;

create table member(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','홍길동','male'
);

insert into member (id,pw,name) values(
'bbb','1111','유관순');

insert into member(id,pw) values(
'ccc','1111');

insert into member (id,pw,name) values(
'a','1111','홍길동');

select*from member;
--제약조건: not null: null값만 제외, 중복은 가능!
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
insert into emp02 (empno,ename,job,deptno) values(
'1111','홍길동','aa','11'
);
insert into emp02 (empno, ename, job, deptno) values(
'2222','홍길자','bb','22');
insert into emp02 (empno, ename) values(
'3333','홍길순');
select*from emp02;
--제약조건: unique: 중복만 제거, null허용
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
insert into emp03 (empno,ename,job,deptno) values(
'1111','홍길동','aa','11'
);
insert into emp03 (empno,ename,job,deptno) values(
null,'홍길동','aa','11'
);
insert into emp03 (empno,ename,job,deptno) values(
'3','이순신','aa','11'
);
select*from emp03;

--1번의 홍길동을 찾아라
select * from emp03
where empno='1111';
--null홍길동을 찾아라
select*from emp03
where empno is null and ename='홍길동'; -- empno = null ;; 이거 안됨;;

--null값을 어떻게 처리할것인가. 결측치처리!!
create table emp01(
empno number(4) primary key, --번호만 검색해서 찾을 수 있다. 중복허용x
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

--5개 null,1,2,3,1
insert into emp01 values(
1,'홍길동','0001',1
);
insert into emp01 values(
3,'홍길동','0001',1
);

select*from emp01;
--3번홍길동 찾기
select*from emp01
where empno=3;