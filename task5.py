import random
import functools

with open("файл задание5.txt", "w") as my_file:
    numbers = [str(random.randint(-100,100)) for i in range (10)]
    my_file.write(' '.join(numbers))

with open("файл задание5.txt", "r") as my_file:
    numbers = next(my_file).split()
    print(numbers)
    print(functools.reduce(lambda x,y: int(x)+int(y), numbers))
    
        
        
