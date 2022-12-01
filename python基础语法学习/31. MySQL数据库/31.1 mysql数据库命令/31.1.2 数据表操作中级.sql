-- 创建数据库
create database python_test_1 charset=utf8;

-- 使用数据库
use python_test_1;

-- students表
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',  # gender=1代表‘男’ 类推
    cls_id int unsigned default 0,
    is_delete  bit default  0
);

-- classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);

-- 向students表中插入数据
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);


-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期");



-- 对表名进行别名设置
select s.id,s.name,s.gender from students as s;
select id as 序号,name as 姓名,gender as 性别 from students;
select id as order_number ,name as 姓名,gender as 性别 from students;

# 例1：查询编号大于3的学生

select * from students where id > 3;

# 例2：查询编号不大于4的学生

select * from students where id <= 4;

# 例3：查询姓名不是“黄蓉”的学生

select * from students where name != '黄蓉';

-- 例4：查询没被删除的学生

select * from students where is_delete=0;



-- 逻辑运算符

-- and
-- or
-- not

-- 例5：查询编号大于3的女同学

select * from students where id > 3 and gender=0;

-- 例6：查询编号小于4或没被删除的学生

select * from students where id < 4 or is_delete=0;

# 例7：查询姓黄的学生

select * from students where name like '黄%';

# 例8：查询姓黄并且“名”是一个字的学生

select * from students where name like '黄_';

# 例9：查询姓黄或叫靖的学生

select * from students where name like '黄%' or name like '%靖';

# 查询周姓两个字的
select * from  students where name like '周_';

select * from students where name like '黄%' or name like '_杰';

# --例10：查询编号是1或3或8的学生

select * from students where id in(1,3,8);  # 不连续范围

# - between ... and ...表示在一个连续的范围内

# 例11：查询编号为3至8的学生

select * from students where id between 3 and 8;  # 连续查询 包括3,包括8

# 例12：查询编号是3至8的男生

select * from students where (id between 3 and 8) and gender='男';


#  空字符串在数据库中不等同于none
# 例13：查询没有填写身高的学生

select * from students where height is null;

# - 判非空is not null

# 例14：查询填写了身高的学生

select * from students where height is not null;

# 例15：查询填写了身高的男生
select * from students where height is not null and gender=1;



-- --------------------------- 排序 ------------------------------
# 1.查询未删除的男生信息 按学号降序
# 先确定范围，再排序,默认升序(asc) 降序需要写明desc
select * from students where gender=1 order by  id desc ;

# 例3：显示所有的学生信息，先按照年龄从大到小排序，当年龄相同时，按照身高从高到矮排序

select * from students  order by age desc,height desc;  #当年龄相同时，按照身高降序，多个条件通过逗号隔开




# -----------------为了快速得到统计数据，经常会用到如下5个聚合函数-----------------------


-- count(*)表示计算总行数，括号中写星与列名，结果是相同的

-- 例1：查询学生总数 也是这个表的总行数

select count(*) from students;
# 等价于
select count(name) from students;

-- 2. 查询女生编号的最大值
select max(id) from students where gender=2;

-- 3.求和
-- 查询未删除女生得总年龄
select sum(height) from students where gender='男' and is_delete=0;

-- 平均值
select avg(height) from students where name like '周%';


-- ------------------  分组  ---------------------------
# group by
#
# 1. group by的含义:将查询结果按照1个或多个字段进行分组，字段值相同的为一组
# 2. group by可用于单个字段分组，也可用于多个字段分组
select gender from students group by gender;

-- 分组显示 group by + group concat(字段名)
select gender as 性别,group_concat(name) as 姓名 from students group by gender;


-- 分别统计性别为男/女的人的个数
select gender,count(*) from students group by gender;




-- -------------------------- 分页  -------------------------
-- select * from 表名 limit start,count;

-- 1. 查询前三名男同学
select * from students where gender='男' limit 0,4;   # 0表示从第一个开始，3的意思是数量

-- 2.查询前五条数据  从第一个开始的话 可以省略0
select  * from students limit 5;

-- 4.查询id 为 6-10的数据，用户设置的开始位置-1
select * from students where id>=6 and id <=10;
select * from students limit  5,5;  # 这个类似于索引,从索引5(id=6)往后取5个数据
select * from students order by id desc limit 4,5 ;   # 这个情况是以最后id=14作为索引0，往前取5个数据

# !!! 不能在limit写公式 且limit翻页必须要在最后一页

