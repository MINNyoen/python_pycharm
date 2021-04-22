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
    num1 = num_entry.get()
    sub1 = sub_entry.get()
    book1 = book_entry.get()
    name1 = name_entry.get()

    if num1 == '1' and sub1 == 'big' and book1 == 'data' or name1 == 'kim':
        messagebox.showinfo('성공하셨습니다.',
                            '입력하신 번호는', num1,
                            '입력하신 제목은', sub1,
                            '입력하신 내용은', book1,
                            '입력하신 이름은', name1)
        print('True')
    else :
        messagebox.showinfo('실패', '다시 시도해 주세요')
        print('Error')


w = Tk()
w.title("빅데이터 4일차 문제")
w.geometry('600x250')
qw = Label(w, text='  항목  ', bg='yellow green', font = ('돋움', 20),) # 글자 입력
qw.grid(row=1, column=0)

qe = Label(w, text='입력', bg='yellow green', font = ('돋움', 20)) # 글자 입력
qe.grid(row=1, column=1)

num = Label(w, text='  번호  ', bg='yellow green', font = ('돋움', 20)) # 글자 입력
num.grid(row=2, column=0) # 올리는거

num_entry = Entry(w, font = ('돋움', 20), bg='red', fg='white')
num_entry.grid(row=2, column=1)

sub = Label(w, text='제목', bg='yellow green', font = ('돋움', 20))
sub.grid(row=3, column=0)

sub_entry = Entry(w, font = ('돋움', 20), bg='red', fg='white')
sub_entry.grid(row=3, column=1)

book = Label(w, text='내용', bg='yellow green', font = ('돋움', 20))
book.grid(row=4, column=0)

book_entry = Entry(w, font = ('돋움', 20), bg='red', fg='white')
book_entry.grid(row=4, column=1)

name = Label(w, text='작성자', bg='yellow green', font = ('돋움', 20))
name.grid(row=5, column=0)

name_entry = Entry(w, font = ('돋움', 20), bg='red', fg='white')
name_entry.grid(row=5, column=1)

b = Button(w, text='글쓰기 완료', font = ('돋움', 20), bg='yellow', fg='green', command=login) #클릭버튼
b.grid(row=6,columnspan=2)

w.mainloop()

# User Interface(UI)
# -GUI : 사용자가 그래픽 화면(윈도우 아이콘, 파이썬 tkinter)을 클릭/입력해서 사용/실행
# - command line interface(CLI) : 사용자가 명령어를 쳐서 프로그램을 사용 / 실행