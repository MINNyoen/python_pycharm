from tkinter import *

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

b = Button(w, text='로그인 처리', font = ('궁서', 30), bg='yellow', fg='white') #클릭버튼
b.pack()

w.mainloop()