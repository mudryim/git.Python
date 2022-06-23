#NoteBook of your car
import math
#Start
print("Хай! Давай запишем историю твоей ласточки")
info = {}
info2 = {}
cos_list = []
#user input values of date and km
active = True
dat = input('Введите текущую дату: ')
km = input('Введите пробег: ')
info[dat] = km
#user input values of fixing car
while active:
    #Repeat noting
    fix = input('ТО, ремонт: ')
    cost = int(input('Сумма грн.:'))
    cos_list.append(cost)
    info2[fix] = cost
    respond = input('Завершть запись? (press "q")')
    #Interrupt note
    if respond == "q":
        active = False
# showing results
print("===RESULTS===")
for dat, km  in info.items():
    print(f"\tДата: {dat}, Пробег: {km}")
for fix, cost in info2.items():
    print(f"\nТО, Ремонт: {fix}\nСумма: {cost}")
#Total sum
print("Общая сумма: ", sum(cos_list))

input('')