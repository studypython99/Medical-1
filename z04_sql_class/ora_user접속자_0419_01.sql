select*from employees;

--ȸ������ ���̺� ����
create table member (
id varchar2(20),
pw varchar2(20),
name varchar2(20),
phone varchar2(20)
);
--������ �Է�
insert into member (id,pw,name,phone) values (
'aaa','1111','ȫ�浿','010-1010-1010'
);

insert into member values (
'aaa','1111','������','010-1010-1010'
);

insert into member (id,name,phone) values (
'ccc','�̼���','010-1010-1010' --�ѱ��� �ѱ��ڴ� 3�ڸ� �����Ѵ�.
);
/*�÷� �� ���� ���� 
insert into member values (
'ddd', '������','010-4444-4444'
);*/

select id,pw,name,phone from member;
--����
commit;

rollback;

select*from member; --����ڷ� �˻�
select id,name from member; --�����ڷ� id,name �˻�

insert into member values(
'ddd','111','������','010-2020-2020'
);

--��� ��ü ��й�ȣ 2222 ����
update member set pw='2222' where id='ccc';
select*from member; --����ڷ� �˻�

--������̺�
select*from tab;

--���̺� Ÿ�� Ȯ��
desc member;

--����Ŭ Ÿ��
--number(����), date(��¥), char(��������), varchar2(��������),clob(��뷮����)

--number: ����, �Ǽ�
--number(4): -9999 ~ +9999
CREATE table mem(
no number,--��������x
no2 number(4),--4�ڸ�����
no3 number(4,2)--xx.xx �Ҽ��� 2�ڸ��� �Ҵ��Ͻÿ�.
);

insert into mem (no,no2,no3) values (11,12,13.13);
insert into mem (no,no2,no3) values (21,22,23.23);
insert into mem (no,no2,no3) values (31,32,33.33);

select*from mem;
commit;
------------------------------------------------------------------
create table mem2(
no number(4,2),
mdate date,--�����Ͻú��� ���� ���� ����
mdate2 timestamp --date=timestamp(�и��ʱ��� ���� ���� 1��=1000)
);

insert into mem2(mdate)values('2024-04-19');
select*from mem2;
insert into mem2(mdate)values(sysdate);--sysdate: ����ð�
insert into mem2(mdate2)values(sysdate);--sysdate: ����ð�
insert into mem2(mdate, mdate2)values(sysdate,sysdate+30);

select*from mem2;
select to_char(mdate,'yyyy-mm-dd hh24:mi:ss')from mem2;
select to_char(mdate2,'yyyy-mm-dd hh24:mi:ss:ff')from mem2;

select * from mem2;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);

--�������� ���� char, varchar2
--char: ��������, �ӵ��� ������
insert into mem3 (tel) VALUES ('12345678');
insert into mem3 (tel) VALUES ('87654321');
insert into mem3 (tel) VALUES ('123');
insert into mem3 (tel) VALUES ('123456789');

--varchar2: ��������
insert into mem3 (name) values ('123456789');
insert into mem3 (name) values ('ȫ�浿');
insert into mem3 (name) values ('�Ż���'); --12�ڸ� �ʿ�
INSERT INTO MEM3 (NAME) VALUES ('AAA');
insert into mem3 (name) values ('aaa');

select upper(name) from mem3 where (name)='aaa';

--select: select,from ���� ������, ��ҹ��� ����x
select*from mem,mem2; --��� �÷��� ���

select department_id from employees;
