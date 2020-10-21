number1 = int(input('Введите первое число\n'))
number2 = int(input('Введите второе число\n'))
sign = input('Введите знак\n')

if sign == "+":
    s = number1+number2
    ans = 'сумма'

if sign == "-":
    s = number1-nunmer2
    ans = 'разность'

print(ans, s)
