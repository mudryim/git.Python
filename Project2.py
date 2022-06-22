#NoteBook of your car
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
    fix = input('ТО, ремонт: ')
    cost = int(input('Сумма грн.:'))
    info2[fix] = cost
    cos_list.append(cost)
    respond = input('Завершть запись? (press "q")')
    if respond == "q":
        active = False
# showing results
print("===RESULTS===")
for dat, km  in info.items():
    print(f"\tДата: {dat}, Пробег: {km}")
for fix, cost in info2.items():
    print(f"\nТО, Ремонт: {fix}\nСумма: {cost}")

input('')