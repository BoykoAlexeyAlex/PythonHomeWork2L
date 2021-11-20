h= int(input('Введите высоту треугольника '))
for i in range(h):
    for j in range(h*2-1):
        if i == h-1:
            print('*',end= ' ')
        elif j == (h-1+i) or j == (h-1-i):
            print('*',end= ' ')
        else: print(' ',end= ' ')
    print()

