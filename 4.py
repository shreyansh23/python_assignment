import math
class shapes(object):
    pass

class rectangle(shapes):
    
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def __str__(self):
        stri ="Rectangle with length: "+str(self.length)+" and breadth: "+ str(self.breadth)   
        return stri 
    def area(self):
        return (self.length*self.breadth)
    def perimeter(self):
        return (2*(self.length+self.breadth))
           
class square(rectangle):
    def __init__(self,s):
            super(square,self).__init__(s,s)
    def __str__(self):
            stri ="Square with side: "+ str(self.breadth)   
            return stri    
             
class circle(shapes):
    def __init__(self,r):
        self.radius=r
    def __str__(self):
        stri="Circle with radius: "+str(self.radius)
        return stri
    def area(self):
        return math.pi*self.radius*self.radius
    def perimeter(self):
        return 2*math.pi*self.radius           


ci=circle(3)
#print(ci)
#print(ci.radius)
print(ci.area())
print(ci.perimeter())

sq=square(5)
#print(sq)
#rec=rectangle(3,4)

#print(rec)          
#print(rec.length)
#print(sq.area())
print(math.pi)
