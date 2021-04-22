my_list = '나는 열심히 살자가 인생의 목표예요.!'

print(my_list[0]) #인덱스 0글자 한개

print(my_list[0:2]) #인덱스 0~1번까지 글자들을 추출

#단어를 분리해내보자.
my_list_list = my_list.split(sep=' ') #string의 리스트
print(my_list_list[0])
print(my_list_list[1])

# 1. 주민번호
social_no = '961105-2149016'
year = int(social_no[0:2]) #string => int
age = 2021 - (1900 + year)
print(age)

sexual = int(social_no[7])
if sexual == 1 or sexual == 3 :
    print('men')
else:
    print('women')