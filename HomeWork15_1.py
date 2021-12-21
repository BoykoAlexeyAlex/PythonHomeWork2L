def align(str1):
    for i in range(20 - len(str1)):
        str1 += ' '
    return str1

class Student () :

    def __init__(self,name = '',surname='',grade=0):
        self.__name = name
        self.__surname = surname
        self.__grade = grade



    def set_student(self):
        self.__name = input('Введите имя студента ')
        self.__surname = input('Введите фамилию студента ')
        self.__grade = input('Введите оценку студента ')



    def std_print(self):

        print(align(self.__surname)+align(self.__name)+align(self.__grade))

class Group () :

    def __init__(self):
        self.__lst = []


    def add_student(self):
        while True:
            a = Student()
            a.set_student()
            self.__lst.append(a)
            key = input('Введите "n" для окончания ввода или любой символ для продолжения ')
            if key == 'n':
                break

    def print_group(self):
        print(align('Фамилия') + align('Имя') + align('Оценка'))
        print()
        for i in range (len(self.__lst)):
            self.__lst[i].std_print()


group1 = Group()
group1.add_student()
print()
group1.print_group()








