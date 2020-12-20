my_file = open ("для задания 4.txt", "r")
my_newFile = open("для задания 4 - новый.txt", "w")

my_dict = {
    'One': 'Адын',
    'Two': 'Дуа',
    'Three': 'Тры',
    'Four': 'Чэтырэ'
}

sep = ' - '

for line in my_file:
    elList = line.split(sep)
    rus = my_dict[elList[0]]
    newElList = [rus,elList[1]]
    my_newFile.write(sep.join(newElList))

my_file.close()
my_newFile.close()

    
    
