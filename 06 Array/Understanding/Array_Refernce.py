class Akshay():
    def __init__(self,name, cls, rol):
        self.name = name
        self.cls = cls
        self.rol = rol

    def disp(self):
        print(self.cls)
        print(self.rol)
        print(self.name)

a = Akshay("Ap", 12, 21)
a.disp()