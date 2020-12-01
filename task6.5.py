class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print ("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Ручка')

class Pensil(Stationery):
    def draw(self):
        super().draw()
        print('Карандаш')

class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Маркер')

a = Pen('Шариковая ручка')
a.draw()

b = Pensil ('Простой карандаш')
b.draw()

c = Handle('Зеленый маркер')
c.draw()
