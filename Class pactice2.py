# Write your code here :-)
class Rectangle:
    def __init__(self, c, l, w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area = self.length*self.width
        return self.area
    def per(self):
        self.perimeter=2*self.length+2*self.width
        return self.perimeter
    def diagonal(self):
        self.diag=(self.width**2+self.length**2)**(1/2)
        return self.diag
    def volume(self,h):
        self.height=h
        self.vol=self.length*self.width*self.height
        return self.vol





myRect1 = Rectangle('red', 2,1)
print('Color is:',myRect1.color)
print('Length is:', myRect1.length)
print('Width is:', myRect1.width)
print('Area is:', myRect1.area())
print('My Perimeter is ', myRect1.per())
print('Volume is: ', myRect1.volume(10))
print(myRect1.color)
print('myRect1 length=', myRect1.length)



myRect2 = Rectangle('blue',4, 3)
print('Your diagonal is: ',myRect2.diagonal())
print(myRect2.color)
print('myRect2 length=', myRect2.length)
print('myRect2 Area', myRect2.area())
print('myRect1 diagonal=',myRect1.diagonal())
myVol=myRect1.volume(5)
print('myRect1 Volume is: ',myRect1.vol)
print('first diagnol is: ',myRect1.diagonal())
