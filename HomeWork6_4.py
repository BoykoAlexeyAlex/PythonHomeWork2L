h= int(input('Введите высоту треугольника '))
for i in range(h):
    for j in range(h*2-1):
        if j >= (h-1-i) and j <= (h-1+i):
            print('*',end= ' ')
        else: print(' ',end= ' ')
    print()
