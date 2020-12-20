my_file = open ("для задания3.txt", "r")
summ=0
for line in my_file:
    words = line.split()
    summ += float(words[1])
    if float(words[1]) < 20000:
        print (f'У сотрудника {words[0]} - зп менее 20 тысяч')
my_file.seek(0)
print(f'Средняя зарплата в компании - {summ/len(my_file.readlines())}')
my_file.close()
        
