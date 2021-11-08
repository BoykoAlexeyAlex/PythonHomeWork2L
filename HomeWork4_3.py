st = input('Введите строку ')
st1=st
sy = input('Введите искомый символ ')
count = 0
symbol_exist=0
while symbol_exist >=0:
    symbol_exist = st1.find(sy)
    if symbol_exist >=0:
        st1=st1[symbol_exist+1::]
        count +=1
print('Вхождение символа',sy,'в строку',st,count, 'раз')



