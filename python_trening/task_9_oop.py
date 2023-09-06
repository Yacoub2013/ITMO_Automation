class Button:

    type: str = 'Кнопка'


    def __init__(self, text, link):

        self.text = text
        self.link = link



home = Button('Домой ','/home')
catalog_msk = Button('Каталог ', '/msk/catalog')

print(home.text)
print('Кнопка ' + home.text + 'имеет ссылку ' + home.link)
print(home.type)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + 'имеет ссылку ' + catalog_msk.link)

print(catalog_msk.type)

class BattonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Кнопка по локатору - {}".format(self.loc)

# Создаес экземпляры клааса, не внутри обьекта!!!!!

# в классе BattonTwo 3 переменные, соответсвенно мы их передаем сюда!!!! передаем их значение.

home_two = BattonTwo('Домой', '/home', 'button#home')

# Вызываем метод, метод click для экземпляр класса home_two

print(home_two.click())

