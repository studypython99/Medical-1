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

--�÷� �߰�
alter table students add rank number(3);

update students set rank=0;

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