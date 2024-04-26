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

--foreign key, 외래키 , ex) 게시글 작성후, 댓글 추가, 게시글 삭제시 댓글도 모두 삭제
--drop table emp01;

--emp01 테이블 생성
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);
--emp01 empno 타입변경
alter table emp01
modify (empno number(6));
alter table emp01
modify (deptno number(6));

--dept01 테이블 생성
create table dept01(
deptno number(2) primary key,
dept_name varchar2(20)
);
--칼럼의 타입 변경
alter table dept01
modify(dept_name varchar2(80)); --가져오려는 값이 더 크다, 담을 수 없었다 
--칼럼 내용 추가
insert into dept01(deptno,dept_name)
select department_id, department_name from departments;

insert into emp01 values(
1,'홍길동','0001',10
);
insert into emp01 values(
2,'유관순','0002',20
);
insert into emp01 values(
3,'이순신','0002',30
);

--deptno 10~270까지 있다
insert into emp01 values(
4,'김구','0003',270
);
insert into emp01 values(
5,'강감찬','0004',280 --270번까지 있으니 등록불가;
);-- 외래키 삭제 후 입력가능;

--foreign key 삭제 후 입력해보기
alter table emp01
drop constraint fk_deptno;
commit;

--emp01 foreign key 추가: fk_deptno라는 이름으로 deptno를 foreign key로 등록할거야
--fk_deptno별칭
--add constraint 별칭 foreign key(현재컬럼) references 다른테이블(컬럼이름)
alter table emp01
add constraint fk_deptno foreign key(deptno)
REFERENCES dept01(deptno);

select*from departments;

desc member;
--
create table board(
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);
insert into board values(
1,'aaa','게시글1','내용1'
);
insert into board values(
8,'bbb','게시글8','내용8' -- 2~8까지 입력
);
commit;
select*from board;

--foreign key 만들기
alter table board
add constraint fk_id foreign key (id)
references member(id);

--comment 테이블 댓글테이블

--cno number(4) primary key
--bno number(4) #테이블등록 후 foreign key 등록하기
--cpw varchar2(20)
--ccontent varchar2(1000)

create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);
drop table ccomment; --alter 할거면 지우고 다시하자..

--댓글달기 15 21 35 42 55
insert into comments values(
5,5,'1111','댓글내용1'
);
-- fk를 등록할 때 설정, 
-- fk키로 등록되어있는 모든 데이터 삭제
-- fk키로 등록되어있는 모든 데이터 존재
delete board where bno=5;
commit;

--외래키 삭제
alter table board drop constraints fk_id;
select*from board;
select*from comments;

delete board where bno=1; --무결성 위배,
--fk_cno가 삭제가 되도록 함.
alter table comments 
add constraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

delete comments where cno=2;

--check 제약조건, 특정값의 범위, 특정값만 입력되도록 함 ex) male/female
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', --컬럼에 데이터를 넣지 않으면 자동으로 0001 저장됨
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('남자','여자'))
);

insert into emp(empno,ename,job,sal,gender) values(
1,'홍길동','0002',3000,'남자'
);
insert into emp(empno,ename,job,sal,gender) values(
2,'유관순','0003',4000,'여자'
);
insert into emp(empno,ename,job,sal,gender) values(
3,'이순신','0004',5000,'중자' --gender 제약조건 위배됨.
);
insert into emp(empno,ename,job,sal,gender) values(
4,'강감찬','0005',2000,'남자'
);
insert into emp(empno,ename,job,sal,gender) values(
5,'김구','0006',1000,'남자' --sal 2000~20000 사이값만 가능
);
insert into emp(empno,ename,sal,gender) values(--job제거
6,'김유신',3000,'남자' -- job 0001 디폴트 설정
);
select*from emp;