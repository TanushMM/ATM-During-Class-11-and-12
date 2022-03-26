create database atm;
use atm;
create table sss(
accno char(16) primary key,
pin char(4),
balance char(25),
name varchar(50),
age varchar(2),
date varchar(2),
month varchar(2),
year char(4),
phonenumber char(10));

insert into sss values(1234123412341234,2004,35000,'Tanush',16,5,6,2004,1234567890);
insert into sss values(1111000011110000,2004,15000,'Adithyanarayanan',17,17,7,2003,2468013579);
insert into sss values(1111222233334444,2003,49000,'Vinod',17,1,3,2003,0987654321);
insert into sss values(1122334455667788,2000,76000,'Bharath',17,6,6,2003,1357924680);

