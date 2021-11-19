import random
lst = list(random.randint(0,5) for _ in range (10))
print(lst)
print('Количество уникальных чисел в списке',len(set(lst)))
print(set(lst))