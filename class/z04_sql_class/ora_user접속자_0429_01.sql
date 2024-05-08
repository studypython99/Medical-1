
--���Ἲ ��������: �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ����� ��Ģ.
--not null, unique, primary key, foreign key, check
create table member(
memno number(4) not null,
id varchar2(30) primary key,
pw varchar(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in ('����','����')),
mdate date default sysdate
);

--������ �Է�, ���, ����, ����
insert into member (memno,id,pw,name,gender,mdate) values(
1,'aaa','111','ȫ�浿','����',sysdate
);
insert into member(memno,id,pw,name,gender) values(
2,'bbb','111','������','����'
);
select*from member;

--���̺� ����
create table board(
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(1000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī : fk_id
references member(id) -- member table�� primary key �� id�� �Ǿ����� �� �ܷ�Ű ���
);

--primary key�� �����Ϸ��� foreign key ��ϵǾ� �ִ� �����͸� �켱 �����ؾ���
--primary key �����Ǹ� ��λ��� -on delete cascade
--                    ������� - on update cascade
--������ �Է�
insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','�����Դϴ�','�����Դϴ�.',sysdate,board_seq.currval,0,0,1,''
);
--������ �Է�
insert into board values(
board_seq.nextval,'aaa','�����Դϴ�3','�����Դϴ�.3',sysdate,board_seq.currval,0,0,1,''
);

select*from board;
select*from member;
--����
delete board where bno=3;
commit;

delete member where id='aaa';


--decode(switch��ġ�ϴ��� ���� Ȯ��), case(if���ǹ� ��밡��) ��������
--decode���ǹ�
select emp_name, department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��'
)
from employees
order by department_id asc;

select department_id, department_name from departments;

select *from stu_score
order by avg desc;
--90a 80b 70c, like ���Ұ�
select avg, decode(avg,
'9%','A',
'8%','B',
'7%','C',
)
from stu_score
order by avg asc;

--sh_clerk*15%, ad_asst*10% MK_rep*5%;
--decode, like���Ұ�
select*from employees;
select job_id,salary,
decode(job_id,
'%CLERK', salary*(1.15),
'%ASST', salary*(1.10),
'%REP', salary*(1.05)
) as sall
from employees
order by job_id asc;

--job_id, clerk�� ���ִ� job_id�� �˻��Ͻÿ�
select job_id from employees;
select job_id from employees
where job_id like '%clerk';

--case��
select name, avg from stu_score;

select name, avg,
case 
when avg >=90 then 'A'
when avg >=80 then 'B'
when avg >=70 then 'C'
else 'F'
end as grade
from stu_score;


select department_id, department_name from departments;
--case����, department_id �̸�
select department_id from employees
order by department_id asc;

select department_id, department_name,
case
when (select department_id from departments) = (select department_id from employees)
then (select department_name from  departments)
end as ii
from departments;

--������ ����Ͻÿ�
--job_id
--clerk ����: salary*15%, ad_asst*10%, rep����*5%, man����*2%
--case
select job_id, salary from employees;
select job_id, salary,
case
when job_id like '%CLERK' then salary*1.15
when job_id like '%ASST' then salary*1.10
when job_id like '%rREP%' then salary*1.05
when job_id like '%MAN%' then salary*1.02
end as sal_up
from employees
order by job_id asc;

--���� ��� ���ϴ� 0.15, ����̻� 0.05% �λ��ؼ� ����ϼ���
--case ������ ����ϱ�
select emp_name,
case
when salary > (select avg(salary) from employees) then 'up'
else 'down'
end as sal_updown
,
case
when salary > (select avg(salary) from employees) then salary*1.05
else salary*1.15
end 
from employees;

--rank
select total, rank from stu_score
order by total desc;
--order by total desc�� ���·� rank()�� ����
select total,rank,rank() over(order by total desc) from stu_score;
--rank update
update stu_score a
set rank = (
select ranks from(
select no, rank() over(order by total desc) as ranks from stu_score
) b
where a.no = b.no
)
;
commit;
select no, rank from  stu_score
order by no asc;
-----------------------------------------------------------
--join

select department_id, department_name from departments;
select emp_name,department_id from employees;
-- �ΰ� ���̺� ����
select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id;

--�׷��Լ�: sum, avg, count, max, min stddevǥ������, variance�л�

--���� ����
select sum(salary) from employees;
--�������� �հ�
select sum(kor) from stu_score;

select count(*) from employees; --107
select count(*) from employees
where department_id = 50; --45

--Ŀ�̼��� �޴� ����� ��
select count(commission_pct) from employees; --35
select emp_name, commission_pct from employees
where commission_pct is not null; --35

--group by, �׷��Լ����� ���δ�
--��ü ��� ��
select count(*) from employees;
--�μ���ȣ 50�� ��� ��
select count(*) from employees
where department_id = 50;
--�μ���ȣ���� ��� ��
select department_id, count(department_id) from employees
group by department_id
order by department_id asc;

--avg grade
--stu_score 90���̻� A, 80���̻� B, 70���̻� C, 60���̻� D, ������ F
select*from stu_score;

select grade, count(grade)
from(select avg,
case
when avg like '9%' then 'A'
when avg like '8%' then 'B'
when avg like '7%' then 'C'
when avg like '6%' then 'D'
else 'F'
end as grade
from stu_score) 
group by grade;

--kor 10���뺰�� ���
--trunc(kor,-1)�� ����� group by
select trunc(kor,-1), count(trunc(kor,-1))from stu_score
group by trunc(kor,-1);
--as k_kor, as k_count �� �����ϱ�
select k_kor, count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score) --10���뺰�� ����� ��Ī�� ���
group by k_kor;

--�׷������� �־���Ѵ�. �׷��Լ� group by ���
select department_id,count(*) from employees
group by departnemt_id
order by department_id;

select emp_name,count(emp_name) from employees
group by emp_name;

--�μ��� ��� ������ ���Ͻÿ�
select * from employees;
--�μ��� ��������
select department_id,round(avg(salary),2) from employees
group by department_id
order by department_id;

--CLERK�� ���ԵǾ��ִ�, REP, MAN �� ���� ���
select job_id from employees;
select job_id, round(avg(salary),2)
from (select job_id from employees
where job_id like '%CLERK%')
group by job_id
order by job_id;

select job_id from employees
where job_id like '%CLERK%';

-- clerk�� ���Ե� ������
select job_id,count(job_id) from employees
where job_id like '%CLERK%'
group by job_id;

--clerk�� ��µǵ���
select substr(job_id,4,7) from employees;
select job_id,substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7),count(substr(job_id,4,7)) from employees
where substr(job_id,4,7)='clerk'
group by substr(job_id,4,7);

select substr(job_id,4,7),count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id,4,7)
order by c_job_id;

--�μ���(group by department_id) �ִ�,�ּ�,��տ��� ���
select nvl(department_id,0), count(salary), max(salary), min(salary), round(avg(salary),2) from employees
where department_id is not null
group by department_id
order by department_id;

--+@ �μ��� ���� ����ʹ�.
select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

--�μ��� ��� ��, Ŀ�̼��� �޴� ��� �� ���

--�μ��� ��� ��
select*from employees;
select department_id, count(department_id), count(commission_pct) from employees
where department_id is not null
group by department_id;


--���ϱ׷��� �Լ��� �ƴմϴ� ��� ����, group by �־���Ѵ�
select*from employees;
select department_id, count(department_id), count(commission_pct) from employees
where department_id is not null;

--having: group by ������, where: �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees
group by department_id;

--emp_name �ι�°�� a�� �������� �ʴ°͸�
select emp_name from employees
where emp_name not like '_a%';

select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000;

--��տ��޺��� ���� �׷��� ��ո� ���
select department_id, round(avg(salary),2) from employees
where emp_name not like '_a%'--�Ϲ�����
group by department_id
having avg(salary) >= (select avg(salary) from employees); --�׷�����

--�μ��� �ִ������ 8õ �̻��� �μ�, �ִ���� ���
select nvl(department_id,0), max(salary) from employees
group by department_id
having max(salary) >= 8000
order by department_id;

--join rdbms, ������db
select emp_name, department_id,salary from employees;

select department_id, department_name from departments;

select *from employees, departments;

select count(*) from employees; --107
select count(*) from departments; --27

--equi join
--�� ���̺� �� ���� �÷��� ������ ���ؼ�, �ش�Ǵ� �����͸� ���
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees, departments
where employees.department_id = departments.department_id;

select department_id, department_name from departments;

select*from member;
select*from board;

-- board�� id��, member�� name���� �����ϱ�
select bno,name,btitle,bcontent, bdate, bgroup, bstep, bindent, bhit, bfile from board, member
where member.id = board.id
;

update member set name='ȫ����'
where id = 'aaa';
select * from member;

select *from stu_score;
select*from employees;
select department_id, avg(salary), max(salary), min(salary) from employees
        group by department_id
        ;
select name, avg,
case
when avg >= 60 then '60�̻�'
else '60����'
end as grade
from stu_score
order by grade;

--�����ȣ, �����, �μ���ȣ, �μ���
select employee_id, emp_name, a.department_id,department_name
from employees a, departments b
where a.department_id = b.department_id;

--�׸���, �̸� �ι�° �ڸ��� a�� ���� ���
select emp_name from employees
where emp_name like '_a%';

--������ ����̻��� ���
select salary from employees
where salary >=(select avg(salary) from employees);

select*from employees;
select*from jobs;
select*from departments;
--�����ȣ, �����, �μ���ȣ, �μ���, ���޹�ȣ, ���޸� ���
select employee_id, emp_name, a.department_id, department_name, a.job_id, job_title
from employees a, departments b, jobs c
where a.department_id = b.department_id and a.job_id = c.job_id;

--�����ȣ, �����, ���� ,�ּҿ��޺�, ����, ����Ÿ��Ʋ
--�ּҿ��� ��% �̻��� �ް� �ִ��� ���
select employee_id, emp_name, salary, min_salary,
round(((salary-min_salary)/salary)*100,2)||'%', a.job_id,job_title
from employees a, jobs b
where a.job_id = b.job_id;

select job_id, job_title from jobs;

--job_title, manager ���ڰ� �� �ִ�
--�����ȣe, �����e, ���޹�ȣe, ���޸�j, ����e, �ִ����j�� ����Ͻÿ�???????????????????
select*from employees;
select*from jobs;
select*from departments;
select employee_id, emp_name, b.job_id, job_title, salary, max_salary 
from employees a, jobs b
where a.job_id = b.job_id and job_title like '%manager%';

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
);

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);
commit;
select*from stu_grade;
select avg from stu_score;
--case when dhen grade�÷� 90���̻� A...bcdf �������
select no,name,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_grade, stu_score;

--non equi join
select no,name,avg,grade
from stu_score,stu_grade --���� �÷��� ����, �׷����� join�غ��ڴ�: non equi join
where avg between low_score and high_score
order by no
;

update stu_grade set low_score=92
where grade = 'A';

--��������� �������� �����
select*from kor_loan_status;
--������ ���� �հ踦 ����Ͻÿ�
select region, gubun, to_char(sum(loan_jan_amt),'999,999,999')||'���'
from kor_loan_status
group by region, gubun
order by region
;
--�⵵��,������,�����հ�ݾ�
select*from kor_loan_status;
select substr(period,1,4),region, to_char(sum(loan_jan_amt),'999,999,999')||'���'
from kor_loan_status
group by substr(period,1,4), region
order by region
;
--�ð��뺰,���ɴ뺰 �Ǹŷ� �� ���� ����Ͻÿ�
select *from lotte_product;
select time_cd, age_cd, sum(purh_amt) a
from lotte_product
group by time_cd, age_cd
order by a desc
;
--�̸���,�ݾ��հ� ���
select*from shop_product;

select name, sum(amount)
from shop_product
where pdate>= '2024/03/01'
group by name
;
--customer_rank ���̺� ����
--rank, 100�� �̸�: bronze / 200�� �̸�: silver / 300�̸�: gold / 300���̻�: platinum
create table customer_rank(
rank varchar2(2) primary key,
low_amount number(30) not null,
high_amount number(30) not null
);
insert into customer_rank values(
'B',0,999999
);
insert into customer_rank values(
'S',1000000,1999999
);
insert into customer_rank values(
'G',2000000,2999999
);
insert into customer_rank values(
'P',3000000,9999999999999
);
commit;

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
