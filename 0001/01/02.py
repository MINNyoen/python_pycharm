num = 0
plus = 1
for x in range(20):  # 0~4, 1씩증가
    print(x,end=" ")
print("-------------")

for num in range(1,101):
    print(x, end=" ")
print("-------------")

for x in range(0,201):
    print(x, end=' ')
print("-------------")

for x in range(1, 101, 2):
    print(x, end=" ")
print("-------------")

for x in range(100, 501, 5):
    print(x, end=" ")
print("-------------")

for x in range(100, 501, 5):
    num = num + x
    print(num, end=" ")
print(num)
print("-------------")

for x in range(3, 201, 8):
    plus = plus + x
    print(plus, end=" ")
print(plus)
print("-------------")

food = ['감자', '고구마', '양파']
for x in food:
    print(x + '짱!')
for x in food:
    print(x + '짱!', end = " ")

print("--------------------")
food1 = "감자,고구마,양파,스프,국수,라면"
food2 = food1.split(",")
for x in food2:
    if x != '양파' and x != '국수':
        print(x + '맛있어여!', end = " ")
        continue
