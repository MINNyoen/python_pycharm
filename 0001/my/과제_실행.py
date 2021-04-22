import 과제 as db

datas = ()
id = input("아이디를 입력하세요")
title = input("제목을 입력하세요")
contents = input("내용을 입력하세요")
writer = input("글쓴이를 입력하세요")

data=(id, title, contents, writer)

db.insert(data)
db.read(id)
db.all()



