print('Введите целое число')
num = int(input())
square =1
count = 1
while square<=num:
    count += 1
    print(square, end=" ")
    square = count ** 2
