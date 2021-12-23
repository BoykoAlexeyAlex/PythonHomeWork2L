class Buffer :

    def __init__(self):
        self.lst = []
        self.count = 1

    def get_current_part(self):
        return sum(self.lst)

    def add(self, *args: int):
        for i in range (len(args)):
            if len(self.lst) < 5:
                self.lst.append(args[i])
            else:
                print(f'Сумма элементов с {self.count} по {self.count + 4} равна {self.get_current_part()}')
                self.count += 5
                self.lst.clear()
                self.lst.append(args[i])
            if len(self.lst) == 5 :
                print(f'Сумма элементов с {self.count} по {self.count + 4} равна {self.get_current_part()}')
                self.count += 5
                self.lst.clear()





a = Buffer()
a.add(1, 1, 1)
a.add(1, 1, 10, 10, 10)
a.add(10, 10, 3, 3, 3, 3, 3)
a.add(100, 100)
a.add(100)
a.add(100, 100, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6)


