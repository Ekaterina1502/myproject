import card, pocket

playerCard = card.card()
computerCard = card.card()

myPocket = pocket.pocket()

print(playerCard)
print()
print(computerCard)

isStupid = False

while not playerCard.isOver() and not computerCard.isOver():

    
    playerCard.numbers = 0
    print(playerCard.isOver())

    print()
    barrel = myPocket.getBarrel()
    print('Выбран бочонок с номером', barrel)

    answer = input('Вычеркиваем (y/n)?')
    if answer.lower() == 'y':
        if not playerCard.defeat(barrel):
            print('Вы проиграли, надо было продолжить')
            isStupid = True
            break
    else:
        if not playerCard.cont(barrel):
            print('Вы проиграли, надо было вычеркнуть')
            isStupid = True
            break

    if barrel in computerCard.card:
        computerCard.defeat(barrel)
    else:
        computerCard.cont(barrel)

    print(playerCard)
    print()
    print(computerCard)

if not isStupid:
    if playerCard.numbers == computerCard.numbers:
        print('Ничья')
    elif playerCard.numbers < computerCard.numbers:
        print('Вы выиграли')
    else:
        print('Победила машина')
