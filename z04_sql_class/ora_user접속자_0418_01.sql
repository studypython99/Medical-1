--�����ִ� ���̺� �˻�
SELECT
    * FROM tab;
    
select*from employees;    --f9: ���ٸ� ����, f5: ��ü����

--���̺� ���� Ȯ��
desc employees;

--���̺� ����
create table stu_score (
    no number(2),
    kor number(3),
    eng number(3),
    avg number(5,2) --xxx.xx �� 5�ڸ�, 
);
--Į��(no,kor,eng,avg)�� ��� �Է���
insert into stu_score(no,kor,eng,avg) values (
1,100,99,(100+99)/2
);
--Į���� ��������
insert into stu_score values(
2,95,98,(95+98)/2
);

select*from stu_score;

create table num(
no number,
name varchar2(10),
kor number,
eng number,
avg number(4,1)
);
select*from num;

--���� ��¥
--dual: �������̺�
select sysdate from dual; --24/04/18

--��¥ ���� ����: to_char ����ȯ>>���� ����,'yyyy-mm-dd HH:mi:ss'
select to_char(sysdate,'yyyy-mm-dd HH:mi:ss') from dual;--2024-04-18 01:07:52

select to_char(sysdate,'HH:mi:ss') from dual;

select sysdate+100 from dual; --24/07/27
select sysdate+1000 from dual; --27/01/13
select sysdate-to_date('24/01/01') from dual;--108.xx