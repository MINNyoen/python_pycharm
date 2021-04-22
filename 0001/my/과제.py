import pymysql #alt+Enter
#DAO역할 모듈: CRUD(DML)

#정형데이터 => mysql, oracle, sqlite3(관계형 데이터베이스 관리 시스템, RDBMS)
def insert(datas):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'insert into board values (%s, %s, %s, %s)'
    result = cur.executemany(sql, datas)
    print('처리 결과', result, '개')

    con.commit()
    con.close()

def read(id):
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = "select * from board where id ='" + id + "'"
    cur.execute(sql)

    # row = cur.fetchone()
    rows = cur.fetchall() # 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    print(type(rows))
    # print(rows[0])
    for row in rows:
        print(row)

    con.close()

def all():
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor(pymysql.cursors.DictCursor)
    print(cur)

    sql = "select * from board "
    cur.execute(sql)

    # row = cur.fetchone()
    rows = cur.fetchall() # 조건에 맞는 목록을 모두 가지고 온다.
    # cur.fetchmany(개수) : 조건에 맞는 목록을 개수만큼 가지고 온다.
    print(rows)
    print(type(rows))
    # print(rows[0])
    for row in rows:
        print(row)

    con.close()

def update(id, title, contents, writer):
    #1. mysql과 연결
    con = pymysql.connect(host='localhost', port=3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    #2. 스트림안의 데이터를 다룰 수 있는 부품인 cursor를 획득!
    cur = con.cursor()
    print(cur)

    #3. sql문을 만들어서 전송함.
    data = (writer, title, contents, id)
    sql = "update board set writer = %s, title = %s, contents = %s where id = %s"
    cur.execute(sql, data) #tuple로 넣어주어야 한다.

    #4. auto-commit이 안된다. 수동으로 반영시켜야 한다.
    con.commit()
    con.close()

def delete(id):
    con = pymysql.connect(host = 'localhost', port= 3306, db='shop', user='root', password='1234')
    print(con.get_host_info())

    cur = con.cursor()
    print(cur)

    sql = 'delete from board where id = "' + id + '"'
    result = cur.execute(sql)
    print(result)

    con.commit()
    con.close()

