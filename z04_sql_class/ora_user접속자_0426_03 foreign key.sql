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

--foreign key, �ܷ�Ű , ex) �Խñ� �ۼ���, ��� �߰�, �Խñ� ������ ��۵� ��� ����
--drop table emp01;

--emp01 ���̺� ����
create table emp01(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9),
deptno number(2)
);
--emp01 empno Ÿ�Ժ���
alter table emp01
modify (empno number(6));
alter table emp01
modify (deptno number(6));

--dept01 ���̺� ����
create table dept01(
deptno number(2) primary key,
dept_name varchar2(20)
);
--Į���� Ÿ�� ����
alter table dept01
modify(dept_name varchar2(80)); --���������� ���� �� ũ��, ���� �� ������ 
--Į�� ���� �߰�
insert into dept01(deptno,dept_name)
select department_id, department_name from departments;

insert into emp01 values(
1,'ȫ�浿','0001',10
);
insert into emp01 values(
2,'������','0002',20
);
insert into emp01 values(
3,'�̼���','0002',30
);

--deptno 10~270���� �ִ�
insert into emp01 values(
4,'�豸','0003',270
);
insert into emp01 values(
5,'������','0004',280 --270������ ������ ��ϺҰ�;
);-- �ܷ�Ű ���� �� �Է°���;

--foreign key ���� �� �Է��غ���
alter table emp01
drop constraint fk_deptno;
commit;

--emp01 foreign key �߰�: fk_deptno��� �̸����� deptno�� foreign key�� ����Ұž�
--fk_deptno��Ī
--add constraint ��Ī foreign key(�����÷�) references �ٸ����̺�(�÷��̸�)
alter table emp01
add constraint fk_deptno foreign key(deptno)
REFERENCES dept01(deptno);

select*from departments;

desc member;
--
create table board(
bno number(4) primary key,
id varchar2(30),
btitle varchar2(1000),
bcontent varchar2(3000)
);
insert into board values(
1,'aaa','�Խñ�1','����1'
);
insert into board values(
8,'bbb','�Խñ�8','����8' -- 2~8���� �Է�
);
commit;
select*from board;

--foreign key �����
alter table board
add constraint fk_id foreign key (id)
references member(id);

--comment ���̺� ������̺�

--cno number(4) primary key
--bno number(4) #���̺��� �� foreign key ����ϱ�
--cpw varchar2(20)
--ccontent varchar2(1000)

create table comments(
cno number(4) primary key,
bno number(4),
cpw varchar2(20),
ccontent varchar2(1000),
constraint fk_bno foreign key(bno)
references board(bno)
);
drop table ccomment; --alter �ҰŸ� ����� �ٽ�����..

--��۴ޱ� 15 21 35 42 55
insert into comments values(
5,5,'1111','��۳���1'
);
-- fk�� ����� �� ����, 
-- fkŰ�� ��ϵǾ��ִ� ��� ������ ����
-- fkŰ�� ��ϵǾ��ִ� ��� ������ ����
delete board where bno=5;
commit;

--�ܷ�Ű ����
alter table board drop constraints fk_id;
select*from board;
select*from comments;

delete board where bno=1; --���Ἲ ����,
--fk_cno�� ������ �ǵ��� ��.
alter table comments 
add constraint fk_bno foreign key(bno)
references comments(bno) on delete cascade;

delete comments where cno=2;

--check ��������, Ư������ ����, Ư������ �Էµǵ��� �� ex) male/female
create table emp(
empno number(4) primary key,
ename varchar2(20) not null,
job varchar2(9) default '0001', --�÷��� �����͸� ���� ������ �ڵ����� 0001 �����
sal number(7,2) check(sal between 2000 and 20000),
gender varchar2(6) check(gender in('����','����'))
);

insert into emp(empno,ename,job,sal,gender) values(
1,'ȫ�浿','0002',3000,'����'
);
insert into emp(empno,ename,job,sal,gender) values(
2,'������','0003',4000,'����'
);
insert into emp(empno,ename,job,sal,gender) values(
3,'�̼���','0004',5000,'����' --gender �������� �����.
);
insert into emp(empno,ename,job,sal,gender) values(
4,'������','0005',2000,'����'
);
insert into emp(empno,ename,job,sal,gender) values(
5,'�豸','0006',1000,'����' --sal 2000~20000 ���̰��� ����
);
insert into emp(empno,ename,sal,gender) values(--job����
6,'������',3000,'����' -- job 0001 ����Ʈ ����
);
select*from emp;