--���̺� ����
create table emp01(
emp_id number(6),
emp_name varchar2(80),
hire_date date
);

--���̺� ���� �� ������ �����ϱ�
desc employees;
create table emp02 as --2. emp02�� �Է�
select*from employees; --1. ������ ���θ�

--����, �Ʒ� �ΰ��� ����.
select*from emp02;
select*from employees;

--���̺� ������ �����ϱ�
create table emp03 as --2. ������ ������ ����
select *from employees where 1=2; --1.�ϳ��� �ȸ¾Ƽ� ������ �� ������
--emp03�� ����0����x
select*from emp03;
select*from employees;

--���̺��� �����ϸ鼭, �����͸� �����ϱ�, ���̺� ������ �ٸ� ��
insert into emp01(emp_id,emp_name,hire_date)
select employee_id,emp_name,hire_date from employees;

select*from emp01; --�÷� 3��
select*from employees; --�÷� 14��
--1�� ������ �߰�
insert into emp01 values(
207,'ȫ�浿','2024-04-26'
);

--���̺��� �����ϸ鼭, �����͸� �����ϱ�
insert into emp03
select*from employees;

select*from emp03;
select*from emp01 order by emp_id desc;
select*from employees;

select*from emp01 order by emp_id desc;

--drop table s_info;
--drop table m_date;
desc member;

--�÷� Ÿ�Ժ���
alter table member
modify(stu_name varchar2(30));

--�÷� ����
alter table member
drop column pw;
desc member;

--�÷� �߰�, �������ٿ� �߰��߰�
alter table member
add(pw varchar2(30));
desc member;

select*from member;

select mno,id,pw,stu_name,gender from member;
select*from member;

insert into member values(
seq_mno.nextval,'ggg','1111','ȫ����','male' --�̷����ϸ� ����,(������ �ٸ���)
);

--�÷��� ������ �ٲٰ�ʹ�, ���� �� �߰�
alter table member modify stu_name invisible; --stu �����
alter table member modify gender invisible; --gen �����
alter table member modify stu_name visible; --stu ��Ÿ����
alter table member modify gender visible; --gen ��Ÿ����
select*from member;
--�÷� �Ͻ��� �������
alter table member
set unused(id);--id ������
--������� ����
alter table member
drop unused columns; --�÷� �������� �����
select*from member;

--���̺����
--drop table emp03;

--���̺��̸� ����
rename emp01 to employees01;

--���Ἲ ��������

--foreign key�� �ٸ� ���̺��� ������ �Է½�,
--����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��
