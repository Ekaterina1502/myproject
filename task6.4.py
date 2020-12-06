class Car:
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
      
    def go (self):
        print ('Машина поехала')
    def stop (self):
       print ('Машина остановилась')
    def turn(self, direction):
        print (f'Машина повернула {direction}')
    def show_speed(self):
        print (f'Скорость автомобиля {self.speed}')

class Towncar(Car):
    def __init__(self, speed, name):
        super().__init__ (speed, 'grey', name, False)
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print (f'Вы превысили скорость на {self.speed-60} км/ч')
        
class SportCar(Car):
    def __init__(self, speed, name):
        super().__init__ (speed, 'red', name, False)
        
class WorkCar(Car):      
    def __init__(self, speed, name):
        super().__init__ (speed, 'black', name, False)
    def show_speed(self):
        super().show_speed()
        if self.speed >40:
            print (f'Вы превысили скорость на {self.speed-40} км/ч')
        
class PoliceCar(Car):  
    def __init__(self, speed, name):
        super().__init__ (speed, 'blue and white', name, True)

a = Towncar (45, 'toyota')
a.show_speed ()
print(a.name , a.color, a.is_police)

b = SportCar (120, 'Jaguar')
b.show_speed ()
print(b.name , b.color, b.is_police)

c = WorkCar (70, 'Mazda')
c.show_speed ()
print(c.name , c.color, c.is_police)

d = PoliceCar (65, 'Ford Focus')
d.show_speed ()
print(d.name , d.color, d.is_police)
