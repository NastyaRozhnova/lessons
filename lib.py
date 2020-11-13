def check_number(number: str) -> int:
    '''
    Проверка строки на число

    :param str number: проверяемая строка
    return int
    '''
    while not number.isdigit():  # '23'
        number = input('Должна быть цифра:\n')
    return int(number)


def check_input(answer: str, allowed: list) -> str:
    # сформируем сообщение пользователю
    message = 'Должно быть '      
    for element in allowed[:-1]: 
        message += f'{element}, ' 
    message = f'{message[0:-2]} или {allowed[-1]}\n'

    # проверим корректность ввода
    while answer not in allowed:
        answer = input(message)
    
    return answer

    
