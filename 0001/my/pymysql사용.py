from mysql연결 import *

id = input("아이디를 입력하세요")
pw = input("비밀번호를 입력하세요")
name = input("이름을 입력하세요")
tel = input("번호를 입력하세요")

my1 = mysql(id,pw,name,tel)
my1.delete()
