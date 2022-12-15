// 1.测试数据
db.getCollection("products").insert([ {
    _id: 100,
    sku: "abc123",
    description: "Single line description"
} ]);
db.getCollection("products").insert([ {
    _id: 101,
    sku: "abc789",
    description: "First line\nSecond line"
} ]);
db.getCollection("products").insert([ {
    _id: 102,
    sku: "xyz456",
    description: "Many spaces before    line"
} ]);
db.getCollection("products").insert([ {
    _id: 103,
    sku: "xyz789",
    description: "Multiple\nline description"
} ]);
db.getCollection("products").insert([ {
    _id: 104,
    sku: "abc123",
    description: "Single line description"
} ]);



db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba04fce0a56f10342b6f3"),
    name: "郭靖",
    hometown: "蒙古",
    age: 20,
    gender: true
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba07cce0a56f10342b6f4"),
    name: "黄蓉",
    hometown: "桃花岛",
    age: 18,
    gender: false
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba0acce0a56f10342b6f5"),
    name: "华筝",
    hometown: "蒙古",
    age: 18,
    gender: false
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba0d2ce0a56f10342b6f6"),
    name: "黄药师",
    hometown: "桃花岛",
    age: 40,
    gender: true
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba0f1ce0a56f10342b6f7"),
    name: "段誉",
    hometown: "大理",
    age: 16,
    gender: true
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba10bce0a56f10342b6f8"),
    name: "段王爷",
    hometown: "大理",
    age: 45,
    gender: true
} ]);
db.getCollection("stu_info").insert([ {
    _id: ObjectId("626ba12cce0a56f10342b6f9"),
    name: "洪七公",
    hometown: "华山",
    age: 18,
    gender: true
} ]);