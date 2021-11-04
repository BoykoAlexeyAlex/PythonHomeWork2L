num = 1
num_count = 0
num_summ = 0
num_min = 0
num_max = 0
odd_counter = 0

while num != 0 :
    print('Введите целое число, для выхода введите 0')
    num = int(input())
    if num_count < 1:
        num_min = num
    elif num < num_min and num != 0:
        num_min = num
    if num % 2 > 0 :
        odd_counter += 1
    if num > num_max:
        num_max = num
    num_summ += num
    if num != 0:
        num_count += 1

print ('Количество введеных чисел', num_count)
print('Сумма введенных чисел', num_summ)

if num_count > 0:
    print('Среднее арифметическое введеных чисел',num_summ/(num_count))
else:
    print('Среднее арифметическое введеных чисел', 0 )

print('Минимальное значение', num_min)
print('Максимальное значение', num_max)
print('Количество нечетных чисел', odd_counter)
print('Количество четных чисел', ((num_count)-odd_counter))

