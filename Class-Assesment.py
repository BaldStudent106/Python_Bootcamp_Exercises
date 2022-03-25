'''
This is my exercise for OOP in Python
'''

#Question 1: Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.


#define the object Line
class Line():

    #def line init method
    def __init__(self,c1,c2):
        self.x1,self.x2=c1
        self.y2,self.y1=c2

    #def Line distance method
    def distance(self):
        return((self.x2-self.x1)**2 + (self.y2-self.y1)**2)**0.5

    #def Line slope method
    def slope(self):
        return(self.y2-self.y1)/(self.x2-self.x1)


#define the value or coordinates
coor1=(5,6)
coor2=(9,1)

#Created a Line object
line_example=Line(coor1,coor2)

#Call distance method
print(line_example.distance)

#Call slope method
print(line_example.slope(coor1,coor2))


