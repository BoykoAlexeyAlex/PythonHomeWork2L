num = 0
maxi_num = 2
degree_count = 0
print('Введите целое число')
num= int(input())
while maxi_num <= num:
    maxi_num *=2
    degree_count +=1
if maxi_num > 2 :
    print('Наибольшая степень двойки, которая не больше введенного числа',int(maxi_num/2))
    print('Это 2 в', degree_count, 'степени')
else:
    print('Не существует степеней двойки меньше, либо равных введеному числу')


