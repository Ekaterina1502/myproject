import json
import functools

with open("для задания 7.txt") as file:
    comp = {}
    for line in file:    
        lineList = line.split()
        comp[lineList[0]] = int(lineList[2]) - int(lineList[3])
    avarageProfit = functools.reduce(lambda x,y: x+y, [comp[name] for name in comp])/len(comp)
    data = [comp,{'avarageProfit': avarageProfit}]
    print(data)
    with open("для задания 7 - новый.txt", "w") as new_file:
       new_file.write(json.dumps(data))
