select emp_name, department_id from employees;

select*from departments;

select department_id, department_name from departments;

select * from departments, jobs;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);
--�����ȣ, ����̸�,�޿�,�Ի����� from employees;
select employee_id, emp_name, salary, create_date from employees;
--typeȮ��
desc employees;
/*
�̸�             ��?       ����           
-------------- -------- ------------ 
EMPLOYEE_ID    NOT NULL NUMBER(6)    
EMP_NAME       NOT NULL VARCHAR2(80) 
EMAIL                   VARCHAR2(50) 
PHONE_NUMBER            VARCHAR2(30) 
HIRE_DATE      NOT NULL DATE         
SALARY                  NUMBER(8,2)  
MANAGER_ID              NUMBER(6)    
COMMISSION_PCT          NUMBER(2,2)  
RETIRE_DATE             DATE         
DEPARTMENT_ID           NUMBER(6)    
JOB_ID                  VARCHAR2(10) 
CREATE_DATE             DATE         
UPDATE_DATE             DATE    
*/
