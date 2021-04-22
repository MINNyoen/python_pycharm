from 사람모듈 import *

class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("공부해라")





class Worker(Person):

    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company

    def work(self):
        print("일해라")



if __name__ == '__main__':
    student1 = Student('김',13)
    print(student1)
    student1.study()

    worker1 = Worker('김박',20,'sam')
    print(worker1)
    worker1.work()