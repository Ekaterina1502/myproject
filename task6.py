import json
import functools

dictionary = {}

with open('для задания6.txt') as file:
    data = json.load(file) #десериализируем json
    for name in data: #перебираем ключи из data
        numList = [data[name][i] for i in data[name]] #получаем список колва занятий
        dictionary[name] =  functools.reduce(lambda x,y: x + y, numList) #находим сумму списка и помещаем в нвоый словарь

print(dictionary)
