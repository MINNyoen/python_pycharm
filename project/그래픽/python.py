from tkinter import *
def click(Return):
    entered_text = entry.get()
    output.delete(0.0,END)
    try:
        definition = my_glossary[entered_text]
    except:
        definition = " 단어의 정의를 찾을 수 없습니다."
    output.insert(END,definition)
window=Tk()
window.title("My Coding Club Glossary")
Label(window, text = '정의되어 있는 단어를 입력하고 엔터 키를 누르세요:').grid(row=0,column=0,sticky=W)
entry = Entry(window, width=20, bg='pink')
entry.grid(row =1, column=0, sticky=W)
Button(window, text='제출',width=5,command=click).grid(row=2,column=0,sticky=W)
Label(window,text='\n정의:').grid(row=3, column=0, sticky=W)
output=Text(window, width=75, height=100, wrap=WORD,background='pink')
output.grid(row=4, column=0, columnspan=2, sticky=W)
my_glossary={
    '알고리즘' : '컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것',
    '인수': '작업을 수행할 수 있는 함수에 의해 요구되는 정보의 조각. 보통 문자 또는 숫자가 사용됨',
    '2진수':'2진법으로 나타낸 숫자',
    '변수':'컴퓨터 메모리에 저장되어 있는 값을 참조하기 위해 사용하는 이름',
    '위젯' : '버튼 또는 텍스트 엔트리 박스 등을 가르키는 GUI 요소',
    }
window.bind('<Return>',click)
window.mainloop()