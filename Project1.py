# Калькулятор (вычисление среднего расхода топлива)
from colorama import init
from colorama import Fore, Back, Style
init()

print("Sup! Let's find out your . ")
sList = []

active = True
while active:
# User put metions of fuel and distance 
    l = int(input('Put the fuel volume (l): '))
    d = int(input('Put the distance (km): '))
    result = l * 100 / d
    sList.append(result)
#output of data
    if result <= 8:
        print(f'{Back.GREEN}{result} - you have economic expense!' )
    elif result > 8 and result <= 12:
        print(f'{Back.YELLOW}{Fore.BLACK}{result} - you have a normal expense.')
    else:
        print(f'{Back.RED}{result} - this is huge expense...')
#ending of circle
    respond = input('Continue? (yes/no)')
    if respond == 'no':
        active = False
#showing list result
print("===RESULTS===")
for i in sList:
    print(i)


