select*from employees;

--회원정보 테이블 생성
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
--데이터 입력
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1010-1010'
);

insert into member values (
'aaa','1111','유관순','010-1010-1010'
);

insert into member (id,name,phone) values (
'ccc','이순신','010-1010-1010' --한글은 한글자당 3자리 차지한다.
);
/*컬럼 수 부족 에러 
insert into member values (
'ddd', '강감찬','010-4444-4444'
);*/

select id,pw,name,phone from member;
--저장
commit;

rollback;

select*from member; --모든자료 검색
select id,name from member; --선택자료 id,name 검색

insert into member values(
'ddd','111','강감찬','010-2020-2020'
);

--멤버 전체 비밀번호 2222 변경
update member set pw='2222' where id='ccc';
select*from member; --모든자료 검색

--모든테이블
select*from tab;

--테이블 타입 확인
desc member;

--오라클 타입
--number(숫자), date(날짜), char(고정문자), varchar2(가변문자),clob(대용량문자)

--number: 정수, 실수
--number(4): -9999 ~ +9999
CREATE table mem(
no number,--길이지정x
no2 number(4),--4자리까지
no3 number(4,2)--xx.xx 소숫점 2자리를 할당하시오.
);

insert into mem (no,no2,no3) values (11,12,13.13);
insert into mem (no,no2,no3) values (21,22,23.23);
insert into mem (no,no2,no3) values (31,32,33.33);

select*from mem;
commit;
------------------------------------------------------------------
create table mem2(
no number(4,2),
mdate date,--연월일시분초 까지 저장 가능
mdate2 timestamp --date=timestamp(밀리초까지 저장 가능 1초=1000)
);

insert into mem2(mdate)values('2024-04-19');
select*from mem2;
insert into mem2(mdate)values(sysdate);--sysdate: 현재시간
insert into mem2(mdate2)values(sysdate);--sysdate: 현재시간
insert into mem2(mdate, mdate2)values(sysdate,sysdate+30);

select*from mem2;
select to_char(mdate,'yyyy-mm-dd hh24:mi:ss')from mem2;
select to_char(mdate2,'yyyy-mm-dd hh24:mi:ss:ff')from mem2;

select * from mem2;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

--문자형을 저장 char, varchar2
--char: 고정문자, 속도가 빠르다
insert into mem3 (tel) VALUES ('12345678');
insert into mem3 (tel) VALUES ('87654321');
insert into mem3 (tel) VALUES ('123');
insert into mem3 (tel) VALUES ('123456789');

--varchar2: 가변문자
insert into mem3 (name) values ('123456789');
insert into mem3 (name) values ('홍길동');
insert into mem3 (name) values ('신사임'); --12자리 필요
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');

select upper(name) from mem3 where (name)='aaa';

--select: select,from 으로 구성됨, 대소문자 구분x
select*from mem,mem2; --모든 컬럼을 출력

select department_id from employees;
