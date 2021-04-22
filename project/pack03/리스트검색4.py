food_list = ['김치찌개','된장찌개','제육볶음','불고기볶음']
print(food_list[-3:-1])
last_food = food_list[-1]
print(food_list.count('김치찌개'))

soup = 0
meat = 0

for x in food_list:
    if '찌개' in x:
        soup = soup + 1
    elif '볶음' in x:
        meat = meat + 1
print('찌개 메뉴 개수', soup)
print('볶음 메뉴 개수', meat)