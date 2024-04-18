--테이블 생성
create table stu_score(
no number(4) primary key,--대표키로 설정되어 중복,null값이 들어갈 수 없다.
name varchar2(30),--varchar2: 가변길이 문자열
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(6)
);

--데이터 입력: insert
insert into stu_score (no,name,kor,eng,math,total,avg) values(
1,'홍길동',100,100,100,300,100.00
);

--데이터 검색: select
select*from stu_score;

--완료
commit;

--1개 데이터 수정: update
update stu_score set name='홍길자' where no=1;

select*from stu_score;

--되돌리기
rollback;

desc stu_score;

--삭제: delete
delete stu_score where no=1;

select*from stu_score;

drop table stu_score; --롤백 없음, 복구안됨;;

--갖고있는 모든 테이블을 보여줌
select*from tab;
