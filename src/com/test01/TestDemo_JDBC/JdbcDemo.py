#charset utf8

import pymysql

class JdbcDemo():

    def __init__(self):
        print ('init.....')

    def NormalTest(self):
        try:
            conn=pymysql.connect(host='127.0.0.1', port=3306 , user='root', passwd='root', db='test', charset='utf8')
            cur=conn.cursor()
            cur.execute('SELECT * FROM TE')
            data=cur.fetchall()
            for d in data:
                print("id:",d[0],"name",d[1])

        except Exception : print ('ERROR')

if __name__=="__main__":
    conn=JdbcDemo()
    conn.NormalTest()

