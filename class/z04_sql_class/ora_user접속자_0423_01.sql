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