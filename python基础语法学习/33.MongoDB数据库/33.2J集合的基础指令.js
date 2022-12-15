// // 手动在数据库中创建集合
// // options是可选参数
//
// //
// db.CreateCollecion(name,options)
// db.CreateCollecion('stu')
// // 只有在数据库中创建了集合，这个数据库才真正存在
//
// //
// db.CreateCollecion('sub',{capped:true,size:10})// sub集合有大小，最大只能存10个字节
// // 如果字节溢出，则会覆盖之前的字节，容量集合不常用
//
// // 查看当前数据库中存在的集合
// show collections
//
// // 删除集合
// db.集合名称.drop()
// db.sub.drop()



