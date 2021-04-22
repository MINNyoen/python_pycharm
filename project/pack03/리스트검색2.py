# a110 : a는 부서를 나타냄, 1: 직급, 10: 내 번호
# 부서가 a: 기획부, b: 개발부, c: 인사부
# 직급이 1: 사장, 2: 팀장, 3: 사원

#a110
for _ in range(0,3):
    code = input('본인의 사원번호를 입력하세요. ')
    job = code[0]
    clas = code[1]
    if job == 'a':
        print('기획부')
    elif job == 'b':
        print('개발부')
    elif job == 'c':
        print('인사부')
    else:
        print('잘못입력하셨습니다.')

    if clas == '1':
        print('사장님')
    elif clas == '2':
        print('팀장님')
    elif clas == '3':
        print('사원님')
    else:
        print('잘못입력하셨습니다.')
    print('당신의 번호는',code[2:4],'입니다')



