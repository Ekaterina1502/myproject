class Road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    def get_weight(self, kg, thickness):
        return self._length*self._width*kg*thickness
a = Road(10000,2)
print(a.get_weight(10, 2))

