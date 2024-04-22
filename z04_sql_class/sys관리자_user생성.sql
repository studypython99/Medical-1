--c##생략가능 명령어
alter session set "_oracle_script"=true;
--생성
create user "ORA_USER3" identified by 1111;
--권한부여
grant connect, resource, dba to "ORA_USER3";
--전체보기
select * from all_users;