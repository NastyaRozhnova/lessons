from random import randint
from lib import check_number

name = input('Как тебя зовут?\n')
max = check_number(input(f'{name}, до скольки мне загадать число?\n'))
print(f'Хорошо, {name}, я загадываю число от 1 до {max}')
attempts = check_number(input('Сколько у тебя будет попыток?\n'))

# Загадаем число
guess_number = randint(1, max)
counter = 0  # Счётчик попыток

while counter != attempts:
    counter += 1 # counter = counter+1
    answer=check_number(input(f'Попытка {counter}:\n'))

    if answer>guess_number: 
        print('Твоё число слишком большое')

    if answer<guess_number: 
        print('Твоё число слишком маленькое')

    if answer==guess_number: 
        print('Угадал')
        break 
else:
    print(f'Твои попытки закончились, я загадал число {guess_number}')

check_number()


