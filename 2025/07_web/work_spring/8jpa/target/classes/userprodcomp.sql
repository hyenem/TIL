drop schema if exists sf_prod;
create schema if not exists sf_prod 
	character set utf8mb4 
	collate utf8mb4_0900_as_cs;

use sf_prod;

drop table if exists user;
create table if not exists user(
  id varchar(10) primary key,
  pass varchar(10) not null,
  name varchar(20) not null
);
insert into user values ('scsa',1234,'홍길동');

drop table if exists product;
drop table if exists company;

create table if not exists company(
  cno int primary key,
  name varchar(10) not null,
  loc varchar(10)
);
insert into company values (10,'삼성','서울'),
(20,'엘지','인천'),(30,'현대','경기');

create table if not exists product(
  num varchar(10) primary key,
  title varchar(20) not null,
  price int not null,
  cno int,
  foreign key(cno) references company(cno)
);
insert into product values ('1001','NoteBook',10000,20);
insert into product values ('1002','Phone',   20000,10);
insert into product values ('1003','Computer',30000,30);
commit;

select * from user;
select * from company;
select * from product;