food = ['아이스크림','아이스아메리카노','콜라'] #목록(list)
# hobby = []
print(food[0]) # 리스트 중 1번째
print(food[1]) # 리스트 중 2번째
print(food[2]) # 리스트 중 3번째

for i in range(0, 3): # i라는 변수를 설정한다 0~2까지 (3번 반복)
    print(food[i], end=' ') # 윗줄에서 정한 변수를 food리스트에서  띄어쓰기와 함께 송출한다.
print() #줄 나눔

for x in food: #for - each구문 # x라는 변수를 설정한다 food리스트에서 (food 데이터 양만큼 반복)
    print(x, end=' ') # 윗줄에서 정한 x값 송출
print() #줄 나눔
#########################################
# 오늘 끝나고 나서, 할 일 5가지를 목록으로 만들어보세요.
# 2가지 방식으로 프린트!

work = ['데이트', '전화', '예약', '식사', '잠']

for q in work:
    print(q, end=' ')
print() #줄 나눔

for w in range(0, 5):
    print(work[w], end=' ')
print() #줄 나눔
print('목록의 개수는 ', len(work))