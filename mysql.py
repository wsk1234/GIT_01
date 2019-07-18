"""
pymysql 操作数据库基本流程演示
"""

import pymysql

# 链接数据库
db=pymysql.connect(host='localhost',port=3306,
                   user='root',password='123456',
                   database='stu',charset='utf8')

# 获取游标（操作数据库，执行sql语句）
cur=db.cursor()

# 执行sql语句
sql="insert into class_1 values" \
    "(7,'Lucy',18,'w',82,'2019-8-9');"
sql_1="insert into class_1 values" \
    "(8,'Hanm',19,'m',90.5,'2019-8-8');"
sql_2="insert into class_1 values" \
    "(9,'Lohan',18,'w',86.5,'2019-8-7');"

cur.execute(sql) # 执行语句
cur.execute(sql_1) # 执行语句
cur.execute(sql_2) # 执行语句

db.commit() # 将写操作提交，多次写操作一同提交

# 关闭数据库
cur.close()
db.close()

