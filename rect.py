import Polygon

class Rectangle(Polygon.Polygon) :
    def __init__(self) :
        Polygon.Polygon.__init__(self, 4)
    def getArea(self) :
        self.area = self.sideLen * self.sideLen
        print(self.area)

r = Rectangle()
r.setSide()
r.getArea()
r.getShape()