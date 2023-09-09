class Car:
    def __init__(self,color ,type ,year):
        self.color=color
        self.type=type
        self.year=year

    def start(self):
        print('Автомобиль заведен!')
    def disable(self):
        print('Автомобиль заглушен!')
    def year_of_issue(self):
        print(self.year)
    def type_1(self):
        print(self.type)
    def color_1(self):
        print(self.color)

car_start=Car(color='синий автомобиль',type='сидан',year=2023)
car_start.start()

car_disable=Car(color='синий автомобиль',type='сидан',year=2023)
car_disable.disable()

car_year_of_issue=Car(color='синий автомобиль',type='сидан',year=2023)
car_year_of_issue.year_of_issue()

car_type=Car(color='синий автомобиль',type='сидан',year=2023)
car_type.type_1()

car_color=Car(color='синий автомобиль',type='сидан',year=2023)
car_color.color_1()