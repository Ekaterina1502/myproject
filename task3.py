class cell:
    def __init__(self, cellnum):
        self.cellnum = cellnum

    def __str__(self):
        return str(self.cellnum)

    def __add__(self, other):
        return cell(self.cellnum+other.cellnum)

    def __sub__(self, other):
        sub = self.cellnum-other.cellnum
        if sub < 0:
            print('Клеток не может быть отрицательное число')
        return cell(sub)

    def __mul__(self, other):
        return cell(self.cellnum*other.cellnum)

    def __truediv__(self, other):
        return cell(self.cellnum/other.cellnum)

    def make_order(self, cellInRow):
        a = ''
        for i in range(self.cellnum):
            if i % cellInRow ==0:
                a += '\n'
            a += '*'
        return a
            
        

x = cell(72)
print(x.make_order(10))
y = cell(7)
print(f'Объединение клеток {x + y}')
print(f'Вычитание клеток {x - y}')
print(f'Умножение клеток {x * y}')
print(f'Деление клеток {x / y}')

