--���Ἲ ��������

--foreign key�� �ٸ� ���̺��� ������ �Է½�,
--����Ǿ� �ִ� ���� ���̺� �Է��Ϸ��� �����Ͱ� �ִ��� Ȯ��
--������ �����͸� ���� �� �ֵ��� �Ѵ�.

--drop table employees01;
--drop table emp02;
--drop table member;
--drop table board;

create table member(
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6)
);

insert into member values(
'aaa','1111','ȫ�浿','male'
);

insert into member (id,pw,name) values(
'bbb','1111','������');

insert into member(id,pw) values(
'ccc','1111');

insert into member (id,pw,name) values(
'a','1111','ȫ�浿');

select*from member;
--��������: not null: null���� ����, �ߺ��� ����!
create table emp02(
empno number(4) not null,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
insert into emp02 (empno,ename,job,deptno) values(
'1111','ȫ�浿','aa','11'
);
insert into emp02 (empno, ename, job, deptno) values(
'2222','ȫ����','bb','22');
insert into emp02 (empno, ename) values(
'3333','ȫ���');
select*from emp02;
--��������: unique: �ߺ��� ����, null���
create table emp03(
empno number(4) unique,
ename varchar2(10) not null,
job varchar2(9),
deptno number(2)
);
insert into emp03 (empno,ename,job,deptno) values(
'1111','ȫ�浿','aa','11'
);
insert into emp03 (empno,ename,job,deptno) values(
null,'ȫ�浿','aa','11'
);
insert into emp03 (empno,ename,job,deptno) values(
'3','�̼���','aa','11'
);
select*from emp03;

--1���� ȫ�浿�� ã�ƶ�
select * from emp03
where empno='1111';
--nullȫ�浿�� ã�ƶ�
select*from emp03
where empno is null and ename='ȫ�浿'; -- empno = null ;; �̰� �ȵ�;;

--null���� ��� ó���Ұ��ΰ�. ����ġó��!!
create table emp01(
empno number(4) primary key, --��ȣ�� �˻��ؼ� ã�� �� �ִ�. �ߺ����x
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);

--5�� null,1,2,3,1
insert into emp01 values(
1,'ȫ�浿','0001',1
);
insert into emp01 values(
3,'ȫ�浿','0001',1
);

select*from emp01;
--3��ȫ�浿 ã��
select*from emp01
where empno=3;