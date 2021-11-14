import random
l1 = [random.randint(0,10) for _ in range(20)]
count = 0
print(l1)
for i in range(1,len(l1)-1):
    if l1[i] > l1[i-1] and l1[i] > l1[i+1]:
        count += 1
        print(l1[i], end=" ")
print()
print('Количество элементов, которые больше своих соседей: ', count)

