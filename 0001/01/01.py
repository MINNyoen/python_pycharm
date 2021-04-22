num1 = int(input("숫자 1 입력"))
num2 = int(input("숫자 2 입력"))
print("더하기는 : " + str(num1 + num2))
print("빼기는 : " + str(num1 - num2))
print("곱하기는 : " + str(num1 * num2))
print("나누기는 : " + str(num1 / num2))
print("몫 : " + str(num1 // num2))


peo1 = input("사람 입력")
peo2 = int(input("나이 입력"))
print(str(peo1) + "은 " +str(peo2) + "세 입니다.")
if(peo2 > 100):
    (print("나이가 많으시군요."))

else:
    print("나이가 적으시군요")


hobby = "달리기"
time = 10
print(hobby + "를 " + str(time) + "시간 했습니다.")
if(hobby == "달리기" and time > 10):
    print("오늘 달리기는 충분합니다.")
elif(hobby == "달리기" or time < 10):
    print("어떠한 운동이든 시작하세요!!")
else:
    print("입력 없음?")


