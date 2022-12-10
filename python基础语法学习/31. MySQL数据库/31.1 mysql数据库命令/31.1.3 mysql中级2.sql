-- ------------- 自关联 -----------------------
-- 1. 内连接查询
select * from students inner join  classes on students.cls_id=classes.id;
-- 查询所有字段，从学生表内查询，条件：学生表cls字段=班级表id
-- 内连接查询 如果表一数据对应不上表二数据，不显示

-- 2.左连接查询
-- 此处使用 as 为表起别名
select * from students as 主表 left join classes as 子表 on 主表.cls_id=子表.id;
-- 查询所有字段，根据学生表进行查询，左连接 on后面跟查询条件 班级表[子表]条件 班级表[id]=学生表[cls_id]
-- 此时学生表是主表 把学生表的所有数据查询出来 如果对应不上，则显子表示为空null
select * from classes as 主表 left join students 子表 on 主表.id=子表.cls_id;

--3.右连接查询
select * from students as s right join classes as c on s.cls_id=c.id;
-- 主表中只有两条数据，如果主表中的数据都在子表对应，全部显示
-- 如果班级表出现了python3班，没有绑定任何学生。查询班级表，则对应的python3班为null
-- 如果子表中有主表不存在的数据，则不显示


--  ------------------------- 自关联  ------------------------------
--通过关联使得id之间有关系 类比于类 对象等
-- windows默认编码集是gbk 会造成乱码 建议在navicat里写sql


/*- 设计省信息的表结构provinces
- - id
    - ptitle
- 设计市信息的表结构citys
- - id
    - ctitle
    - proid
- citys表的proid表示城市所属的省，对应着provinces表的id值 !!!


问题：
- 能不能将两个表合成一张表呢？
思考：
- 观察两张表发现，citys表比provinces表多一个列proid，其它列的类型都是一样的
意义：
- 存储的都是地区信息，而且每种信息的数据量有限，没必要增加一个新表，或者将来还要存储区、乡镇信息，都增加新表的开销太大
答案：

- 定义表areas，结构如下
  - id
  - atitle
  - pid
说明:
- 因为省没有所属的省份，所以可以填写为null
- 城市所属的省份pid，填写省所对应的编号id
- 这就是自关联，表中的某一列，关联了这个表中的另外一列，但是它们的业务逻辑含义是不一样的，城市信息的pid引用的是省信息的id
- 在这个表中，结构不变，可以添加区县、乡镇街道、村社区等信息
*/

create table tb_areas(
    aid int primary key ,
    atitle varchar(20),
    pid int
);

-- 自关联表示了表内部列的关系
select city.* from tb_areas as city INNER JOIN tb_areas
as province on city.pid=province.aid where province.atitle="安徽省";

-- 这里其实是引用了两次表，重命名两次,select city.* 只筛选出第一次引用的表的所有主键
-- 相当于把表复制一份再按照规则拼接，然后在按照select剪切

select * from tb_areas as zone INNER JOIN tb_areas
as city on zone.pid=city.aid where city.atitle="淮南市";

insert into classes(name) values ("python_04班");

