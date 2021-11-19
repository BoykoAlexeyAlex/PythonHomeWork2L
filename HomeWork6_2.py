import random
lst1 = list(random.randint(0,20) for _ in range (10))
lst2 = list(random.randint(0,20) for _ in range (10))
print(lst1)
print(lst2)
print ('Количество уникальных чисел в обеих списках', len(set(lst1 + lst2)))
print (set(lst1 + lst2))
