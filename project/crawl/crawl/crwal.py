from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://comic.naver.com/webtoon/weekday.nhn")

bsobject = BeautifulSoup(html, 'html.parser')

for link in bsobject.find_all('img'):
    print(link.text.strip(), link.get('src'))
