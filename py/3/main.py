import pylab as py

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Line(Point):


    def __init__(self, p1, p2):


        self.org= p1

        self.ext= p2

    def __str__(self):


        return '(' + self.org.__str__() + ',' + self.ext.__str__() + ')'

    def plot(self, fmt):

        xvalues= [self.org.x, self.ext.x]

        yvalues= [self.org.y, self.ext.y]

        py.plot(xvalues, yvalues, fmt)

    def shift(self, dx, dy):

        self.org.shift(dx, dy) # shift its org point

        self.ext.shift(dx, dy) # shift its ext point


point=Point(4,1)
line=Line(10,2)
# line.plot(2)
print(line)
