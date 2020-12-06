class Worker:
    
    def __init__(self, name, surname, position, wage, bonus):
        self._income = {
            'wage':wage,
            'bonus':bonus
        }
        self.name = name
        self.surname = surname
        self.position = position
        
        
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        fullName = self.name + ' ' + self.surname + ' ' + self.position
        return fullName
    def get_total_income(self):
        fullIncome = self._income['wage'] + self._income['bonus']
        return fullIncome

a = Position ("Виктор", "Иванов", "инженер", 50000, 30000 )
print(a.get_full_name ())
print(a.get_total_income ())
b = Position ("Дмитрий", "Петров", "олигарх", 10000, 500000 )
print(b.get_full_name ())
print(b.get_total_income ())
