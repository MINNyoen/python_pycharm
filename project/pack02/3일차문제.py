# 1번 문제
ID = input('아이디는 무엇입니까? ')
name = input('이름은 무엇입니까? ')

if ID == 'root' and name == '홍길동':
    print('아이디가 ',ID,'인',name,'님이 로그인되었습니다.')
else:
    print('아이디가 ',ID,'인',name,'님이 로그인되지 못했습니다.')

print('----------------------------------------------')
# 2번 문제
n1 = int(input('첫번째 숫자는? '))
n2 = int(input('두번째 숫자는? '))
print('---------------------')
print('두 수의 합은', n1 + n2)
print('두 수의 차는', n1 - n2)
print('두 수의 곱은', n1 * n2)
print('두 수의 나눗셈은', n1 / n2)
print('나누고나서의 나머지는', n1 % n2)

print('----------------------------------------------')
# 3번 문제
age = int(input('나이는 몇살 입니까? '))
name = input('이름은 무엇입니까? ')
print(name,'님의 10년 후의 나이는', age + 10,'세입니다.')

print('----------------------------------------------')
# 4번 문제
money = int(input('엄마 용돈 주세요! '))

if money >= 10000:
    print('엄마 너무 용돈이 많아요')
else :
    print('엄마 너무 용돈이 적어요')

print('----------------------------------------------')
# 5번 문제
num = int(input('숫자를 입력하세요.'))

if num % 2 == 0 :
    print('짝수입니다.')
else :
    print('홀수입니다.')

print('----------------------------------------------')
# 6번 문제
hope = int(input('실적을 입력하세요.'))

if hope >= 1000:
    print('축하합니다. 실적을달성하셨습니다!')
    print('당신의 이번달 보너스는', int(hope * 0.2), '만원 입니다')
else:
    print('아쉽습니다. 다음엔 더 노력하세요.')

print('----------------------------------------------')
# 7번 문제
name_roket = input('미사일의 이름은?')
start_roket = int(input('미사일 시작값은?'))
move_roket = int(input('미사일 움직이는 값은? '))
print('----------------------')
print(name_roket,'미사일이',start_roket - move_roket,'로 이동되었습니다.' )

print('----------------------------------------------')
# 8번 문제
give_money = int(input('받은 돈?'))
all_cost = int(input('상품의 총액?'))

print('받은 돈 :', give_money )
print('상품의 총액 :', all_cost )
print('부가세 :', all_cost/10  )
print('잔돈 :', give_money - all_cost )

print('----------------------------------------------')
# 9번 문제
s = '*'
for _ in range(0,1000):
    print(s)


print('---------------------------------------------')
# 문제 10번
number1 = 0
number2 = 0
number_list = []

while number1 <= 20:
    print(number1)
    number1 = number1 + 1

for _ in range(0, 20):
    number2 = number2 + 1
    number_list.append(number2)
print(number_list)


print('---------------------------------------------')
# 문제 11번
zero = 0
while zero <= 50:
    if zero % 2 == 0:
        print(zero)
    else:
        print()
    zero = zero + 1

print('---------------------------------------------')
# 문제 12번
list = []
zero = 0
while zero <= 1000:
    if zero % 3 == 0:
        list.append(zero)
    zero = zero + 1
print('3의 배수의 개수는', len(list),'개')

print('---------------------------------------------')
# 문제 13번
a = input('먹고싶은 음식은? ')
while a != 'x' :
    a = input('먹고싶은 음식은? ')
print('종료합니다.')

print('---------------------------------------------')
# 문제 14번
food = ['치킨', '피자', '떡볶이', '해산물', '삼겹살']
print(food)
print(food[0],food[4])
print(food[2])
for w in range(2,4):
    print(food[w], end=' ')
print(food[2])
print(food[2:4])



print('---------------------------------------------')
# 문제 15번
page = []
page.append('네이버')
page.append('카카오')
page.append('다음')
page.append('링크드인')
print(page)

print('---------------------------------------------')
# 문제 16번
clsss = []
first = int(input('1학기 총점? '))
clsss.append(first)
second= int(input('2학기 총점? '))
clsss.append(second)
third = int(input('3학기 총점? '))
clsss.append(third)

print(('총 학기 평균은',clsss[0] + clsss[1] + clsss[2] / 3,'입니다'))

print('---------------------------------------------')
# 문제 17번
a = int(input('당신이 생각한 정답 입력 :'))
count = 0
if a == 77:
    print('정답입니다.')
else:
  while a != 77:
    count = count + 1
    if a >77 :
          print('77보다 큽니다.')
          print('시도횟수',count)
    else:
          print('77보다 작습니다.')
          print('시도횟수',count)
    print('정답이 아닙니다.')
    a = int(input('당신이 생각한 정답 입력:'))
    if a == 77:
      print('정답입니다.')
      print('시도횟수',count)

print('---------------------------------------------')
# 문제 18번
mon = int(input('입금액 :'))
plus =float(input('이자율 :'))

print('1년 후 받게 될 금액은 : ', int(mon *(1 + plus)),'won')

print('---------------------------------------------')
# 문제 20번
location = []
one = input('내가 가장 좋아하는 장소?')
location.append(first)
two= input('내가 가장 좋아하는 장소?')
location.append(second)
three = input('내가 가장 좋아하는 장소?')
location.append(third)
four = input('내가 가장 좋아하는 장소?')
location.append(four)
five = input('내가 가장 좋아하는 장소?')
location.append(five)
print('------------------')
print(location)
location.remove('강남')
print(location)
location[4] = '제주시'
print(location)

#문제 20번 - 2
Location = []
for k in range(0,5):
    k = input('내가 가장 좋아하는 장소는? ')
    Location.append(k)
print('------------------')
print(Location)
Location.remove('강남')
print(Location)
Location[3] = '제주시'
print(Location)

for index in range(len(Location)):
    print(index + 1, '위:', location[index])

#부족한 부분 break, list에서 [2:]느낌 20번,16번 문제 for 활용

#
c1 = [22,99,11,23]
c2 = [44,99,24,55]
print(c1 + c2)
for p in range(len(c1)):
    if c1[p] == c2[p]:
        print(c1[p])


