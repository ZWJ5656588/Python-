// 插入一个数据
/*
集合创建之前我们首先创建的是数据库
 */
// 如果切入到了一个不存在的数据库可以使用db，集合名称，insert(),创建一个集合
// 数据库同时也会生效
use test_2
db.stu_test.insert({"name":"小王","age":18})


// 查询指定集合内的数据
db.stu_test.find()
// 拿到一个字典
// object id 是一个十六进制的数据，是谓一致


// 使用单引号进行数据插入
db.stu_test.insert({name:'xiaohong',age:20})


// 数据保存
db.stu_test.insert({_id:10010,name:'xiaoming',age:18})
db.stu_test.insert({_id:10010,name:'xiaoming',age:40}) // 错误，_id不能重复
// 更改某一个id的局部数据要用save
db.stu_test.save({_id:10010,name:'xiaoming',age:40}) // 正确


/*
数据更新(只写局部数据进行更新)
*/
// 将原有的xiaoming改成xiaozhao
db.stu_test.update({name:'xiaowang'},{name:'xiaozhao'}) //丢失数据
// 如果直接向上面这种使用update，会造成数据中其余键值对丢失，可以进行完善
db.stu_test.update({name:'xiaoming'},{$set:{name:'xiaozhu'}})
// 使用$set:{} 确定需要修改的字段，不会对其余字段造成影响


// 删除数据
// 删除第一次出现的xiaowang的数据
db.stu_test.remove({name:'xiaowang'},{justone:True})

