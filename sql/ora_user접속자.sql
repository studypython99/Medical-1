--���̺� ����
create table stu_score(
no number(4) primary key,--��ǥŰ�� �����Ǿ� �ߺ�,null���� �� �� ����.
name varchar2(30),--varchar2: �������� ���ڿ�
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(6)
);

--������ �Է�: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
1,'ȫ�浿',100,100,100,300,100.00
);

--������ �˻�: select
select*from stu_score;

--�Ϸ�
commit;

--1�� ������ ����: update
update stu_score set name='ȫ����' where no=1;

select*from stu_score;

--�ǵ�����
rollback;

desc stu_score;

--����: delete
delete stu_score where no=1;

select*from stu_score;

drop table stu_score; --�ѹ� ����, �����ȵ�;;

--�����ִ� ��� ���̺��� ������
select*from tab;
