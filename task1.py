my_f = open("text.rft","w")

while True:
    my_var = input ('Введите что-нибудь')
    if my_var == '':
        break
    my_f.write(f'{my_var}\n')

my_f.close()
