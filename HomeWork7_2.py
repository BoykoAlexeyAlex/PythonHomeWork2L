

def arithmetic (op1, op2, operation):
    if operation == '+':
        res = op1 + op2
    elif operation == '-':
        res = op1 - op2
    elif operation == '*':
        res = op1*op2
    elif operation == '/':
        res = op1/op2
    else:
        res = 'Неизвестная операция'
    return res


o1 = int(input('Введите первый операнд '))
o2 = int(input('Введите второй операнд '))
op = input('Введите операцию ')
print('Результат операции:',arithmetic(o1,o2,op))

        