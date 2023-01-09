// 查询age大于18的数据
db.stu_info.find({age: {$gte: 18}})

// 使用"$in"进行返回查询 符合18或28的返回
db.stu_info.find({age: {$in: [18, 28]}})

// 并且查询
db.stu_info.find({age: 18, hometown: "桃花岛"})

// 或者查询
// db.集合名称.find({$or: [{查询条件}， {查询条件}]})
db.stu_info.find({$or: [{age: 18}, {hometown: "桃花岛"}]})

// 将之前所学的查询进行整合使用
// 如果语句过长，可以使用编辑器写上查询语句 并且换行不影响
db.stu_info.find(
    {
        $or: [{age: {$gte: 45}},
            {
            hometown: {
                $in:["桃花岛", "华山"]
                }
            }]
    })






// 查询两个学生
db.stu_info.aggregate(
  {$limit: 2}
)

// 案例：取出当前从第一位学生之后的一条学生信息
db.stu_info.aggregate({$skip: 1}, {$limit: 1}


// 使⽤$where后⾯写⼀个函数， 返回满⾜条件的数据
// 查询年龄⼤于30的学⽣
db.stu_1.find({$where: function(){return this.age<=18}})


// mongodb中的投影
// 在查询到的返回结果中，只选择必要的字段
// 如果不想显示_id，需要单独设置_id: 0
// db.集合名称.find({条件}, {字段名称1, 字段名称2...})

db.stu_info.find({age: {$gt: 18}}, {name: 1, _id: 0})

// 无条件进行投影查询
db.stu_info.find({}, {name: 1, _id: 0})