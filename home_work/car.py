class Car:
    def __init__(self,color ,type ,year):
        self.color=color
        self.type=type
        self.year=year

    def start(self):
        print('Автомобиль заведен!')
    def disable(self):
        print('Автомобиль заглушен!')
    def year_of_issue(self,year_new):
        self.year_new=year_new

    def type_1(self,type_new):
        self.type_new=type_new

    def color_1(self, color_new):
        self.color_new=color_new


