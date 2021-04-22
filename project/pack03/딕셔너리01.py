me = {'이름':'min', '나이': 27, 'height':190} # 딕셔너리(사전), {키:값}
you = {'이름':'jin', '나이': 27, 'height':170}
print(me['이름'])
print(you['나이'])
me['나이'] = me['나이'] + 1
print(me)

he = dict()
he['이름'] = 'kim'
he['나이'] = 27
he['height'] = 180
he['weight'] = 100.5
print(he)

del he['height']
print(he)
print(len(he))

print(he.keys())

for x in he:
    print(x)
    print(x, he[x]) # []를 포함해야 값

# 문제
#1번
place = {'좋아하는 장소':'집','싫어하는 장소':'밖','내가 가보고 싶은 장소':'유럽'}

print(place['좋아하는 장소'])
place['내가 가보고 싶은 장소'] = '신촌'
print(place.keys())

#2번
words = {'the':'그','that':'그것 or 저것','this':'이것','it':'저것','ok':'화긴'}

while True:
    question = input('궁금한 영어단어를 적어주세요(the, that, this, it, ok), 종료시 x  ')
    if question == 'x':
        print('종료되었습니다.')
        break
    else :
        anwser = words[question]
        print(anwser)

print(words)

#3번
all_grades = {'1학기':100,'2학기':50,'3학기':88,'4학기':99}
print('2학기 성적은', all_grades['2학기'], '입니다')
for x in all_grades:
    if all_grades[x] >= 85:
        print('85점이 넘는 학기의 점수는 각', x, all_grades[x])