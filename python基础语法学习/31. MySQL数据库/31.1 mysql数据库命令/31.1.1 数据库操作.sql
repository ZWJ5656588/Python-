-- 这是一个注释
-- 2.通过指令进入到数据库

-- 数据类型
/*
 decimal表示浮点数，如decimal(5,2)表示共存5位数，小数占2位

- char表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '
- varchar表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'

 */

show databases ;

-- 3.进入指定数据库
 use 数据库名称;

-- 4.查看当前使用的数据库
 select database();

-- 5. 创建数据库
 create database 数据库名称 charset =utf8;       -- 使用navicat软件可以看到不乱码的中文数据 windows下cmd查看数据库肯定乱码

-- 6 查看数据库创建过程
show create database 数据库名称;

-- 7.退出交互模式
 \q;

create table students2(
    id int unsigned auto_increment primary key not null ,
    name varchar(20),
    age tinyint unsigned,
    sex enum('男','女'),
    hobbies varchar(10),
    -- unique 约束 ，若字段值不为空，则全表唯一
    tel char(11) not null unique
);
insert into  students2 values (0,'张三',18,'男','唱'),(0,'李四',19,'男','跳'),(0,'小红',19,'女','rap'),(0,'只因',20,'男','篮球');

select * from students2 where sex='男';

delete from students2 where id=3;

update students2 set sex='女';






