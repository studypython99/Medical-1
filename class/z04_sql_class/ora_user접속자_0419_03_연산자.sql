create table stu_score (
 no number,
 name varchar2(30),
 kor number(3),
 eng number(3),
 math number(3),
 total number(3),
 avg number(5,2),
 rank number
);
insert into stu_score values (
1,'홍길동',100,100,100,300,100,1
);
insert into stu_score values (
5,'김구',100,100,100,300,100,1
);
commit;
select * from stu_score;

--산술연자 number타입인 경우
select*from stu_score;

insert into stu_score values(
6,'김유신',100,95,96,(100+95+96),(100+95+96)/3,1
);

--번호,이름,국어,국어-20,평균,국어-20을 계산한 평균
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select*from employees;
--환율계산 1달러: 1381.79원
select employee_id,emp_name,salary,salary*138.79 from employees;

--commission_pct, 실제월급: 월급+(월급*commission)
select*from employees;

select emp_name, salary, salary*(1+nvl(commission_pct,0)) from employees;
--nvl(컬럼,0)
select employee_id,emp_name,nvl(commission_pct,0) from employees;