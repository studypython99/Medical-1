-- non-equi join
select no,name,avg,grade 
from stu_score,stu_grade
where avg between low_score and high_score
order by no
;
--name,sum(amount),rank���
select*from shop_product;

select name, s_amount,rank 
from (select name, sum(amount) as s_amount from shop_product where pdate>='2024/03/01' group by name),customer_rank
where s_amount between low_amount and high_amount
;
--t
select name,s_amount,rank from (select name,sum(amount) s_amount from shop_product where pdate>='2024/03/01'
group by name),customer_rank
where s_amount between low_amount and high_amount
;
select name,sum(amount) s_amount from shop_product group by name;

--������ ���Ӱ� �ο��ؼ� ������ִ� �Լ� rownum, row_number()
--�������� ��ȣ�� �ο��� rownum
select rownum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from lotte_product
;
--11������ �����ϸ� ������ �߻�, rownum�� 1������ ������;;
select rownum rnum,b.* 
from
(
select rownum rnum,a.* from lotte_product a --��ȣ�� �̸� �ٿ����´�
)b
where rnum >=11 and rnum <=20;
--order by ������ ��ȣ�� ���̴°��� �̿��� �����ϱ� ���� �̸� order�� �����Ų �� rownum����
select rownum,b.*
from (select * from lotte_product order by std_ym) b
;

select rownum,a.*
from lotte_product a
where rownum <= 10 --10���� ��������
;

select*from stu_score 
order by no
;
--kor ���� 21~30�� ���
select rownum, b.* from(select rownum rnum,a.* from stu_score a order by kor desc)b;
select c.* from(select rownum rnum, b.* from(select rownum rnum,a.* from stu_score order by kor desc)a)b)c where rnum >=21 and rnum <=30;
--!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
/* 1: select * from stu_score a order by kor desc;
   2: select rownum rnum, a.* from(select * from stu_score a order by kor desc)a */
select * from (select rownum rnum, a.* from(select * from stu_score a order by kor desc)a) where rnum >=11 and rnum <=30;

--drop table students;
select*from students;
update students set id='aaa',name='ȫ�浿', gender='m' where id='Claire' and pw='7577';--2��
update students set id='bbb',name='������', gender='m' where id='Koralle';
update students set id='ccc',name='�̼���', gender='f' where id='Cornall' and pw='1997'; --2��
update students set id='ddd',name='������', gender='m' where id='Zitella';
update students set id='eee',name='�豸', gender='f' where id='Sutton';
update students set id='fff',name='������', gender='m' where id='Alanah';
update students set id='ggg',name='ȫ����', gender='f' where id='Cirstoforo';
commit;
rollback;
--���Ӱ� ������ ��ȣ����: rownum
--1. select ����
select a.* from students a;
--2. rownum �Լ� ����
select rownum, a.* from students a;
--3. order by ���� ����
select rownum, a.* from students a
order by grade;

--1.select 2.order by ���� 3.rownum
select * from students
order by grade;

select rownum, a.* from
(
select * from students
order by grade;
)a;

--��� 85�̻�, no 500���� ū �� �˻�
select a.* from stu_score a
where avg >= 85 and no>500
order by no;
--���� ����
select * from
(
select*from stu_score where avg >=85
) where no>=500
;
--�̸���, ���ų��� �հ�
select*from shop_product;
select neme, amount, pdate from shop_product
where pdate >='2024-03-01';
--equi join: �÷��� 2���� ���̺� ���� ����, 2���� �÷��� �̿��ؼ� �˻��ϴ� ���
--non equi join: ���� �÷��� �����餵 ��2���� ���̺��� ����� �˻��ϴ� ���
select name, s_amount, rank 
from (select name, sum(amount) as s_amount from shop_product where pdate >='2024/03/01' group by name), customer_rank
where s_amount between low_amount and high_amount
;--non equi join

select name, sum(amount) as s_amount from shop_product
where pdate >='2024/03/01'
group by name;

select rownum, a.* from students a
order by id;

select * from(select rownum rnum, b.* from (select *from students order by id)b) where rnum>=11 and rnum <=20;

select row_number() ober(order by id) as rnum,a.*
from students a)
where rnum>=11 and rnum<=20;
--self join, �̸��� ������ ���� �ѹ� �� ���̰� �ʹ�
select employee_id,emp_name,a.department_id, department_name, a.manager_id from employees a, departments b
where a.department_id = b.department_id
order by a.department_id;

-- cross join 107 * 107
-- self join,equi-join �Բ� ���
-- equi join : 2�� ���̺� ���� �÷��� ������ �˻�
select a.employee_id, a.emp_name, a.department_id, department_name, a.manager_id, b.emp_name
from employees a,employees b, departments c
where a.manager_id = b.employee_id and a.department_id = c.department_id
--�Ŵ��� ���̵�� ���� ���� ���̵� �����ͼ� b.emp_name�� �Է��ض�
--�ڱ� ��� ã�Ƽ� ����س���
;
--self join
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id;

--'Guy Himuro'�� ������ �μ��� �ٹ��ϴ� ����� ����Ͻÿ�
--�÷�: �����, �μ���ȣ, ������ ����� �μ���ȣ
--1. john �μ� ���
--2. ���� �μ���ȣ�� ����� ���
select * from employees;
select a.emp_name, a.department_id, b.emp_name, b.department_id
from employees a, employees b
where a.emp_name like 'Guy Himuro' and a.department_id = b.department_id
;

select*from member;

insert into member values(
member_seq.nextval,'ddd',1111,'������','����',sysdate
);
commit;
desc member;
update member set name='ȫ�浿' where id='aaa';
rollback;

select * from employees;

select a.emp_name,a.department_id,c.department_name,b.emp_name 
from employees a, employees b, departments c
where a.department_id = b.department_id and a.emp_name = 'Pat Fay'
and a.department_id = c.department_id
;
select*from member;
--hhh,1111,ȫ����,����

--���̺� ����
create table mem(
id varchar2(30) primary key,
pw number,
name varchar2(30),
mdate date
);

select*from mem;
--drop table mem;

create table yeogi(
yno number(4) primary key,
title varchar2(100) not null,
region varchar2(30),
score number,
member number,
img varchar2(100),
price number
);
select * from yeogi;

--2�� �����̺�: department_id

select * from employees;
select * from departments;
--department_id �ΰ��� �������´�
select employee_id, emp_name, department_id, department_name
from employees a, departments b
where a.department_id = b.department_id
;

select * from stu_score;
select * from students;
--�÷� �߰�
alter table students add no number(38);
--�ڷ� �߰�
insert into students(no) select no from stu_score;
--rownum���� ������� ��ȣ�� no�� �ֱ�
select rnum from(select rownum rnum, a.* from students a); --1
update students b set no = (select rnum from(select rownum rnum,id from students )a)
where a.id = b.id
;
update students b
set no = ()
from(select rownum rnum, id from students)a
;


--ȫ�浿 �л�, �л������� ��� ����� ����, �̸���, ��, �г�
select no, name, kor, eng, math, total, avg, rank, c_date from stu_score
where name='ȫ�浿';

select no,id,a.name,phone,email,major,grade from students a, stu_score b
where a.name='ȫ�浿' and a.name = b.name;

--drop table stu_score;

--equi join
--2���� ���̺� join 1���� ������ �÷��� �־�� �Ѵ�.
--������ �÷��� �ߺ��� ������Ѵ�, 
--2�� �� �Ѱ��� ���̺����� primaryŰ�� ���Ǿ�� �Ѵ�.
select a.id, a.name, phone, total, avg from students a, stu_score b
where a.id = b.id
;

--self join
--������ ���̺� 2���� ������ ���� join, ���ã��
select a.employee_id, a.emp_name, a.department_id, a.job_id, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id
order by department_id;

--drop table students;

select * from students;
select * from stu_score;
desc students;
--stu_score, rank �Է��ϱ�
update stu_score a
set rank = (select ranks from (select no,id,rank() over(order by total desc) as ranks,rank, total from stu_score)b--2����,3
where a.no = b.no)
;
--rank
select rank() over(order by total desc) as ranks,rank, total from stu_score--1
select ranks from (select no,id,rank() over(order by total desc) as ranks,rank, total from stu_score)b--1����,2
;

select * from member;

alter table member add no number;
--rank, id ��������
select rownum rnum, id from member;
                        --rownum�� rnum���� ����, 
update member a set no = (select rnum from(select rownum, a.* from member)b where a.id = b.id)
;

update stu_score set rank=0;
commit;
--total ������ �������� ����, =�� ����� ����
select total, rank from stu_score
order by total desc;

select total, rank() over(order by total desc) ranks from stu_score;
select row_number() pver(order by total desc) rnum, total from stu_score;

--stu_score, rank ������ ��� update�Ͻÿ�
select total, rank() over(order by total desc) ranks from stu_score

;

--update���
update stu_score set rank = 1
where no=1;
select * from stu_score;
--????????????????????????????????????????
update stu_score set rank=(select rank from(select no, rank() over(order by total desc) ranks from stu_score)
where a.no = b.no)

--
    select * from stu_score order by total desc  --1
    (select rownum rnum,a.* from( select * from stu_score order by total desc )--1+2
    select * from(select rownum rnum,a.* from( select * from stu_score order by total desc ) a) where rnum>=11 and rnum<=20 --1+2+3
;
select * from (
select row_number() over(order by total desc) rnum,a.* from stu_score a
)
where rnum>=11 and rnum<=20
;

--
select employee_id, emp_name,manager_id from employees
order by employee_id;

--self join manager_id, �̸� ��������
--���� �������� �ʾƵ� ��µǵ��� outer join
--null���� �ִ� �ݴ��� �׸� (+)��ȣ�� �ִ´�
--null���� ������ �ݴ��� (+)�� �ִ� �ʿ� �߰�����
select a.employee_id, a.emp_name, a.manager_id, b.emp_name
from employees a, employees b
where a.manager_id = b.employee_id(+) -- a�� ���°� b�� �߰��Ѵ�
;

select manager_id, emp_name from employees
where emp_name = 'Diana Lorentz';

--outer join, �μ���ȣ�� 10~110������ �ִ�. =employees 10~110
--���ºμ�(120~270)�� ǥ�ô� ���ּ���. == departments 10~270
-- null���� �߰����� (+)
select emp_name,a.department_id, department_name 
from employees a, departments b
where a.department_id(+) = b.department_id
order by department_id
;
--�μ���ȣ�� 10~270���� �ִ�.
select department_id from departments;

-- ANSI JOIN
select * from employees cross join departments;
select * from employees, departments;

--equi join ������ �������� ���
select a.department_id, department_name --�μ���ȣ, �μ��̸��� ��Ÿ����
from employees a, departments b --������̺�a, �μ�b �κ���
where a.department_id = b.department_id 
;
--ansi inner join
select a.department_id, department_name from employees a inner join departments b
on a.department_id = b.department_id
;
--ansi inner join - using ���� �����κ�
select department_id, department_name
from employees join departments
using (department_id)
;
-- natural join ?????????????????????????????????
select employees.department_id, departments.department_name
from employees natural join departments b;

-- ansi outer join, left outer join, right outer join, full outer join 4���� ����
select a.emp_name, a.manager_id, b.emp_name from employees a
left outer join employees b
on a.manager_id = b.employee_id;
--�⺻ sql left,right,full �Ұ�;;
select a.emp_name, a.manager_id, b.emp_name 
from employees a, employees b
where a.manager_id(+) = b.employee_id;


--�̸��˻� a�� �� ���, 10���� ��������
select * from stu_score where id like '%a%'
order by no
;
--row_number() over()
--11~20���� ����ϱ�
select rownum, id  from stu_score
where rownum >=11 and rownum <=20
;
select rownum rnum a.* from (select * from stu_score)a where rownum >=11 and rownum <=20;

select rownum,a.* from stu_score a order by no;
select row_number() over(order by no) rnum, a.* from stu_score a; -- 1
select *from(select row_number() over(order by no) rnum, a.* from stu_score a where id like '%a%')where rnum >=11 and rnum <=20;


select count(*) from stu_score where id like '%a%';


--���
create table melon (
mno number primary key,
rank number,
v_rank number,
img varchar2(100),
title varchar2(100),
singer varchar2(100),
likeNum number --��ǥ ���� �־���Ѵ�
);

create table yanolja (
yno number primary key,
img varchar2(100),
title varchar2(100),
grade number,
grade_num number,
price number
);
desc melon;
select * from melon;