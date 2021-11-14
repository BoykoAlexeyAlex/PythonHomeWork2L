import random
# l1=[int(input('Введите число для списка ')) for _ in range(10)]
l1=[random.randint(0,10) for _ in range(10)]
k= int(input('Введите индекс элемента для удаления '))
print(l1)
for i in range(k,len(l1)-1):
    l1[i] = l1[i+1]
# print(l1)
l1.pop()
print(l1)