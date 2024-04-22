--10번도 아니고 50번도 아닌, not != <> ^=
select department_id from employees
where department_id != 10 and department_id != 50
order by department_id;

--5000이상 9000이하
select salary from employees
where salary >=5000 and salary <=9000
order by salary
;

--평균이 99점 이상인 학생을 검색
insert into member (id,pw,name,phone) values (
'aaa','1111','홍길동','010-1111-1111'
);
insert into member values (
'bbb','1111','유관순','010-2222-2222'
);
insert into member (id,name,phone) values(
'ccc','이순신','010-3333-3333'
);
select*from students;

--no= 1의 이름을 홍길동 으로 변경
update students set name='홍길동'
where no=1;

update students set name='유관순'
where no=2;

update students set name='이순신'
where no=3;

update students set name='강감찬'
where no=4;

update students set name='김구'
where no=5;

update students set name='좌의정'
where no=6;

update students set name='영의정'
where no=7;

update students set name='이익'
where no=8;

update students set name='정약용'
where no=9;

update students set name='이세돌'
where no=10;

--국어 80, 평균 85점 이상인 학생을 출력
select no, name, kor, avg from students
where kor>=80 and avg >=85;

--국어 70,80,90점 학생출력
select no, name, kor from students
where kor=70 or kor=80 or kor=90;

update students set kor = 100, total = 100+eng+math, avg = (100+eng+math)/3
where no=1;

select *from students
where no=1;

--국어점수가 70~90점 학생출력
select no, name, kor from students
where kor>=70 and kor<=90;

--between a and b, a와 b 사이(이상이하)
--not: between 이외 (미만초과)
select no, name, kor from students
where kor not between 70 and 90;

--날짜도 between a and b
select hire_date from employees
order by hire_date;
--99년보다 크거나 같고, 01년보다 작거나 같은 사원
select hire_date from employees
where hire_date between '99/01/01' and '01/12/31'
order by hire_date;

--in: 동일한 필드가 여러 값중에(70,80,90) 하나를 검색할 경우 or
select name,kor from students
where kor in(70,80,90);

--이름검색
select*from students
where name='홍길동';
--like: 특정단어가 포함되어있는 것을 검색 
--홍 이라는 글자가 있다면 나타내라
select*from students
--where name like '홍%';--홍으로 시작하는
--where name like '%홍';--홍으로 끝나는
--where name like '%홍%';--홍'포함되어있는 단어
where name like '%홍%';

-- _: 한칸 공간을 사용
select*from students
where name like '_길%';
--3번째에 t 가 들어가있는 이름
select*from students
where name like '__t%';

--이름이 4자리인, 3버째 r이 들어가 있는 이름 검색
select*from students
where name like '__r_';
--4자리인 이름
select name from students
where length(name) =4;

--이름이 A로 시작되는

select*from students
where name like 'A%';

--이름에 a가 들어가 있는
select*from students
where name like '%a%';

--대소문자 구분없이 a가 들어있는 학생
--소문자 치환(lower), 대문자 치환(upper), 첫글자 대문자(initcap)
select*from students
where lower (name) like '%a%'

--a가 포함되지 않은 이름
select *from students
where name not like '%a%';

select mamager_id from employees;
--manager_id 100인 사원 검색
select employee_id, emp_name,manager_id from employees
where manager_id=100;

select employee_id, emp_name, manager_id from employees
where manager_id = null; --null검색 안됨;;

select employee_id, emp_name, manager_id from employees
where manager_id is not null;

--정렬 asc(ascending), desc(descending) 한글도 가능

select*from students
order by name asc;

--1차: 국어역순정렬, 2차: 영어순차정렬
select*from students
order by kor desc, eng asc;

--total로 역순정렬
select*from students
order by total desc;

--컬럼 추가
alter table students add rank number(3);

update students set rank=0;

commit;

--등수, 보여주기만 하고 저장은 안됨;;
select no, name,total,rank() over(order by total desc) as rank from students;

--수정, 1번 13등으로
update students set rank=13
where no=1;

-- 등수
select no,rank() over(order by total desc) as rank from students
;
update students s1 set rank = (select ranks
from (select no no2, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no2 )
;
select * from students;

-- 등수
select no,rank() over(order by total desc) as rank from students
;
--이중쿼리;;;;
update students s1 set rank = (select ranks
from (select no, rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no )
;
select * from students;

--전체중에서 국어 70이상
select*from students
where kor>=70;
--평균 80이상 중에서 국어 70이상
select*from (select*from students where avg>=80)
where kor>=70;