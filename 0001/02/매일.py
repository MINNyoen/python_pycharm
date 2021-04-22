class everyday:
    study = ''
    time = ''
    location = ''
    def __init__(self,study, time, location):
        self.study = study
        self.time = time
        self.location = location

    def study1(self):
        return self.study + '공부를' + self.time + '시간 동안 하다.'


    def where(self):
        return self.location + '에서' + self.study + '공부를 하다.'

    def __str__(self):
        return self.study, '공부를', self.time, '시간 동안 하다.'

if __name__ == '__main__':
    Day = everyday('파이썬','10','강남')
    Day1 = everyday('자바','11','신촌')
    Day2 = everyday('파이썬','12','종로')
    print(Day.study1())
    print(Day2.where())