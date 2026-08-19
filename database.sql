create database Restaurant;
use Restaurant;
set autocommit=0;
create table admin(aname varchar(25) not null,Password varchar(50) not null);
select * from admin;
create table user(userid int auto_increment primary key,username varchar(40) not null,
mobilenum varchar(40) not null);
select * from user;
create table menu(itemid int primary key,itemname varchar(50) not null,
catogery varchar(50),quantity int,price int not null);
select * from menu;
create table cart(cartid int auto_increment primary key,itemname varchar(50) not null,
quantity int);
select * from cart;
create table orders(orderid int auto_increment primary key,orderdate date);
alter table orders add cartid int;
alter table orders add constraint fk_tabl foreign key(cartid) references cart(cartid);
alter table orders add itemname varchar(50);
alter table orders add quantity int;
alter table orders add price int;
alter table orders add costprice int;
select * from orders;
insert into admin(aname,password) values('Likki','Likki@123');
show tables;
alter table menu add costprice int;
commit;
