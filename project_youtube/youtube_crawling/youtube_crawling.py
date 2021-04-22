import pandas as pd # 데이터를 처리하기 위한 가장 기본적인 패키지
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.webdriver.chrome.options import Options
import datetime as dt
import pyperclip
import openpyxl

# 1. Workbook 생성
from selenium.webdriver.support.wait import WebDriverWait

wb = openpyxl.Workbook()
# 2. Sheet 활성
sheet = wb.active
# 3. 데이터프레임 내 header(변수명)생성
sheet.append(["비디오 id", "이미지", "제목", "카테고리", "날짜"])

url = 'https://www.youtube.com'
driver = webdriver.Chrome('../driver/chromedriver.exe')
driver.implicitly_wait(5) #묵시적 대기 창 동적인페이지는 상관없지만
driver.maximize_window() #창안에서 안보이면 오류..

# 웹 페이지 가져오기
driver.get(url)

driver.find_elements_by_xpath('//*[@id="search"]')[0].click() #검색창영역클릭
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys('tottenham')#검색창 영역에 원하는 youtuber입력
driver.find_elements_by_xpath('//*[@id="search"]')[0].send_keys(Keys.RETURN)#엔터

driver.find_elements_by_xpath('//*[@id="avatar-section"]/a')[0].click() #개인 유튜브 홈페이지
driver.find_elements_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div')[0].click() #동영상 클릭

body = driver.find_element_by_tag_name('body')#스크롤하기 위해 소스 추출

num_pagedowns = 10
#10번 밑으로 내리는 것
while num_pagedowns:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    num_pagedowns -= 1

html0 = driver.page_source
html = BeautifulSoup(html0,'html.parser')

video_list0 = html.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})
url = 'https://www.youtube.com/'
# len(video_list0)
for i in range(50):
    per_url = url + video_list0[i].find('a',{'id':'thumbnail'})['href'] #개인 유튜브 url
    per_url1 = per_url[33:]
    name = video_list0[i].find('a', {'id': 'video-title'}).text #동영상 제목
    thumm = video_list0[i].find('img', {'id': 'img'}).get('src') #동영상 썸네일

    #개인 유튜브 페이지 접속
    driver.get(per_url)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_all_elements_located)

    time.sleep(6)
    html2 = driver.page_source
    html3 = BeautifulSoup(html2,'html.parser')

    # 동영상 게시 날짜
    date = html3.find('div', {'id': 'date'}).text[1:12]

    # sheet 내 각 행에 데이터 추가
    sheet.append([per_url1, thumm, name, "baseball", date])
    print(per_url1, thumm, name, "football", date)
wb.save("youtube_tv.xlsx")

# 개인 동영상 url
#driver.find_elements_by_xpath("//*[@id='top-level-buttons']/ytd-button-renderer[1]/a")[0].click()
#driver.find_elements_by_xpath("//*[@id='target']/yt-icon")[0].click()
#copy = driver.find_elements_by_xpath("//*[@id='textarea']")[0]
#copy.click()
#copy.send_keys(Keys.CONTROL + 'c')
#per_video = pyperclip.paste()
# print(per_video)


