number = int(input('Введите число: '))
summ = 0

while number != 0:
    last_num = number % 10
    summ += last_num
    if last_num == 5:
        print('Обнаружен разрыв')
        break
    number //= 55
    print('Текущая сумма цифр:', summ)
    print('\nИтоговая сумма цифр', summ)