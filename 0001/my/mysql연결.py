import pymysql

class mysql():

    def __init__(self, id, pw, name, tel):
        self.id = id
        self.pw = pw
        self.name = name
        self.tel = tel

    def creat(self):
        con = pymysql.connect(host= 'localhost', port= 3306, db='shop', user='root', password= '1234')
        print(con.get_proto_info())

        cur = con.cursor()
        print(cur)

        sql = 'insert into member values ("id","pw", "name", "tel")'
        result = cur.execute(sql)
        print(result)

        con.commit()
        con.close()

    def create2(datas):
        con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
        print(con.get_host_info())

        cur = con.cursor()
        print(cur)

        sql = 'insert into member values (%s, %s, %s, %s)'
        result = cur.executemany(sql, datas)
        print('처리 결과', result, '개')

        con.commit()
        con.close()

    def delete(self):
        con = pymysql.connect(host= 'localhost', port= 3306, db='shop', user='root', password= '1234')
        print(con.get_host_info())

        cur = con.cursor()
        print(cur)

        sql = 'delete from member where id = "' + str(self.id) + '"'
        result = cur.execute(sql)
        print(result)

        con.commit()
        con.close()

    def select(self):
        con = pymysql.connect(host= 'localhost', port= 3306, db='shop', user='root', password= '1234')
        print(con.get_host_info())

        cur = con.cursor()
        print(cur)

        sql = 'select * from member where id = "' + str(self.id) + '"'
        result = cur.execute(sql)
        cur.fe
        print(result)

        con.commit()
        con.close()
        return