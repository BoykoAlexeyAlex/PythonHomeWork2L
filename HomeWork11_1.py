
def change_sys (num,base):

    from string import ascii_uppercase as char_str
    lst_main = [_ for _ in range(10)] + list(char_str)
    lst_res = []

    while num > 0 :
        lst_res.insert(0,lst_main[num%base])
        num //= base
    str_res = ''.join([str(_) for _ in lst_res])
#    print(lst_main)
    return str_res


num = int(input('Введите десятичное число '))
base = int(input('Введите основание системы счисления для перевода '))

print('В системе по основанию', base, 'число', num ,'будет записано так:', change_sys(num,base))




