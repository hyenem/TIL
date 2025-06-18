drop schema if exists back_prod;
create schema if not exists back_prod 
	character set utf8mb4 
	collate utf8mb4_0900_as_cs;

use back_prod;

drop table if exists user;
create table if not exists user(
  id varchar(10) primary key,
  pass varchar(10) not null,
  name varchar(20) not null
);
insert into user values ('scsa',1234,'홍길동');

drop table if exists product;
create table if not exists product(
  num varchar(10) primary key,
  title varchar(20) not null,
  price int not null
);
insert into product values ('1001','NoteBook',10000);
insert into product values ('1002','Phone',   20000);
insert into product values ('1003','Computer',30000);
commit;

select * from user;
select * from product;
