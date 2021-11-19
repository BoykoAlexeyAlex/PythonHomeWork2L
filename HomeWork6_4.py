h= int(input('Введите высоту треугольника '))
str1 = ''

for i in range(h):
    for j in range(h*2-1):
        if j >= (h-1-i) and j <= (h-1+i):
            str1 += '* '
        else: str1 += '  '
    print(str1)
    str1 = ''