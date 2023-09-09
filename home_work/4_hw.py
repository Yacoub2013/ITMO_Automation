from ast import Str


class rectangle:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def square(self):
        print('Площадь прямоугольника равна:',self.x*self.y)

    def perimeter(self):
        print('Периметр прямоугольника равен:',(2*self.x) + (2*self.y))

print('Площадь и периметр первого прямоугольника:')
sguare_rectangle_1=rectangle(x=3,y=4)
sguare_rectangle_1.square()
perimeter_rectangle_1=rectangle(x=3,y=4)
perimeter_rectangle_1.perimeter()

print()
print('Площадь и периметр второго прямоугольника:')
sguare_rectangle_2=rectangle(x=4,y=9)
sguare_rectangle_2.square()
perimeter_rectangle_2=rectangle(x=4,y=9)
perimeter_rectangle_2.perimeter()

print()
print('Площадь и периметр третьего прямоугольника:')
sguare_rectangle_2=rectangle(x=7,y=11)
sguare_rectangle_2.square()
perimeter_rectangle_2=rectangle(x=7,y=11)
perimeter_rectangle_2.perimeter()

class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def addition(self):
        print('Сумма a+b=',self.a+self.b)
    def multiplication(self):
        print('Производение a*b=',self.a*self.b)

    def division(self):
        print('Диление a/b=',self.a/self.b)

    def subtraction(self):
        print('Разность a-b=',self.a-self.b)
print()
print('Результат сложения a и b:')
addition_Math=Math(a=10,b=2)
addition_Math.addition()

print('Результат произведение a на b:')
multiplication_Math=Math(a=10,b=2)
multiplication_Math.multiplication()

print('Результат диления a и b:')
division_Math=Math(a=10,b=2)
division_Math.division()

print('Результат разностия a и b:')
subtraction_Math=Math(a=10,b=2)
subtraction_Math.subtraction()
print()

class Demoqa:

    def __init__(self, text, loc=None ):
        self.text=text
        self.tipe='Кнопка'
        self.loc=loc


    def conditions(self):
        return 'Клик по кнопке - {}'.format(self.text)

print('Кнопка Text-Box')
text_box = Demoqa('Text-Box')
print(text_box.conditions())

print()
print('Кнопка Check-Box')
check_box = Demoqa('Check-Box')
print(check_box.conditions())

print()
print('Кнопка Radio-Button')
radio_button=Demoqa('Radio-Button')
print(radio_button.conditions())

print()
print('Кнопка Wep-Tables')
wep_tables=Demoqa('Wep-Tables')
print(wep_tables.conditions())


print()
print('Кнопка Buttons')
buttons=Demoqa('Buttons')
print(buttons.conditions())

print()
print('Кнопка Links')
links=Demoqa('Links')
print(links.conditions())

print()
print('Кнопка Broken Links - Images')
broken_links_images=Demoqa('Broken Links - Images')
print(broken_links_images.conditions())

print()
print('Кнопка Dynamic Propertais')
dynamic_propertais=Demoqa('Dynamic Propertais')
print(dynamic_propertais.conditions())

print()
print('Кнопка Practice Form')
practice_form=Demoqa('Practice Form')
print(practice_form.conditions())

print()
print('Кнопка Browser Windows')
browser_windows=Demoqa('Browser Windows')
print(browser_windows.conditions())

print()
print('Кнопка Alerts')
alerts=Demoqa('Alerts')
print(alerts.conditions())

print()
print('Кнопка Frames')
frames=Demoqa('Frames')
print(frames.conditions())

print()
print('Кнопка Nested Frames')
nested_frames=Demoqa('Nested Frames')
print(nested_frames.conditions())

print()
print('Кнопка Modal Dialogs')
modal_dialogs=Demoqa('Modal Dialogs')
print(modal_dialogs.conditions())

print()
print('Кнопка Acordian')
acordian=Demoqa('Acordian')
print(acordian.conditions())

print()
print('Кнопка Auto Complete')
auto_complete=Demoqa('Auto Complete')
print(auto_complete.conditions())

print()
print('Кнопка Date Picker')
date_picker=Demoqa('Date Picker')
print(date_picker.conditions())

print()
print('Кнопка Slider')
slider=Demoqa('Slider')
print(slider.conditions())

print()
print('Кнопка Progress Bar')
progress_bar=Demoqa('Progress Bar')
print(progress_bar.conditions())

print()
print('Кнопка Tabs')
tabs=Demoqa('Tabs')
print(tabs.conditions())

print()
print('Кнопка Tool Tips')
tool_tips=Demoqa('Tool Tips')
print(tool_tips.conditions())

print()
print('Кнопка Menu')
menu=Demoqa('Menu')
print(menu.conditions())

print()
print('Кнопка Select Menu')
select_menu=Demoqa('Select Menu')
print(select_menu.conditions())

print()
print('Кнопка Sortable')
sortable=Demoqa('Sortable')
print(sortable.conditions())

print()
print('Кнопка Selectable')
selectable=Demoqa('Selectable')
print(selectable.conditions())


print()
print('Кнопка Resizable')
resizable=Demoqa('Resizable')
print(resizable.conditions())

print()
print('Кнопка Droppable')
droppable=Demoqa('Droppable')
print(droppable.conditions())

print()
print('Кнопка Dragabble')
dragabble=Demoqa('Dragabble')
print(dragabble.conditions())


print()
print('Кнопка Login')
login=Demoqa('Login')
print(login.conditions())

print()
print('Кнопка Book Store')
book_store=Demoqa('Book Store')
print(book_store.conditions())

print()
print('Кнопка Profile')
profile=Demoqa('Profile')
print(profile.conditions())

print()
print('Кнопка Book Story API')
book_story_api=Demoqa('Book Story API')
print(book_story_api.conditions())

