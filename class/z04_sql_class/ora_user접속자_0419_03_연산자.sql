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
1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values (
5,'�豸',100,100,100,300,100,1
);
commit;
select * from stu_score;

--������� numberŸ���� ���
select*from stu_score;

insert into stu_score values(
6,'������',100,95,96,(100+95+96),(100+95+96)/3,1
);

--��ȣ,�̸�,����,����-20,���,����-20�� ����� ���
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select*from employees;
--ȯ����� 1�޷�: 1381.79��
select employee_id,emp_name,salary,salary*138.79 from employees;

--commission_pct, ��������: ����+(����*commission)
select*from employees;

select emp_name, salary, salary*(1+nvl(commission_pct,0)) from employees;
--nvl(�÷�,0)
select employee_id,emp_name,nvl(commission_pct,0) from employees;