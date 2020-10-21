from random import randint

name = input('Как тебя зовут?\n')
max = int(input(f'{name}, до скольки мне загадать число?\n'))
print(f'Хорошо, {name}, я загадываю число от 1 до {max}')
attempts = int(input('Сколько у тебя будет попыток?\n'))

# Загадаем число
guess_number = randint(1, max)
counter = 0  # Счётчик попыток

while counter != attempts:
    counter += 1 # counter = counter+1
    print(counter)

