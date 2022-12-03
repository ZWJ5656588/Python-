# 通过pymysql连接Mysql服务端
# 变量的站位用%s来占位，不用f表达式

# 一些常用的函数
"""
close()
关闭连接后, 连接对象和它的游标均不可用
commit()
如果支持就提交挂起的事务, 否则不做任何事
rollback()
回滚挂起的事务(可能不可用)
cursor()
返回链接的游标对象

"""
# 名称
#
# 描述
#
# callproc(func[, args])
#
# 使用给定的名称和参数(可选)调用已命名的数据库程序
#
# close()
#
# 关闭游标后，游标不可用
#
# execute(op[, args])
#
# 执行 SQL 操作, 可能使用参数
#
# executemany(op, args)
#
# 对序列中的每个参数执行 SQL 操作
#
# fetchone()
#
# 把查询结果集中的下一行保存为序列 或 None
#
# fetchmany([size])
#
# 获取查询结果集的多行, 默认尺寸为 arraysize
#
# fetchall()
#
# 将所有 (剩余) 行作为结果序列
#
# nextset()
#
# 调至下一个可用的结果集 (可选)
#
# setinputsizes(sizes)
#
# 为参数预先定义内存区域
#
# setoutputsize(size[, col])
#
# 为获取大数据值设定缓冲区尺寸


import pymysql
import datetime
# 1. 数据库连接函数，连接到python_test数据库
def db_connect():
    # 创建数据库对象,不用写数据库端口，host默认localhost
    db=pymysql.connect(host='localhost',user='root',password='',db='python_test')

    # 使用数据库对象创建一个游标对象  (类似于子套接字)
    cursor=db.cursor()

    # 使用游标对象执行sql语句
    # 查询数据库版本
    cursor.execute('select version()')

    # 获取数据,使用fetchone() 获取单条数据
    data=cursor.fetchone()

    # 打印数据
    print(data)

    # 关闭数据库连接
    db.close()


db_connect()


# 2. 创建数据表
def db_connect2():
    # 创建数据库对象,不用写数据库端口，host默认localhost
    db=pymysql.connect(host='localhost',user='root',password='',db='python_test')

    # 使用数据库对象创建一个游标对象  (类似于子套接字)
    cursor=db.cursor()

    # 通过sql创建一个数据表
    cursor.execute('drop table if exists employee')

    # 组织创建表的sql语句
    sql="""
        create table employee(
        first_name varchar(20) not null ,
        last_name varchar(20),
        age tinyint,
        sex varchar(1),
        income int,
        create_time datetime
        );
        """

    # 执行sql语句，用try except 进行异常捕获
    try:
        cursor.execute(sql)
        print('执行成功...')
    except:
        print('执行失败')
    finally:
        db.close()


db_connect2()


# 3.数据库插入数据
def insert_record():
    db = pymysql.connect(host='localhost', user='root', password='', db='python_test')

    # 获取游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "insert into employee (first_name, last_name, age, sex, income, create_time) values 0 " \
          "('%s', '%s', %d, '%s', %d, '%s')" % ('小', '王', 22, '男', 30000, datetime.datetime.now())
    # 执行 SQL 语句
    try:
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('数据插入成功...')
    except Exception as e:
        print(f'数据插入失败: {e}')
        # 如果发生错误就回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


insert_record()




