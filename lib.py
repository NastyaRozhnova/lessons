def check_number(number: str) -> int:
    '''
    Проверка строки на число

    :param str number: проверяемая строка
    return int
    '''
    while not number.isdigit():  # '23'
        number = input('Должна быть цифра:\n')
    return int(number)
