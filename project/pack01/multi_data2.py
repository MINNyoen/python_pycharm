hobby = [] #hobby 정의
hobby.append('코딩') # hobby리스트에 '코딩' 추가
print('개수>> ', len(hobby)) # 개수>>와 hobby의 데이터 숫자를 송출
hobby.append('등산') # hobby리스트에 '등산' 추가
print('개수>> ', len(hobby)) # 개수>>와 hobby의 데이터 숫자를 송출

for _ in range(3): # 변수와는 관련없이 3번 반복한다.
    data = input('당신의 새로운 취미는? ') # data에 취미의 데이터를 넣는다.
    hobby.append(data) # hobby에 위에서 입력한 data를 추가한다.

print('개수>> ', len(hobby)) # 개수>>와 위에서 추가한 모든 hobby 데이터 숫자를 송출

for i in hobby: # hobby 데이터를 순차적으로 i로 변환 (hobby데이터 양만큼 반복)
    print(i) # 윗줄에서 정의한 i를 송출
