from tkinter import *
#import tkinter은 일일이 써줘야함.

#버튼을 눌렀을 때 로그인 기능을 처리해야함.
#특정한 기능은 하나의 함수로 만들어 주면 됨.
#버튼 눌렀을 때 처리하고자 하는 기능하나는 함수 하나가 됨.
#함수를 만드는 것을 함수를 정의한다라고 함.
#기능을 프로그래머가 정의하기 때문에 함수를 정의한다라고 표현함.
def login():
    #id입력한 값, pw입력한 값 가지고 와야함.
    #원래 회원가입할 때의 id/pw와 입력한 값을 비교해야함.
    # public void login() java용어.
    id1 = ID_entry.get()
    pw1 = pw_entry.get()

    print('입력한 ID는', id1, '입력한 패스워드는', pw1)

    if id1 == 'root' and pw1 == '1234':
        messagebox.showinfo('로그인 성공','축하합니다')
        print('True')
    else :
        messagebox.showinfo('로그인 실패', '다시 시도해 주세요')
        print('Error')

w = Tk()
w.geometry('500x250')

id = Label(w, text='ID 입력', font = ('궁서', 30)) # 글자 입력
id.pack() # 올리는거

ID_entry = Entry(w, font = ('궁서', 30), bg='red', fg='white') # 입력칸 만들기
ID_entry.pack()

pw = Label(w, text='PW 입력', font = ('궁서', 30))
pw.pack() # 올리는거

pw_entry = Entry(w, font = ('궁서', 30), bg='red', fg='white')
pw_entry.pack()

b = Button(w, text='로그인 처리', font = ('궁서', 30), bg='yellow', fg='white', command=login) #클릭버튼
b.pack()

w.mainloop()

# User Interface(UI)
# -GUI : 사용자가 그래픽 화면(윈도우 아이콘, 파이썬 tkinter)을 클릭/입력해서 사용/실행
# - command line interface(CLI) : 사용자가 명령어를 쳐서 프로그램을 사용 / 실행