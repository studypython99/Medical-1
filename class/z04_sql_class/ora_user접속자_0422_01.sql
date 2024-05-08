select*from employees;

--as xxx ������ �����ϱ�, as ��������! ""�߰��� �̸� �״�� ��ũ��Ʈ �ݿ���
select salary, salary*1400, salary*1400*12 Y_sal from employees;

select*from stu_score;

select no,name,kor,eng,math,total,avg,rank from stu_score; 

select department_id from employees;

--null : 0���� �����
select nvl(department_id,0) from employees;

select*from employees;

--���ް��, comission_pct�� null�� ǥ�õȴ�
--��Ī: as���, "": Ű���带 �ִ� �״�� ���
select salary, salary + (salary*nvl(commission_pct,0)) as "Realsal" from employees;

select salary as �⺽ from employees;--�����ϸ� ��������...

select*from departments;
--�μ���ȣ, �μ��̸��� ����Ͻÿ�
select department_id, department_name from departments;

--concat: �������� �����͸� 1���� ���ļ� �Ѱܾ� �� ��� ��� || (shift+\)
--ex) ȫ�浿, ������, �̼���, ������, �豸 
--split(): �и� ����Ʈ �迭�� ����

select*from stu_score;

select kor||','||eng||','||math stu from stu_score;

select kor+eng+math as total, (kor+eng+math)/3 from stu_score;

--�ߺ�����: distinct
--where: ������ // not �����ϰ� �˻�: is not null
select DISTINCT department_id from employees where department_id is not null;

--manager_id
select DISTINCT manager_id from employees where manager_id is not null;

select*from employees;

--id: 200���� �޿��� ����ʹ�. 200,201,202
select employee_id, salary from employees
where employee_id = 200 or employee_id = 201 or employee_id = 202;

--200�̻� 203����
select*from employees
where employee_id >=200 and employee_id <=203;

--150���� 200�̻�
select*from employees
where employee_id <=150 or employee_id>=200;

--department_id 10,30,50�� �ش��ϴ� ����� ���
select*from employees
where department_id=10 or department_id=30 or department_id=50;

--���� 6000~9000�� ����� ����Ͻÿ�
select*from employees
where salary>= 6000 and salary<=9000;

--���� 6,7,8000�� ���
--����: order by �÷�, asc:��������, desc:��������
select*from employees
where salary=6000 or salary=7000 or salary=8000
order by salary desc;

--�μ���ȣ(department_id)�� 50���̸鼭, ����(salary)�� 8000�̻��� ���
select*from employees
where department_id=50 and salary >=8000;

--�Ի����� ����(asc)����
select hire_date from employees
order by hire_date ASC;

--�Ի����� ����(desc)����
select hire_date from employees
order by hire_date desc;

--02/01/01���� �Ի����� ����
select emp_name, hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc;

select hire_date, hire_date+100 from employees;
--�ݿø� round(����,�ڸ�������)
select round(sysdate-hire_date,2) from employees;

select*from employees;
--������ġ��� ||��ɾ� ���, (+�ȵ�;;)
select emp_name||email from employees;

--�Ի��� 05�� �̻� 06�� �����̸鼭
--������ 6000 �̻��� ����� �Ի����� ���������Ͻÿ�
select emp_name, hire_date, salary from employees
where hire_date>='05/01/01' and hire_date<'07/01/01' and salary >6000
order by hire_date desc;
