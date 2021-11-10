st = input('Введите строку ')
sy = input('Введите искомый символ ')
count = 0
symbol_exist=0
pointer = 0
while symbol_exist >=0:
    symbol_exist = st.find(sy, pointer)
    if symbol_exist >=0:
        count +=1
        pointer=symbol_exist+1
print('Вхождение символа',sy,'в строку',st,count, 'раз')



