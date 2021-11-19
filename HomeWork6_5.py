h= int(input('Введите высоту фигуры в символах (нечетное количество) '))
str1 = ''
for i in range(h):
    for j in range(h):
        if j >= (h//2-i) and j <= (h//2+i) and i<=(h)//2 and i<=h//2:
            str1 += '* '
        elif i >= h//2 and j==i-h//2 or j==h-1-(i-h//2):
            str1 +='* '
        else: str1 += '  '
    print(str1)
    str1 = ''
