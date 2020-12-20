from random import randint

class card:
    def __init__(self):
        self.numbers = 15
        self.card = []
        while len(self.card) < 15:
            x = randint(1,90)
            if not (x in self.card):
                self.card.append(x)
        self.card.sort()

    def __str__(self):
        row1 = []
        row2 = []
        row3 = []
        for i in range(len(self.card)):
            if i % 3 == 0:
                row1.append(self.card[i])
            elif i % 2 == 0:
                row2.append(self.card[i])
            else:
                row3.append(self.card[i])
        self.__addSpaces(row1)
        self.__addSpaces(row2)
        self.__addSpaces(row3)
        string = ''
        string += '|'.join(row1) + '\n'
        string += '|'.join(row2) + '\n'
        string += '|'.join(row3)
        return string

    def __addSpaces(self, row):
        for i in range(len(row)):
            if type(1) == type(row[i]) and row[i] < 10:
                row[i] = ' ' + str(row[i])
            else:
                row[i] = str(row[i])
        for i in range(4):
            x = randint(1,len(row)-1)
            row.insert(x,'  ')

    def defeat(self, barrel):
        if barrel in self.card:
            i = self.card.index(barrel)
            self.card[i] = '--'
            self.numbers -= 1
            return True
        else:
            return False

    def cont(self, barrel):
        if barrel in self.card:
            return False
        else:
            return True

    def isOver(self):
        if self.numbers == 0:
            return True
        else:
            return False
        

        
