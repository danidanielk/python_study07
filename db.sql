create table coffee(
c_no number(3) primary key,
c_name varchar2(25char) not null,
c_price number(10) not null,
c_type varchar2(15char) not null
);

create sequence coffee_seq; 

select * from coffee;
drop table coffee cascade constraint purge;
drop sequence coffee_seq;


select*  from (select rownum as rn, avg(c_price) from (select avg(c_price) from coffee group by c_type order by avg(c_price))) ;
select * from (select rownum as rn, avg(c_price) from(select avg(c_price) from coffee group by c_type ))having rn between 0 and 2;