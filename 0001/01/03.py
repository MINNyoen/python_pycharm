buy = []
wish = []

for x in range(5):
     buy1 = input(str(x+1) + " 번째 사고 싶은 것을 입력하세요")
     buy.append(buy1)
print(buy)

wish1 = input("입력 하세요.")
wish = wish1.split(",")

for x in range(len(wish)):
    print("나는" + wish[x] +"가 되고 싶어요!")
