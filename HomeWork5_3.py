import random
l1 = [random.randint(0,50) for _ in range(20)]
temp = 0
print(l1)
for i in range(len(l1)//2):
    temp = l1[i]
    l1[i] = l1[len(l1)-1-i]
    l1[len(l1) - 1 - i] = temp
print(l1)
