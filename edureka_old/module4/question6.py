class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def cal_distance(self,point2):
        point1 = self
        dist = (point1.x-point2.x)**2+(point1.y-point2.y)**2
        dist = dist**0.5
        return dist
p1 = Point(1,1)
p2 = Point(5,4)
print("The distance is {0}".format(p1.cal_distance(p2)))
