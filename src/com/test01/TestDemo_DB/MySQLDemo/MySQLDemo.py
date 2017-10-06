# -*- coding:utf-8 -*-
# 导入MySQL驱动:
import pymysql

# 注意把password设为你的root口令:
conn=pymysql.connect(user='root',passwd='root',database='test')
cursor=conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
# cursor.execute('INSERT INTO te(id,name) VALUE (%s,%s)',['5','EE'])
# cursor.execute('UPDATE TE SET name=%s WHERE id=%s',['Ee','5'])
cursor.execute('SELECT * FROM te ')
values=cursor.fetchall()
for val in values:
    print(val)

# print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()