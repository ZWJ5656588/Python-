/*
-- --------------------------- 视图 -----------------------------------
1. 问题
对于复杂的查询，往往是有多个数据表进行关联查询而得到，如果数据库因为需求等原因发生了改变，为了保证查询出来的数据与之前相同，则需要在多个地方进行修改，维护起来非常麻烦
解决办法：定义视图，类比于把sql语句封装到函数中
2. 视图是什么
通俗的讲，视图就是一条SELECT语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。
视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；
方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性
 */

-- 定义视图
create  view  视图名称  as select 语句
-- 视图名称可以看做一个函数名称

-- 查询视图
-- 本质上视图其实是一张虚表,在数据库中创建视图，查询时会跟着表一起查出来
show tables;



-- 案例 查询安徽省下所有的城市，使用视图
select city.* from tb_areas as city INNER JOIN tb_areas
as province on city.pid=province.aid where province.atitle="安徽省";

-- --------------       视图封装         -------------------------
create view  v_city_anhui as select city.* from tb_areas as city INNER JOIN tb_areas
as province on city.pid=province.aid where province.atitle="安徽省";

-- 查看视图
select * from v_city_anhui;



