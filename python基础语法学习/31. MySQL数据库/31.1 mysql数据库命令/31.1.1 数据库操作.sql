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







