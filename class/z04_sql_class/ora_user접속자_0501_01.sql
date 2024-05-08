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