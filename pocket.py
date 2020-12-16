from random import randint, shuffle

class pocket:
    def __init__(self):
        self.__pocket = [i for i in range(1,91)]
        shuffle(self.__pocket)

    def getBarrel(self):
        if len(self.__pocket) > 0:
            return self.__pocket.pop()

