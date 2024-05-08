--갖고있는 테이블 검색
SELECT
    * FROM tab;
    
select*from employees;    --f9: 한줄만 실행, f5: 전체실행

--테이블 구조 확인
desc employees;

--테이블 생성
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2) --xxx.xx 총 5자리, 
);
--칼럼(no,kor,eng,avg)을 모두 입력함
insert into stu_score(no,kor,eng,avg) values (
1,100,99,(100+99)/2
);
--칼럼을 생략가능
insert into stu_score values(
2,95,98,(95+98)/2
);

select*from stu_score;

create table num(
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);
select*from num;

--현재 날짜
--dual: 가상테이블
select sysdate from dual; --24/04/18

--날짜 포맷 변경: to_char 형변환>>포맷 지정,'yyyy-mm-dd HH:mi:ss'
select to_char(sysdate,'yyyy-mm-dd HH:mi:ss') from dual;--2024-04-18 01:07:52

select to_char(sysdate,'HH:mi:ss') from dual;

select sysdate+100 from dual; --24/07/27
select sysdate+1000 from dual; --27/01/13
select sysdate-to_date('24/01/01') from dual;--108.xx