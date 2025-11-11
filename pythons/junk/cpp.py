import random
a = ["fefs", 'sfe', 'rp', 's', 'uyi', 'q', 'sfg', '[][][ef[e]', 'fs.lr', 'feb', 'b', 'v', 'm', 'mnbv', 'sfgrr55', '23ef', 'as', 'q1', 'sfsfrf', 'e4']
def randomword():
    word = ''
    lena = len(a)
    for _ in range(10):
        word += a[random.randint(0, lena-1)]
    return word


with open("10000classes.py", 'w') as f:
    

    for i in list(map(str, range(10000))):
        cl = """class Furniture"""
        cl += i
        cl += ''':
    def __init__(self, furniture_name, x, y, z):
        # Аналог strcpy - просто присваиваем строку
        self.name = furniture_name
        
        # Берем модули размеров (аналог обработки в C++)
        self.sizeX = abs(x)
        self.sizeY = abs(y) 
        self.sizeZ = abs(z)
    
    def display_info(self):
        print("Furniture Information:")
        print(f"Name: {self.name}")
        print(f"Dimensions: {self.sizeX} x {self.sizeY} x {self.sizeZ}")
        print(f"Total Size: {self.sizeX * self.sizeY * self.sizeZ} cubic units")\n\n'''
        cl += "class"
        cl += i
        cl += " = Furniture"
        cl += i
        cl += "("
        strarg = f"'{randomword()}', {random.randint(-4, 100)}, {random.randint(-6, 1243)}, {random.randint(-234, 234)}"
        cl += strarg
        cl += ")\n\n"
        f.write(cl)