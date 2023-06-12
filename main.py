import turtle
class Polygon :
    shapes = {3:'triangle', 4:'rectangle', 5:'pentagon'}
def __init__(self, numSide) :
    self.sideNumber = numSide
    self.sideLen = 0
def setSide(self):
    self.sideLen = float(input("Enter length of side : "))
def getShape(self) :
    print("Shape : %s" %Polygon.shapes[self.sideNumber])
def draw(self):
    for side in range(self.sideNumber):
        turtle.forward(self.sideLen)
        turtle.right(360/self.sideNumber)
        input("Enter the key")

if __name__ == "__main__":
    print('Shape: {}'.format(Polygon.shapes[5]))
    p = Polygon(4)
    print("number of sides : {}".format(p.sideNumber))
    print("length of side : {}".format(p.sideLen))
    p.setSide()
    print("length of side : {}".format(p.sideLen))
    p.getShape()
    p.draw()
