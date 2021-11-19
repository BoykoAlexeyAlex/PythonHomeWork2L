h= int(input('Введите высоту фигуры в символах (нечетное количество) '))+1
str1 = ''
t1 = 0
t2 = 0
for i in range(h-1):
    for j in range(h-1):
        t1 = i-h//2+1
        t2 = (h-1-i)
        if j >= (h//2-1-i) and j <= (h//2-1+i) and i<=(h-1)//2 and i<=h//2:
            str1 += '* '
        elif i >= h//2 and j==i-h//2+1 or j==h-2-(i-h//2+1):
            str1 +='* '
        else: str1 += '  '
    print(str1)
    str1 = ''
