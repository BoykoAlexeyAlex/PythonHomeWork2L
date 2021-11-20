h= int(input('Введите высоту фигуры в символах (нечетное количество) '))
for i in range(h):
    for j in range(h):
        if j >= (h//2-i) and j <= (h//2+i) and i<=h//2 :
            print('*',end= ' ')
        elif i >= h//2 and j==i-h//2 or j==h-1-(i-h//2) or j==h//2:
            print('*',end= ' ')
        else: print(' ',end=' ')
    print()