class Soda:
    def __init__(self, dop=None):
        self.dop = dop

    def show_my_drink(self):
        if self.dop:
            print(f'Газировка и {self.dop}')
        else:
            print('Обычная гозировка')

metod_1 = Soda()
metod_2 = Soda('Малина')

metod_1.show_my_drink()
metod_2.show_my_drink()
