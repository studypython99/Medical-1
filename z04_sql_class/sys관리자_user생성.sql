--c##�������� ��ɾ�
alter session set "_oracle_script"=true;
--����
create user "ORA_USER3" identified by 1111;
--���Ѻο�
grant connect, resource, dba to "ORA_USER3";
--��ü����
select * from all_users;