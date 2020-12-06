from abc import ABC, abstractmethod

class clothes(ABC):
    @abstractmethod
    def getFabricLoss(self):
        pass


class coat(clothes):
    def __init__(self, size):
        self.size = size

    @property
    def getFabricLoss(self):
        return self.size/6.5+0.5
        
        
class suit(clothes):
    def __init__(self, height):
        self.height = height

    @property    
    def getFabricLoss(self):
        return self.height*2 + 0.3

x = coat(5)
print(x.getFabricLoss)

