--2024.04.25 ��������
--����, ����, ����
select sysdate-1, sysdate, sysdate+1 from dual;
--���� ����, �� 1��/ ���� ��������
select sysdate, trunc(sysdate,'month'), last_day(sysdate) from dual;
--�� ��¥�� ��, ��
select trunc(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2)from employees;
--trunc -1: 1���� ����
select trunc (kor,-1) kor,count(trunc(kor,-1)) from stu_score
--10������ �׷���� ����
group by trunc(kor,-1)
order by kor;
--���� hire_date ��¥���� ���� ���
--���ϴ� ������, count(���ϴµ�����)
select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm'))from employees
--group by ���ϴµ�����
group by to_char(hire_date,'mm')
--����
order by hire_date;
--Q ���� ���
--���ϴ� ������, count(���ϴµ�����)
select to_char(hire_date,'yyyy') hire_date, count(to_char(hire_date,'yyyy'))from employees
--group by ���ϴµ�����
group by to_char(hire_date,'yyyy')
--����
order by hire_date;
--����ȯ: number, character, date
--number ��Ģ����0, ��ǥǥ��x, ��ȭǥ��x
--char ��Ģ����x, ��ǥǥ��0, ��ȭǥ��0
--date +,-����, ��¥ ������º���x > to_char ����ȯ �� sysdate,'yyyy-mm-dd'
--������ ���·� �й��� �ο��Ͻÿ� stu_seq
--nextval ���ڰ� 1�� ī��Ʈ��
select SEQ_NO.nextval from dual;
--currval ������ ��ȣ Ȯ��
select seq_no.currval from dual;
select 'ko'||to_char(sysdate,'yyyy')||lpad(stu_seq.nextval,4,0) from dual;
--������ (123,456,789,)+(100,000) = 1234235 ���
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',',''))) from dual;
select to_number('123,456,789','999,999,999')+to_number('123,456,789','999,999,999') from dual;
--����Ÿ���� ��¥Ÿ������ ����
select 20240425 from dual;
select to_char(20240425) from dual;--����: 20240425
select to_date(20240425+300) from dual;--��¥: 24/07/25
select emp_name, hire_date from employees where hire_date > to_date(20070101) order by hire_date asc;
select to_char(hire_date, 'mm') from employees;
select emp_name, hire_date from employees where to_char(hire_date, 'mm') = 08 and emp_name like '_a%' order by hire_date asc;
select emp_name, hire_date from employees where hire_date > to_date(20070101) and emp_name like '_a%' order by hire_date asc;
-- ���� ���� in : 1��, 5�� 8���� �Ի��� ���
select hire_date from employees where to_char(hire_date, 'mm') in ('01', '05', '08');
-- �̸� �� ��° ĭ�� a�� ���� ���
select emp_name from employees where emp_name like '_a%';
-- �� ������ �����ϴ� ���
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
-- �Է� �� ��¥Ÿ�Կ� ��¥������ �������� �Է��ص� ������.
-- ��¥�� ���ڸ� ���� ���� �Ұ���, ���ڸ� ��¥Ÿ������ �����ؾ���.
insert into eventDate
values(seq_mno.nextval, sysdate, '2024-04-01', sysdate-to_date('2024-04-01'));
select * from eventDate;
-- ����Ÿ������ ����
select to_number('20,000', '99,999') - to_number('10,000', '99,999') from dual;
-- null�� 0���� ġȯ
select salary, commission_pct, salary * (1 + nvl(commission_pct, 0)) as sal from employees;
-- manager_id ���� null ���� ceo�� ġȯ
select nvl(to_char(manager_id), 'ceo') as new_id from employees order by manager_id desc;
-- �׷��Լ� : sum, avg, count, min, max : �Ϲ� ������ column�ϰ� ����� �� ����
-- �׷� �Լ��� ����� �ϳ��� row
-- group by�� �̿�
-- ���� count
select count(emp_name) from employees; --107
select count(manager_id) from employees; --106 null ���� ���Ե��� ����
select count(*) from employees; -- ��ü ��(������) ������ Ȯ���� ���� asterisk�� ���
-- sum : ����
select sum(salary) from employees;
-- avg : ���
select avg(salary) from employees;
-- min : �ּ�, max : �ִ�
select min(salary), max(salary) from employees;
-- salary�� ��պ��� ���� ��� �˻�
select emp_name, salary from employees where salary > (select avg(salary) as avg_sal from employees);
-- ��պ��� ���� ������� ��� salary
select avg(salary) from (select emp_name, salary from employees where salary > 6461) order by salary desc;
-- �ּ� salary�� �޴� ����� ��� �̸� ���
select employee_id, emp_name, salary from employees where salary=(select min(salary) from employees);
-- �ִ� salary
select employee_id, emp_name, salary from employees where salary = (select max(salary) from employees);
-- �μ� ��ȣ�� 50���� ����� ��ü ����
select sum(salary) from (select department_id, salary from employees where department_id = 50);
desc stu_score;
select no, name, kor from stu_score where kor >= 80 order by kor desc;
-- ��������, ���������� ���� ��� �̻��� ��� ���
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
-- �������� �ְ��� �л�, �������� �ְ����� �л�, �������� �ְ����� �л� ���
select * from stu_score;
select name, kor, eng, math from stu_score
where kor=(select max(kor) from stu_score)
or eng=(select max(eng) from stu_score)
or math=(select max(math) from stu_score);
-- �ְ� �޿�, ���� �޿�, ��� �޿��� ���� ����� ���
select emp_name, salary from employees
where salary=(select max(salary) from employees)
or salary=(select min(salary) from employees)
or salary=(select round(avg(salary), -2) from employees)
order by salary, emp_name asc;
-- �����Լ�
-- lpad, rpad : �� ���� ä���
select emp_name, lpad(emp_name, 15, '#') from employees;
select emp_name, rpad(emp_name, 20, '-') from employees;
-- ltrim, rtrim : Ư�� ���� �ڸ���
select emp_name, ltrim(emp_name, 'Do') from employees where emp_name like 'Do%';
select 'ko20240001', ltrim('ko20240001', 'ko2024') from dual; -- 1
-- substr : ���� �������� ���� �ڸ���
select emp_name, substr(emp_name, 3, 4) from employees;
select employee_id, job_id from employees;
select substr(job_id, 1, 2)|| trim(to_char(employee_id)) from employees order by employee_id asc;
--length
select emp_name, length(emp_name) from employees
where length(emp_name) >= 15
order by length(emp_name) asc;
-- ��¥ �Լ�
-- ��¥ ������ +, - ���ڴ� ����
select sysdate+1 from dual;
select sysdate - hire_date from employees;
--��¥������ + ��¥������ �Ұ���
select sysdate + hire_date from employees; -- ORA-00975: ��¥�� ��¥�� ������ �� �� �����ϴ�.
select round(sysdate, 'month') from dual; -- 24/05/01
select trunc(sysdate, 'month') from dual; -- 24/04/01
select round(sysdate, 'year') from dual; -- 24/01/01
-- x���� �� ���
select sysdate, add_months(sysdate, 3) from dual; -- 24/07/25
select sysdate, add_months(sysdate, -2) from dual; -- 24/02/25
-- �ø�, ����, ������, �����Լ�
select ceil(-4.2), floor(-4.2), mod(8, 3), power(2, 10) from dual;
select * from employees;
select emp_name || ' ' || to_char(hire_date, 'yyyy"��"mm"��"dd"��"day') from employees
order by hire_date asc;
select emp_name || ' ' || to_char(hire_date, 'yyyy')|| '��'
|| to_char(hire_date, 'mm')||'��'
|| to_char(hire_date, 'dd')||'��'
|| to_char(hire_date, 'day') as emp_hire_info
from employees order by hire_date asc;

--Q �����, �ڸ��� 9�ڸ� ����� 0���� ǥ��
--salar*1400 �տ� ��ȭǥ�ÿ� ������ �־� ����Ͻÿ�
select salary, to_char(salary*1400,'L000,000,000') from employees;

--�ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ��������¥
--'2010-10-10'
select '2010-10-10', last_day('2010-10-10') from dual;-- 10/31
select '2010-10-10', trunc(to_date('2010-10-10'),'month') from dual;-- 10/01

select*from member;

desc member;

-- DDL(date definition language)�÷� �߰�
--commit, rollback �ȵ�; �ٷ� �����
alter table member add gender varchar2(6) default 'Female' not null;
desc member;
--�÷� ����: �÷��̸�����, Ÿ�Ժ���
alter table member rename column name to stu_name
;
--�÷� Ÿ�Ժ���
alter table member modify(stu_name varchar2(50));
--������ �����Ͱ� �����Ϸ��� ũ�⺸�� ���� ���� ����
update member set stu_name='ȫ';
alter table member modify(stu_name number(100);
--�÷��� Ÿ���� �����Ϸ��� ����餷�ӳ� null��� �Ѵ�.
alter table member modify(stu_name number(4);

desc member;
--�÷� ����
alter table member drop column phone;
desc member;
select*from member;
commit;