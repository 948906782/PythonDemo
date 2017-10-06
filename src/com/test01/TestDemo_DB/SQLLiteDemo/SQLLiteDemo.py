#-*- coding:utf-8 -*-
# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn=sqlite3.connect('test.db')
# 创建一个Cursor:
cursor=conn.cursor()
# 执行一条SQL语句，创建user表:
# cursor.execute('CREATE TABLE user (id varchar(32) primary key,name varchar(64))')
# 插入操作
# cursor.execute("INSERT INTO user VALUES ('004','DD')")
# print(cursor.rowcount)# 通过rowcount获得插入的行数:

# 更新操作
cursor.execute("UPDATE user SET name='CC' WHERE id='003'")
print(cursor.rowcount)

# 查询操作
# cursor.execute('SELECT * FROM user')
# values=cursor.fetchall()
# for val in values:
#     print(val)


# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
