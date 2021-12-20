class Counter :
    def __init__(self,min=0,max=100,current=0):
        self.min = min
        self.max = max
        self.current = current
    def set_count(self,min,max,current):
        self.min = min
        self.max = max
        self.current = current
    def get_current(self):
        return  self.current
    def add_current(self):
        self.current +=1


d = Counter(2,10,5)
print(d.get_current())
d.set_count(10,100,20)
print (d.get_current())
d.add_current()
print(d.get_current())