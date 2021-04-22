# import bs4
from bs4 import BeautifulSoup
from urllib import request

name_list = ['조회순', '평점순(현재상영영화)', '평점순(모든영화)']
code_list = ['cnt', 'cur', 'pnt']
for index in range(len(code_list)):
    con = request.urlopen('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel='+code_list[index]+'&date=20210128') #연결부품 획득

    name = name_list[index]
    doc = BeautifulSoup(con, 'html.parser')

    td_title = doc.select('td.title')
    td_point = doc.select('td.point')

    print('순위배정기준:',name)

    if code_list[index] == 'cnt':
        for rank in range(len(td_title)):
            tit = td_title[rank].text
            print('순위', rank+1, ":" , tit.strip())
    elif code_list[index] in ['cur' , 'pnt']:
        for rank in range(len(td_point)):
            tit = td_title[rank].text
            tp = td_point[rank].text
            print('순위',rank+1,'평점)',tp,":",tit.strip())
    else :
        break

    print('-------------------------')