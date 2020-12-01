import time

class TrafficLight:
    __color = 'red'

    def get_running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = 'yellow'
        print(self.__color)
        time.sleep(2)
        self.__color = 'green'
        print(self.__color)
        self.__color = 'red'

x = TrafficLight()
x.get_running()
x.get_running()
