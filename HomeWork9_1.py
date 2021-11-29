import random


def lst_sort (lst1):
    # Функция сортирует все списки в списке по возрастанию
    # Тут используем двойную пузырьковую сортировку :
    # перемещаем самый большой элемент слева направо, а самый маленький справа налево за один проход,
    # таким образом сокращая количество проходов
    for a in lst1:
        lst_tmp = a
        for j in range(len(lst_tmp)//2):
            change = False
            for i in range(len(lst_tmp) - 1 - j):
                if lst_tmp[i] > lst_tmp[i + 1]:
                    lst_tmp[i], lst_tmp[i + 1] = lst_tmp[i + 1], lst_tmp[i]
                    change = True
                if lst_tmp[len(lst1) - 1 - i] < lst_tmp[len(lst1) - 2 - i]:
                    lst_tmp[len(lst1) - 1 - i], lst_tmp[len(lst1) - 2 - i] = lst_tmp[len(lst1) - 2 - i], lst_tmp[len(lst1) - 1 - i]
                    change = True
            if not change:
                break

    return lst1


def lst_print (lst):
    # Печатаем списки не построчно, а поколонно, выравниваем отступы в зависимости от разрядности числа
    for col in range(len(lst)):

        for row in range( len(lst)):
            if lst [row][col]<10:
                print(lst[row][col], end='   ')
            else:
                print(lst[row][col], end='  ')
        print()
    for i in range (len(lst)):
        if sum(lst[i]) >= 100:
            print (sum(lst[i]), end=' ')
        else:
            print(sum(lst[i]), end='  ')






size1 = int(input('Введите размер матрицы (не менее пяти) '))
lst_main = [[random.randint(1,50) for _ in range(size1)] for _ in range(size1)] # Создаем список списков

lst_print(lst_main)
print()
print()

lst_main = lst_sort(lst_main) # Получаем сортированый список списков

# Сортируем списки по сумме элементов по возрастанию с помощью простой пузырьковой сортировки
for i in range(len(lst_main)):
    for j in range(len(lst_main)-1-i):
        if sum(lst_main[j])>sum(lst_main[j+1]):
            lst_main[j],lst_main[j+1] = lst_main[j+1],lst_main[j]

# Переворачиваем каждый нечетный список
for i in range (len(lst_main)):
    if not i % 2:
        lst_main[i].reverse()

lst_print(lst_main)

