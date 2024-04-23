--10번도 아니고 50번도 아닌, not != <> ^=
select department_id from employees
where department_id != 10 and department_id != 50
order by department_id;

--5000이상 9000이하
select salary from employees
where salary >=5000 and salary <=9000
order by salary
;

--평균이 99점 이상인 학생을 검색
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1111-1111'
);
insert into member values (
'bbb','1111','유관순','010-2222-2222'
);
insert into member (id,name,phone) values(
'ccc','이순신','010-3333-3333'
);
select*from students;

--no= 1의 이름을 홍길동 으로 변경
update students set name='홍길동'
where no=1;

update students set name='유관순'
where no=2;

update students set name='이순신'
where no=3;

update students set name='강감찬'
where no=4;

update students set name='김구'
where no=5;

update students set name='좌의정'
where no=6;

update students set name='영의정'
where no=7;

update students set name='이익'
where no=8;

update students set name='정약용'
where no=9;

update students set name='이세돌'
where no=10;

--국어 80, 평균 85점 이상인 학생을 출력
select no, name, kor, avg from students
where kor>=80 and avg >=85;

--국어 70,80,90점 학생출력
select no, name, kor from students
where kor=70 or kor=80 or kor=90;

update students set kor = 100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;

select *from students
where no=1;

--국어점수가 70~90점 학생출력
select no, name, kor from students
where kor>=70 and kor<=90;

--between a and b, a와 b 사이(이상이하)
--not: between 이외 (미만초과)
select no, name, kor from students
where kor not between 70 and 90;

--날짜도 between a and b
select hire_date from employees
order by hire_date;
--99년보다 크거나 같고, 01년보다 작거나 같은 사원
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date;

--in: 동일한 필드가 여러 값중에(70,80,90) 하나를 검색할 경우 or
select name,kor from students
where kor in(70,80,90);

--이름검색
select*from students
where name='홍길동';
--like: 특정단어가 포함되어있는 것을 검색 
--홍 이라는 글자가 있다면 나타내라
select*from students
--where name like '홍%';--홍으로 시작하는
--where name like '%홍';--홍으로 끝나는
--where name like '%홍%';--홍'포함되어있는 단어
where name like '%홍%';

-- _: 한칸 공간을 사용
select*from students
where name like '_길%';
--3번째에 t 가 들어가있는 이름
select*from students
where name like '__t%';

--이름이 4자리인, 3버째 r이 들어가 있는 이름 검색
select*from students
where name like '__r_';
--4자리인 이름
select name from students
where length(name) =4;

--이름이 A로 시작되는

select*from students
where name like 'A%';

--이름에 a가 들어가 있는
select*from students
where name like '%a%';

--대소문자 구분없이 a가 들어있는 학생
--소문자 치환(lower), 대문자 치환(upper), 첫글자 대문자(initcap)
select*from students
where lower (name) like '%a%'

--a가 포함되지 않은 이름
select *from students
where name not like '%a%';

select mamager_id from employees;
--manager_id 100인 사원 검색
select employee_id, emp_name,manager_id from employees
where manager_id=100;

select employee_id, emp_name, manager_id from employees
where manager_id = null; --null검색 안됨;;

select employee_id, emp_name, manager_id from employees
where manager_id is not null;

--정렬 asc(ascending), desc(descending) 한글도 가능

select*from students
order by name asc;

--1차: 국어역순정렬, 2차: 영어순차정렬
select*from students
order by kor desc, eng asc;

--total로 역순정렬
select*from students
order by total desc;

--컬럼 추가 rank
alter table students add rank number(3);
--rank항 값 0으로 변경
update students set rank=0;
--적용
commit;

--등수, 보여주기만 하고 저장은 안됨;;
select no, name,total,rank() over(order by total desc) as rank from students;

--수정, 1번 13등으로
update students set rank=13
where no=1;

-- 등수
select no,rank() over(order by total desc) as rank from students
;
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;
select * from students;

-- 등수
select no,rank() over(order by total desc) as rank from students
;
--이중쿼리;;;;
update students s1 set rank = (select ranks
from (select no, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no )
;
select * from students;

--전체중에서 국어 70이상
select*from students
where kor>=70;
--평균 80이상 중에서 국어 70이상
select*from (select*from students where avg>=80)
where kor>=70;

select*from students;
------------------------------------------------------------------------------
--복습, rank() 순위 전체를 말함; 
select total, rank() over(order by total desc) rank
from students;
--total을 0으로 변경
update students set total=(kor+eng+math);
--이중쿼리구문 students=a로(등수가 total로 정렬된) ,b로(기존의 12345)
--같은 번호자리에 등수를 입력한다.
update students a set rank=(select no, rank() over(oder by total desc) rank
from students b where a.no=b.no);
--1.update 구문
update students a set rank=(rank);

--2. no, rank() 구문, 하나의 테이블b 로 사용
(select no, rank() over(order by total desc) ranks from students) b;

--3. update 구문과 rank() 구문을 no컬럼으로 비교, rank컬럼을 검색
update students a set rank(
select ranks from (select no, rank() over(order by total desc) ranks from students) b
where a.no = b.no
);
--역순정렬
select no,total,rank from students
order by total desc;
--no순차정렬
select no,total,rank,rank from students
order by no;

select no,kor,eng,math,total rank from seudents;
order by kor desc, eng asc;

select manager_id from employees
order by manager_id;

select hire_date from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math)from students;

--입사일로 오름차순 컬럼: 사원,사원명,job_id, 입사일
select*from employees;
select employee_id, emp_name, job_id, hire_date from employees;

--급여를 적게 받는 사람순으로 출력, 월급이 같으면 사원명으로 순차정렬
select employee_id, emp_name, salary from employees
order by salary asc, emp_name;

select *from students;

--숫자함수
--abs: 절대값, 음수값을 내면 안되는 경우 사용.
select -10, abs(-10) from dual; -- -10, 10
--floor: 버림, round: 반올림, ceil: 올림
select 34.789, floor(34.789), round(34.789), ceil(34.789) from dual;
--round 소숫점 자리수 지정하기: round(대상,자릿수)
select 34.178, round(34.178), round(34.127,2) from dual;

select avg from students;
select round(avg,2) avg from students;
--round(n,-1) 정수부분 1의자리 반올림
select 23.5678, round(23.56789,-1) from dual;

--trunc 지정한 자리수 이하 버림
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

--올림
select ceil(34.123) from dual;

--국어점수 일단위 절사해서 10단위 출력
select *from students;
select no, name, trunc(kor,-1) kor from students;

--국영수 일단위 절사 후 합계 출력
select*from students;
select no, name, trunc(kor,-1)k, trunc(eng,-1)e, trunc(math,-1)m ,
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) total
from students;

--mod 나머지
select round(100/7,2) from dual;--나누기
select mod(10,7) from dual; --10을 7로 나눈 나머지값은? 3

--퀴즈. 사원번호가 짝수인것을 출력하시오
select *from employees;
select employee_id from employees
where mod(employee_id,2) = 0; -- if문과 동일하게 사용 가능

--퀴즈 학번 3의배수만 출력
select *from students;
select no, name from students
where mod(no,3)=0; --3으로 나눈 나머지값이 0인것 = 3의 배수

--시퀀스
CREATE SEQUENCE seq_no
       INCREMENT BY 1 --1씩 증가
       START WITH 1 --1부터 시작
       MINVALUE 1 -- 최소값
       MAXVALUE 9999 --최대값
       NOCYCLE --순환x
       NOCACHE --캐시사용x
       NOORDER;
--nextval 숫자가 1씩 카운트됨
select SEQ_NO.nextval from dual;

--currval 시퀀스 번호 확인
select seq_no.currval from dual;

--drop table member;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select seq_mno.nextval from dual;
insert into member values(
seq_mno.nextval,'eee','1111','김구','010-1111-1111'
);
select*from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;
--s0000 라는 형태로 자리수를 늘림, to_char: 날짜, 숫자 데이터를 문자데이터로 변환
select 's'||to_char(seq_mno.nextval,'00000') from dual;

--퀴즈, 한국대학교 ko202400001
--시퀀스 seq_kono 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
noorder;
--trim() 공백제거 to_char 데이터를 문자데이터로 변환
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;

--게시판
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10) --조회수
);

--시퀀스 생성
create sequence  seq_deptno
increment by 10
start with 1
minvalue 1
maxvalue 99999
cycle
nocache
;
select SEQ_DEPTNO.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar(30),
hire_dated date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 999
nocycle
nocache;


insert into emp01 values(
empseq.nextval,'유관순',sysdate
);
select*from emp01;

select*from employees;

--현재까지 입사한 일수(소수점 올림ceil)를 함께 출력하시오 ||'일' concat 문자열 합치기
select employee_id, emp_name, job_id,ceil(sysdate-hire_date)||'일' from employees;


--입사일 오름차순
select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

select emp_name from employees;

--직급과 사번을 합쳐서 출력하시오
select*from employees;
select job_id||employee_id from employees;

--substr: 문자열 자르기 함수, substr(대상,시작,갯수)
select emp_name,substr(emp_name,1,3) from employees;--1번부터 3글자
select substr('abcd',2,3)from dual; --2번부터 3글자

--job_id 앞의 2개 문자와 사번 5자리
select substr(job_id,1,2)||lpad(employee_id,5,0) from employees;
--trim(to_char(employee_id,'00000'))

--s날짜함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
--두 날짜 사이의 개월수 확인
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;
--add_month(현재날짜,+개월수)
select sysdate, add_months(sysdate,2) from dual;
--현재를 기준으로 다음에 오는 월요일 24/04/29
select next_day(sysdate,'월요일') from dual;
--입력한 기준으로 마지막 일을 알려줌.
select last_day(sysdate) from dual;--24/04/30
select last_day('2024-02-21') from dual;--24/02/29