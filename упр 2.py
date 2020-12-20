my_file = open ("для задания2.txt","r")
lines = 0

for line in my_file:
    lines+=1
    print(f' Количество слов в строке {lines}:{len(line.split())}')
print (f'Количество строк в файле - {lines}')
