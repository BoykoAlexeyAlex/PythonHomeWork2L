stud1 = int(input('Введите количество учеников класса 1 '))
stud2 = int(input('Введите количество учеников класса 2 '))
stud3 = int(input('Введите количество учеников класса 3 '))
desk1 = stud1//2+stud1%2
desk2 = stud2//2+stud2%2
desk3 = stud3//2+stud3%2

print('В класс 1 нужно ',desk1,(' парт'))
print('В класс 2 нужно ',desk2,(' парт'))
print('В класс 3 нужно ',desk3,(' парт'))
print('Всего нужно ',desk1+desk2+desk3,(' парт'))