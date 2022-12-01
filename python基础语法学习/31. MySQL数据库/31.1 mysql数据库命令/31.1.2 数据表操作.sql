-- 1.查询当前数据库下所有的表
-- show tables;

-- 2. 创建表
-- 表名 classes
create table classes
(
    -- 字段
    -- unsigned 无符号sql
    -- unique 唯一
    -- auto_increment 自增长
    -- 主键非空
    id int unsigned auto_increment primary key not null,
    -- 如果声明最后一个字段 则字段结尾不能任何符号
    name varchar(10)  -- 最大长度10
);

create table students
(
    id int unsigned auto_increment primary key not null ,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    -- decimal(5,2) 表示小数总共五位，其中小数点后两位
    height decimal(5,2),
    gender enum('男','女','人妖','未知'),
    cls_id int unsigned default 0

);


-- 2. 查询表结构

desc classes ;

-- 3. 创建表后添加字段
alter table students add birthday datetime not null ;

-- 4.修改字段 重命名
alter table students change birthday birth date not null ;

-- 5.修改字段，不重命名
alter table students modify birth date;

-- 6.删除字段
alter table students drop birth;

-- 7.查看表的创建过程
show create table students;

-- 8. 表中数据通配符全查询，此时还未插入数据，所以是空字段
select * from students;

-- 9. 指定字段查询数据，此时还未插入数据，所以是空字段
select id,name from students;

-- 10 插入数据
-- 如果id 一开始不使用自增长，后面将从所定义过的最大值开始增长
insert into students (id,name) values (4,'朱文峻'),(2,'安娜');

-- 11. 数据修改
update students set id=2,name='anna' where id=4;

update students set height=182,gender='男',age=21 where  id=1;
update students set name='大海' ,height=170,gender='男',age=33 where  id=2;

insert into students (id, name, age, height, gender, cls_id)
values (3,'安娜',18,178.256,'女',2);

-- 12.物理删除数据
delete from students where id=5;

insert into students values (0,'顾安',30,176.24,'男',1),(0,'王逸群',21,172.263,'未知',1),(0,'孙起杰',21,179.999,'人妖',0);

insert into students(id, name, age, height, gender)
values (0,'大头',22,175.6,'男');

