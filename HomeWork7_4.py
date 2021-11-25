def is_year_leap (year_num):
    if year_num % 400 == 0 or year_num % 4 == 0 and year_num % 100 !=0 :
        is_leap = True
    else:
        is_leap = False
    return is_leap

y = int(input('Введите номер года '))
print(is_year_leap(y))