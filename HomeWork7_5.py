

def square(len1):
    p = len1*4
    s = len1**2
    d = (s*2)**0.5
    return p,s,d

l = int(input('Введите длину стороны квадрата '))
p,s,d = square(l)
print('Периметр равен:',p,', Площадь равна',s,', Диагональ равна',round(d,2))
