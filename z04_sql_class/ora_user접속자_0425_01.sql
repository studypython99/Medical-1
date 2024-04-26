--2024.04.25 수업내용
--어제, 오늘, 내일
select sysdate-1, sysdate, sysdate+1 from dual;
--월의 버림, 월 1일/ 월의 마지막날
select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;
--두 날짜간 일, 월
select trunc(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2)from employees;
--trunc -1: 1단위 버림
select trunc (kor,-1) kor,count(trunc(kor,-1)) from stu_score
--10단위로 그룹지어서 정렬
group by trunc(kor,-1)
order by kor;
--퀴즈 hire_date 날짜에서 월만 출력
--원하는 데이터, count(원하는데이터)
select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm'))from employees
--group by 원하는데이터
group by to_char(hire_date,'mm')
--정렬
order by hire_date;
--Q 연도 출력
--원하는 데이터, count(원하는데이터)
select to_char(hire_date,'yyyy') hire_date, count(to_char(hire_date,'yyyy'))from employees
--group by 원하는데이터
group by to_char(hire_date,'yyyy')
--정렬
order by hire_date;
--형변환: number, character, date
--number 사칙연산0, 쉼표표시x, 원화표시x
--char 사칙연산x, 쉼표표시0, 원화표시0
--date +,-가능, 날짜 출력형태변경x > to_char 형변환 후 sysdate,'yyyy-mm-dd'
--시퀀스 형태로 학번을 부여하시오 stu_seq
--nextval 숫자가 1씩 카운트됨
select SEQ_NO.nextval from dual;
--currval 시퀀스 번호 확인
select seq_no.currval from dual;
select 'ko'||to_char(sysdate,'yyyy')||lpad(stu_seq.nextval,4,0) from dual;
--문자형 (123,456,789,)+(100,000) = 1234235 출력
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',',''))) from dual;
select to_number('123,456,789','999,999,999')+to_number('123,456,789','999,999,999') from dual;
--숫자타입을 날짜타입으로 변경
select 20240425 from dual;
select to_char(20240425) from dual;--문자: 20240425
select to_date(20240425+300) from dual;--날짜: 24/07/25
select emp_name, hire_date from employees where hire_date > to_date(20070101) order by hire_date asc;
select to_char(hire_date, 'mm') from employees;
select emp_name, hire_date from employees where to_char(hire_date, 'mm') = 08 and emp_name like '_a%' order by hire_date asc;
select emp_name, hire_date from employees where hire_date > to_date(20070101) and emp_name like '_a%' order by hire_date asc;
-- 다중 조건 in : 1월, 5월 8월에 입사한 사람
select hire_date from employees where to_char(hire_date, 'mm') in ('01', '05', '08');
-- 이름 두 번째 칸에 a가 들어가는 사람
select emp_name from employees where emp_name like '_a%';
-- 두 조건을 만족하는 사람
select emp_name, hire_date from employees
where to_char(hire_date, 'mm') in ('01', '05', '08') and emp_name like '_a%'
order by hire_date asc;
select sysdate-to_date('20240401') from dual;
select sysdate, '2024-04-01', sysdate - to_date('2024-04-01') from dual;
select * from m_date;
insert into m_date(no, m_yesterday)
values(seq_mno.nextval, '2024-04-01');
create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);
-- 입력 시 날짜타입에 날짜형태의 문자형을 입력해도 가능함.
-- 날짜와 문자를 빼는 것은 불가능, 문자를 날짜타입으로 변경해야함.
insert into eventDate
values(seq_mno.nextval, sysdate, '2024-04-01', sysdate-to_date('2024-04-01'));
select * from eventDate;
-- 숫자타입으로 변경
select to_number('20,000', '99,999') - to_number('10,000', '99,999') from dual;
-- null을 0으로 치환
select salary, commission_pct, salary * (1 + nvl(commission_pct, 0)) as sal from employees;
-- manager_id 에서 null 값을 ceo로 치환
select nvl(to_char(manager_id), 'ceo') as new_id from employees order by manager_id desc;
-- 그룹함수 : sum, avg, count, min, max : 일반 데이터 column하고 사용할 수 없음
-- 그룹 함수의 결과는 하나의 row
-- group by를 이용
-- 개수 count
select count(emp_name) from employees; --107
select count(manager_id) from employees; --106 null 값은 포함되지 않음
select count(*) from employees; -- 전체 행(데이터) 개수를 확인할 때는 asterisk를 사용
-- sum : 총합
select sum(salary) from employees;
-- avg : 평균
select avg(salary) from employees;
-- min : 최소, max : 최대
select min(salary), max(salary) from employees;
-- salary가 평균보다 높은 사람 검색
select emp_name, salary from employees where salary > (select avg(salary) as avg_sal from employees);
-- 평균보다 높은 사람들의 평균 salary
select avg(salary) from (select emp_name, salary from employees where salary > 6461) order by salary desc;
-- 최소 salary를 받는 사람의 사번 이름 출력
select employee_id, emp_name, salary from employees where salary=(select min(salary) from employees);
-- 최대 salary
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);
-- 부서 번호가 50번인 사원만 전체 월급
select sum(salary) from (select department_id, salary from employees where department_id = 50);
desc stu_score;
select no, name, kor from stu_score where kor >= 80 order by kor desc;
-- 국어점수, 영어점수가 각각 평균 이상인 사람 출력
select no, name, kor, eng from stu_score
where kor >= (select avg(kor) from stu_score)
and eng >= (select avg(eng) from stu_score)
order by kor, eng;
create table s_info(
sno number,
s_count number
);
insert into s_info values(stu_seq.nextval, 2000);
select * from s_info;
insert into s_info values(stu_seq.nextval, (select count(*) from stu_score
where kor >= (select avg(kor) from stu_score)
and eng >= (select avg(eng) from stu_score)
));
-- 국어점수 최고인 학생, 영어점수 최고점인 학생, 수학점수 최고점인 학생 출력
select * from stu_score;
select name, kor, eng, math from stu_score
where kor=(select max(kor) from stu_score)
or eng=(select max(eng) from stu_score)
or math=(select max(math) from stu_score);
-- 최고 급여, 최저 급여, 평균 급여와 가장 가까운 사람
select emp_name, salary from employees
where salary=(select max(salary) from employees)
or salary=(select min(salary) from employees)
or salary=(select round(avg(salary), -2) from employees)
order by salary, emp_name asc;
-- 문자함수
-- lpad, rpad : 빈 공백 채우기
select emp_name, lpad(emp_name, 15, '#') from employees;
select emp_name, rpad(emp_name, 20, '-') from employees;
-- ltrim, rtrim : 특정 문자 자르기
select emp_name, ltrim(emp_name, 'Do') from employees where emp_name like 'Do%';
select 'ko20240001', ltrim('ko20240001', 'ko2024') from dual; -- 1
-- substr : 일정 지점부터 문자 자르기
select emp_name, substr(emp_name, 3, 4) from employees;
select employee_id, job_id from employees;
select substr(job_id, 1, 2)|| trim(to_char(employee_id)) from employees order by employee_id asc;
--length
select emp_name, length(emp_name) from employees
where length(emp_name) >= 15
order by length(emp_name) asc;
-- 날짜 함수
-- 날짜 데이터 +, - 숫자는 가능
select sysdate+1 from dual;
select sysdate - hire_date from employees;
--날짜데이터 + 날짜데이터 불가능
select sysdate + hire_date from employees; -- ORA-00975: 날짜와 날짜의 가산은 할 수 없습니다.
select round(sysdate, 'month') from dual; -- 24/05/01
select trunc(sysdate, 'month') from dual; -- 24/04/01
select round(sysdate, 'year') from dual; -- 24/01/01
-- x개월 후 계산
select sysdate, add_months(sysdate, 3) from dual; -- 24/07/25
select sysdate, add_months(sysdate, -2) from dual; -- 24/02/25
-- 올림, 버림, 나머지, 지수함수
select ceil(-4.2), floor(-4.2), mod(8, 3), power(2, 10) from dual;
select * from employees;
select emp_name || ' ' || to_char(hire_date, 'yyyy"년"mm"월"dd"일"day') from employees
order by hire_date asc;
select emp_name || ' ' || to_char(hire_date, 'yyyy')|| '년'
|| to_char(hire_date, 'mm')||'월'
|| to_char(hire_date, 'dd')||'일'
|| to_char(hire_date, 'day') as emp_hire_info
from employees order by hire_date asc;

--Q 사원명, 자리수 9자리 빈공백 0으로 표시
--salar*1400 앞에 원화표시와 쉼포를 넣어 출력하시오
select salary, to_char(salary*1400,'L000,000,000') from employees;

--자신의 생일과 자신의 생일이 속한 달의 마지막날짜
--'2010-10-10'
select '2010-10-10', last_day('2010-10-10') from dual;-- 10/31
select '2010-10-10', trunc(to_date('2010-10-10'),'month') from dual;-- 10/01

select*from member;

desc member;

-- DDL(date definition language)컬럼 추가
--commit, rollback 안됨; 바로 저장됨
alter table member add gender varchar2(6) default 'Female' not null;
desc member;
--컬럼 수정: 컬럼이름변경, 타입변경
alter table member rename column name to stu_name
;
--컬럼 타입변경
alter table member modify(stu_name varchar2(50));
--기존의 데이터가 변경하려는 크기보다 작을 때만 가능
update member set stu_name='홍';
alter table member modify(stu_name number(100);
--컬럼의 타입을 변경하려면 빈공백ㅇㅣ나 null어야 한다.
alter table member modify(stu_name number(4);

desc member;
--컬럼 삭제
alter table member drop column phone;
desc member;
select*from member;
commit;