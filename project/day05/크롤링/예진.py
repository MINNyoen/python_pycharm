from bs4 import BeautifulSoup
from urllib import request

code_list = ['8809325063156', '8809064223279', '8809064223415', '0075597918830']
name_list = ['MI MANG(미망)', 'CRYING NUT(크라잉넛)', '한영애', 'BLACK KEYS']

for index in range(len(code_list)) :
    con = request.urlopen('http://www.hottracks.co.kr/ht/record/detail/'+ code_list[index])

    doc = BeautifulSoup(con, 'html.parser')

    artist = doc.select('div h2.tit')
    # print(artist)

    ori_price = doc.select('span.ori_price')
    # print(ori_price)

    price = doc.select('div.price strong')
    # print(price)

    point = doc.select('span.w100')
    # print(len(point))
    # print(point[0])

    artist = artist[0].text
    ori_price = ori_price[0].text
    price = price[0].text
    point = point[0].text

    print('아티스트 : ', artist.strip())
    art2 = artist.strip().split(sep='-') #리스트['왼쪽단어','오른쪽단어']
    print(art2[0])
    print(art2[1].strip())
    art3 = art2[0] + '- ' + art2[1].strip()
    print(art3)

    file = open(name_list[index] + '.txt', 'w')
    file.write(art3 + '\n')
    file.write(ori_price + '\n')
    file.write(price + '\n')
    file.write(point + '\n')
    file.close()




    print('원가 : ', ori_price)
    print('판매가 : ', price)
    print('포인트 : ', point)
    print('-----------')