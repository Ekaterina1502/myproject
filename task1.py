class Matrix:

    def __init__(self,data):
        self.data = data

    def __str__(self):
        string = ''
        for row in self.data:
            for column in row:
                string += str(column) + ' '
            string += '\n'
        return string

    def __add__(self,other):
        data = []
        i = 0
        j = 0
        for row in self.data:
            print(row)
            newRow = []
            for column in row:
                newRow.append(column + other.data[i][j])
                j += 1
            j = 0
            i += 1
            data.append(newRow)   
        return Matrix(data)
        
        
x = Matrix([[1,2],[3,4]])
y = Matrix([[1,2],[3,4]])
print(x+y)
