class Box:
    def area(self):
        return self.width*self.height
    def __init__(self,width,height):
        self.width = width
        self.height = height
x = Box(10,2)
print(x.area())
