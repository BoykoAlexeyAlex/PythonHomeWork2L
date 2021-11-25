

def season (month_num):
    sl = ('весна','лето','осень')
    if month_num//3 > 0 and month_num//3 < 4 :
        s = sl[month_num//3-1]
    else:
        s = 'зима'
    return s

month = int(input('Введите номер месяца '))
print('Это',season(month))
