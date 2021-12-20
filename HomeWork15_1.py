

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
        print(f'Имя: {self.__name} Фамилия: {self.__surname} Оценка {self.__grade}')

class Group () :

    def __init__(self,lst=[]):
        self.lst = lst

    def add_student(self,student):
        self.lst.append(student)

    def print_group(self):
        for i in range (len(self.lst)):
            self.lst[i].std_print()


group1 = Group()
for i in range (5):
    a = Student()
    a.set_student()
    group1.add_student(a)
print()
group1.print_group()








