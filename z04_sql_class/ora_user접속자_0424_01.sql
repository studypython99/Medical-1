--10���� �ƴϰ� 50���� �ƴ�, not != <> ^=
select department_id from employees
where department_id != 10 and department_id != 50
order by department_id;

--5000�̻� 9000����
select salary from employees
where salary >=5000 and salary <=9000
order by salary
;

--����� 99�� �̻��� �л��� �˻�
insert into member (id,pw,name,phone) values (
'aaa','1111','ȫ�浿','010-1111-1111'
);
insert into member values (
'bbb','1111','������','010-2222-2222'
);
insert into member (id,name,phone) values(
'ccc','�̼���','010-3333-3333'
);
select*from students;

--no= 1�� �̸��� ȫ�浿 ���� ����
update students set name='ȫ�浿'
where no=1;

update students set name='������'
where no=2;

update students set name='�̼���'
where no=3;

update students set name='������'
where no=4;

update students set name='�豸'
where no=5;

update students set name='������'
where no=6;

update students set name='������'
where no=7;

update students set name='����'
where no=8;

update students set name='�����'
where no=9;

update students set name='�̼���'
where no=10;

--���� 80, ��� 85�� �̻��� �л��� ���
select no, name, kor, avg from students
where kor>=80 and avg >=85;

--���� 70,80,90�� �л����
select no, name, kor from students
where kor=70 or kor=80 or kor=90;

update students set kor = 100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;

select *from students
where no=1;

--���������� 70~90�� �л����
select no, name, kor from students
where kor>=70 and kor<=90;

--between a and b, a�� b ����(�̻�����)
--not: between �̿� (�̸��ʰ�)
select no, name, kor from students
where kor not between 70 and 90;

--��¥�� between a and b
select hire_date from employees
order by hire_date;
--99�⺸�� ũ�ų� ����, 01�⺸�� �۰ų� ���� ���
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date;

--in: ������ �ʵ尡 ���� ���߿�(70,80,90) �ϳ��� �˻��� ��� or
select name,kor from students
where kor in(70,80,90);

--�̸��˻�
select*from students
where name='ȫ�浿';
--like: Ư���ܾ ���ԵǾ��ִ� ���� �˻� 
--ȫ �̶�� ���ڰ� �ִٸ� ��Ÿ����
select*from students
--where name like 'ȫ%';--ȫ���� �����ϴ�
--where name like '%ȫ';--ȫ���� ������
--where name like '%ȫ%';--ȫ'���ԵǾ��ִ� �ܾ�
where name like '%ȫ%';

-- _: ��ĭ ������ ���
select*from students
where name like '_��%';
--3��°�� t �� ���ִ� �̸�
select*from students
where name like '__t%';

--�̸��� 4�ڸ���, 3��° r�� �� �ִ� �̸� �˻�
select*from students
where name like '__r_';
--4�ڸ��� �̸�
select name from students
where length(name) =4;

--�̸��� A�� ���۵Ǵ�

select*from students
where name like 'A%';

--�̸��� a�� �� �ִ�
select*from students
where name like '%a%';

--��ҹ��� ���о��� a�� ����ִ� �л�
--�ҹ��� ġȯ(lower), �빮�� ġȯ(upper), ù���� �빮��(initcap)
select*from students
where lower (name) like '%a%'

--a�� ���Ե��� ���� �̸�
select *from students
where name not like '%a%';

select mamager_id from employees;
--manager_id 100�� ��� �˻�
select employee_id, emp_name,manager_id from employees
where manager_id=100;

select employee_id, emp_name, manager_id from employees
where manager_id = null; --null�˻� �ȵ�;;

select employee_id, emp_name, manager_id from employees
where manager_id is not null;

--���� asc(ascending), desc(descending) �ѱ۵� ����

select*from students
order by name asc;

--1��: ���������, 2��: �����������
select*from students
order by kor desc, eng asc;

--total�� ��������
select*from students
order by total desc;

--�÷� �߰� rank
alter table students add rank number(3);
--rank�� �� 0���� ����
update students set rank=0;
--����
commit;

--���, �����ֱ⸸ �ϰ� ������ �ȵ�;;
select no, name,total,rank() over(order by total desc) as rank from students;

--����, 1�� 13������
update students set rank=13
where no=1;

-- ���
select no,rank() over(order by total desc) as rank from students
;
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;
select * from students;

-- ���
select no,rank() over(order by total desc) as rank from students
;
--��������;;;;
update students s1 set rank = (select ranks
from (select no, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no )
;
select * from students;

--��ü�߿��� ���� 70�̻�
select*from students
where kor>=70;
--��� 80�̻� �߿��� ���� 70�̻�
select*from (select*from students where avg>=80)
where kor>=70;

select*from students;
------------------------------------------------------------------------------
--����, rank() ���� ��ü�� ����; 
select total, rank() over(order by total desc) rank
from students;
--total�� 0���� ����
update students set total=(kor+eng+math);
--������������ students=a��(����� total�� ���ĵ�) ,b��(������ 12345)
--���� ��ȣ�ڸ��� ����� �Է��Ѵ�.
update students a set rank=(select no, rank() over(oder by total desc) rank
from students b where a.no=b.no);
--1.update ����
update students a set rank=(rank);

--2. no, rank() ����, �ϳ��� ���̺�b �� ���
(select no, rank() over(order by total desc) ranks from students) b;

--3. update ������ rank() ������ no�÷����� ��, rank�÷��� �˻�
update students a set rank(
select ranks from (select no, rank() over(order by total desc) ranks from students) b
where a.no = b.no
);
--��������
select no,total,rank from students
order by total desc;
--no��������
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

--�Ի��Ϸ� �������� �÷�: ���,�����,job_id, �Ի���
select*from employees;
select employee_id, emp_name, job_id, hire_date from employees;

--�޿��� ���� �޴� ��������� ���, ������ ������ ��������� ��������
select employee_id, emp_name, salary from employees
order by salary asc, emp_name;

select *from students;

--�����Լ�
--abs: ���밪, �������� ���� �ȵǴ� ��� ���.
select -10, abs(-10) from dual; -- -10, 10
--floor: ����, round: �ݿø�, ceil: �ø�
select 34.789, floor(34.789), round(34.789), ceil(34.789) from dual;
--round �Ҽ��� �ڸ��� �����ϱ�: round(���,�ڸ���)
select 34.178, round(34.178), round(34.127,2) from dual;

select avg from students;
select round(avg,2) avg from students;
--round(n,-1) �����κ� 1���ڸ� �ݿø�
select 23.5678, round(23.56789,-1) from dual;

--trunc ������ �ڸ��� ���� ����
select trunc(34.5678,2) from dual;
select trunc(34.5678,-1) from dual;
select trunc(34.5678) from dual;

--�ø�
select ceil(34.123) from dual;

--�������� �ϴ��� �����ؼ� 10���� ���
select *from students;
select no, name, trunc(kor,-1) kor from students;

--������ �ϴ��� ���� �� �հ� ���
select*from students;
select no, name, trunc(kor,-1)k, trunc(eng,-1)e, trunc(math,-1)m ,
(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) total
from students;

--mod ������
select round(100/7,2) from dual;--������
select mod(10,7) from dual; --10�� 7�� ���� ����������? 3

--����. �����ȣ�� ¦���ΰ��� ����Ͻÿ�
select *from employees;
select employee_id from employees
where mod(employee_id,2) = 0; -- if���� �����ϰ� ��� ����

--���� �й� 3�ǹ���� ���
select *from students;
select no, name from students
where mod(no,3)=0; --3���� ���� ���������� 0�ΰ� = 3�� ���

--������
CREATE SEQUENCE seq_no
       INCREMENT BY 1 --1�� ����
       START WITH 1 --1���� ����
       MINVALUE 1 -- �ּҰ�
       MAXVALUE 9999 --�ִ밪
       NOCYCLE --��ȯx
       NOCACHE --ĳ�û��x
       NOORDER;
--nextval ���ڰ� 1�� ī��Ʈ��
select SEQ_NO.nextval from dual;

--currval ������ ��ȣ Ȯ��
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
seq_mno.nextval,'eee','1111','�豸','010-1111-1111'
);
select*from member;

select sysdate from dual;
select to_char(sysdate,'yy') from dual;
--s0000 ��� ���·� �ڸ����� �ø�, to_char: ��¥, ���� �����͸� ���ڵ����ͷ� ��ȯ
select 's'||to_char(seq_mno.nextval,'00000') from dual;

--����, �ѱ����б� ko202400001
--������ seq_kono 1-99999
create sequence seq_kono
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache
noorder;
--trim() �������� to_char �����͸� ���ڵ����ͷ� ��ȯ
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_kono.nextval,'00000')) as stuno from dual;

--�Խ���
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar2(3000),
id varchar2(30),
bdate date,
bhit number(10) --��ȸ��
);

--������ ����
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
empseq.nextval,'������',sysdate
);
select*from emp01;

select*from employees;

--������� �Ի��� �ϼ�(�Ҽ��� �ø�ceil)�� �Բ� ����Ͻÿ� ||'��' concat ���ڿ� ��ġ��
select employee_id, emp_name, job_id,ceil(sysdate-hire_date)||'��' from employees;


--�Ի��� ��������
select employee_id, emp_name, job_id, hire_date from employees
order by hire_date desc;

select emp_name from employees;

--���ް� ����� ���ļ� ����Ͻÿ�
select*from employees;
select job_id||employee_id from employees;

--substr: ���ڿ� �ڸ��� �Լ�, substr(���,����,����)
select emp_name,substr(emp_name,1,3) from employees;--1������ 3����
select substr('abcd',2,3)from dual; --2������ 3����

--job_id ���� 2�� ���ڿ� ��� 5�ڸ�
select substr(job_id,1,2)||lpad(employee_id,5,0) from employees;
--trim(to_char(employee_id,'00000'))

--s��¥�Լ�
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;
--�� ��¥ ������ ������ Ȯ��
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;
--add_month(���糯¥,+������)
select sysdate, add_months(sysdate,2) from dual;
--���縦 �������� ������ ���� ������ 24/04/29
select next_day(sysdate,'������') from dual;
--�Է��� �������� ������ ���� �˷���.
select last_day(sysdate) from dual;--24/04/30
select last_day('2024-02-21') from dual;--24/02/29

--trunc����, round�ݿø�
select sysdate, hire_date, trunc(sysdate-hire_date,3) from employees;

--������¥: sysdate-1 / ����: sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ���� from dual;

--���� m_no m_yesterday, m_today, m_tomorrow, m_year ���� ���̺� m_date
--���̺� ��Ͽ� ���� ���� ����
create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date
);

select *from m_date;
insert into m_date (m_no, m_yesterday, m_today, m_tomorrow, m_year) values(
1, sysdate-1, sysdate, sysdate+1, sysdate+365
);
select *from m_date;
--abs: ���밪, ceil, round, floor, trunc
select abs(hire_date-sysdate) from employees;
--month�������� �ݿø�(round)
select hire_date, round(hire_date,'month') from employees;
--�� �������� ����
select hire_date, trunc(hire_date,'month') from employees;

select trunc(hire_date,'month')������ , hire_date from employees
order by hire_date;

select *from channels;

select period, count(period) from kor_loan_status
group by period
order by period;

select peiood fromd ofr_loan_status
where period='201111';
--�����뺰�� �������
select trunc(kor,-1) t_kor, count(t_kor) from students
order by t_kor;

select trunc(hire_date,'month') m_hire_date, count(trunc(hire(hire_date,'month')) from employees
group by trunc(hire_date,'month')
order by m_hire_date;

--drop table stu_scoree;
--drop table emp01;
--drop table board;

select*from stu_score
order by no;

update stu_score set name='������'
where no=10;

select*from stu_score;
update stu_score set avg=(total/3);

--2���� ��¥���� �� ������ Ȯ��
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

--6���� �߰�
select hire_date,add_months(hire_date,6) from employees;

--last day
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;
--'d' 12�ø� �������� �ݿø� 
select sysdate, round(sysdate,'d') from employees;
--���� ù �� ��¥
select sysdate ����,trunc(sysdate,'month') ù ,last_day(sysdate) �� from dual;

--�������, ���� ������
select sysdate, next_day(sysdate,'������') from dual;

--�����Ϸ� ����trunc(sysdate,'d')
select sysdate, trunc(sysdate,'d') from dual;
--����Ϸ� ����next_day(sysdate,'�����')
select sysdate, next_day(sysdate,'�����') from dual;

-- board table
create table board(
bno number(4) primary key, --�ߺ��ȵ�, null���x �⺻Ű�� ����. �Խñ۹�ȣ
name varchar2(30), --�۾���
title varchar2(1000), --����
bcontent clob, --varchar2: 3k, clob: unlimit ����
bdate date default sysdate,
bhit number default 0, --��ȸ��
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);
insert into board (bno,name,title,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','�̺�Ʈ��û','�̺�Ʈ�� ��û�մϴ�.',board_seq.currval,'2.jpg'
);
select*from board;

--�� ��ȯ: number, character, date

select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

-- ko 2024 0001
select 'ko'||to_char(sysdate,'yyyy')||lpad('1',4,0) from dual;
--dy�� day������
select to_char(sysdate,'dy'), to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd pm hh:mi:ss mon day') from dual;

--hire_date, yyyy-mm-dd hh:mi:ss mon day

select to_char(sysdate,'am hh24:mi:ss') from dual;

select*from stu_score;

select to_char(c_date,'yy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

--��¥���� ��� �����Ͱ� �� �ִ��� ����Ͻÿ�
select*from stu_score;
select c_date, count(c_date) from stu_score group by c_date;

--�� ��ȯ: number, character, date �ʿ���;;
--������ ��Ģ����(=-*/)�ȵ�, �ڸ���ǥ��, ��ǥǥ��, ��¥���� ǥ��
--������ ��Ģ���� ���� �÷��� ��Ģ���갡��, �ڸ���ǥ��(0001 > �ȵ�)
--��¥�� +,- ������ ����, months-between 2�� ��¥ �� ���, ��¥������ �����ؼ� ��¾ȵ�

--������ �ȿ� �ִ� �����Ͱ� �����̸� �ڵ� ����ȯ�Ǿ� ��� ����
--������ �ȿ� ���ڰ� ������ '100��' �ڵ���ȯ �Ұ�
select 10 a, 100 b,(10+100) ab, to_char(100),10+to_char(100) from dual;
--000 ���ڸ��� 0���� ä��, 999�� ���ڸ��� �����
select 12340000, to_char(12340000), to_char(12340000,'999,999,999')from dual;
--L�� ��ȭǥ��
select 12340000,to_char(12340000,'L999,999,999') from dual;
select 12340000,to_char(12340000,'$999,999,999') from dual;
--�Ҽ��� �ڸ� ǥ��
select 1234.1234, to_char(1234.1234,'000,999.99') from dual;
--�������ŵ� �ڸ��� Ȯ��
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;
--�������� �����Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

--���� 123,456,789 + 100,000  ���� ����Ͻÿ�
select 123456789+100000 from dual;
--��ǥ����, Ÿ��number����, ���
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')),'L999,999,999') from dual;
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

select to_number('0000123') from dual;

--������ +,- �ȵ�;
select '2024-04-24'-'2024-04-01' from dual;
--��¥������ �����ؼ� ���
select to_date('2024%04%24')-to_date('2024%04%01') from dual;
--to_date('20240401')�� 2024-04-01 ���·� ��ȯ
select to_char(to_date('20240401'),'yyyy-mm-dd') from dual;

--���������̴��� �����ͷ� ����ȯ�� �����ϸ� �ڵ����� ã���ش�.
select c_date from stu_score
where c_date = '2024/04/05';
--����ȯ�� �ʿ��ϴ�.
select sysdate-to_date('2024/04/01') from dual;

--���� ������ 20,000-10,000 �� ����ؼ� 10,000 ��µǵ���
select 20,000-10,000 from dual; -- 20	-10	0
select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;

--����
select commission_pct from employees;
--��������= ����*(1+Ŀ�̼�)
select *from employees;
--nvl(��,������) null�� 0���� ǥ���ϴ� ���
select salary*(1+nvl(commission_pct,0))*1300*12 from employees;
--commission_pct�� null�� ���
select emp_name, commission_pct from employees
where commission_pct is null;

--���� manager_id null�̸� 0
select nvl(manager_id,0) from employees;

--���� manager_id null �̸� ceo
select emp_name, (nvl(to_char(manager_id),'ceo')) from employees
order by manager_id desc;