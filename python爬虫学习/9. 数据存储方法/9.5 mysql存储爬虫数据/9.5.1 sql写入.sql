-- /9.5 baidu招聘
create table baidu(
    id int primary key auto_increment not null,
    education varchar(255) not null,
    name varchar(255) not null,
    serviceCondition varchar(255)
)


-- /7.8 mysql储存芒果
create table mangguo(
    id int primary key atuo_increment not null,
    title varchar(255) not null,
    updateinfo varchar(255) not null,
    story varchar(1000) not null
);

insert into mangguo (id, title, updateinfo, story) values ('%d','%s','%s','%s') % (0,title,updateinfo,story)

