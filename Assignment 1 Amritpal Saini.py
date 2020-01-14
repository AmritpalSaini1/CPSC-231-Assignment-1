#Amritpal Saini, 30039983, Catalin Dohotaru, Section 2

xc, yc = eval(input())
#xc, yc are the x and y coordinates for the centre of the circle
r = eval(input())
#r is the radius of the given circle
x1, y1 = eval(input())
#x1, y1 is the coordinates for the beginning of the given line
x2, y2 = eval(input())
#x2, y2 is the coordinates for the end of the given line
#eval(input()) is used to get values from files
import turtle #This allows the use of turtle and turtle commands

def Turtle():
    #function to store all turtle commands.
    wn = turtle.Screen() #Screen varible to allow for setting screen size
    wn.setup(800, 600) #Set screen size

    
def drawInt(x, y):
    #DrawInt is short for Draw Intercepts. It is a function that is used to shorten the code for the intersection function. It draws intercepts
    turtle.penup()
    turtle.goto(x, y - 6)
    turtle.pendown()
    turtle.circle(6)
    turtle.penup()

def intersection(xc, yc, r, x1, y1, x2, y2):
    #xc, yc, r, x1, y1, x2, y2 are varibles acquired from a given file, function intersection calculates and draws the points of intercepts
    a = ((x2 - x1)**2) + ((y2 - y1)**2) 
    b = 2 *((x1-xc) * (x2-x1) + (y1-yc) * (y2-y1))
    c = ((x1-xc)**2) + ((y1-yc)**2) - (r**2)
    #a, b, c are the value for the a quadratic equation given in the file
    intersectTest = b**2 - 4*a*c
    #intersectTest is used to calculate the discriminant. The discriminant is used to know if there is an intercept or not. 
    PlusInt = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a) 
    MinusInt = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
    #PlusInt and MinusInt are both a version of the quadratic formula. One is '-b + sqrt(...)' and the other is '-b - sqrt(...)'
    xInt1 = (1 - PlusInt) * x1 + PlusInt * x2 
    yInt1 = (1 - PlusInt) * y1 + PlusInt * y2
    xInt2 = (1 - MinusInt) * x1 + MinusInt * x2
    yInt2 = (1 - MinusInt) * y1 + MinusInt * y2
    #Function name is short for x/y intercept 1/2, Equations provided for x and y values using alpha
    if (intersectTest < 0):
        #if the discriminant is negative, there is no intercept because the value under the sqrt is negative and thus nonreal
        print("No Intercepts")
        return
    
    elif ((PlusInt < 0) or (PlusInt > 1)) and ((MinusInt < 0) or (MinusInt > 1)):
        #Using the information provided for no intercepts between point (x1, y1) and (x2, y2)
        print("No Intercepts")
        return
    
    elif (MinusInt < 0) or (MinusInt > 1):
        #Using the information provided for only one intercept between point (x1, y1) and (x2, y2)
        drawInt(xInt1, yInt1)
        print("Intercept is at: (",xInt1, " , " , yInt1, ")")
        return
    
    elif(PlusInt < 0) or (PlusInt > 1):
        #same as above but for the other side of the line
        drawInt(xInt2, yInt2)
        print("Intercept is at (", xInt2," , ", yInt2, ")")
        return
                
    elif(intersectTest > 0):
        #in the case that there are two intercepts
        drawInt(xInt1, yInt1)
        drawInt(xInt2, yInt2)
        print("Intercepts at (", xInt1, " , ", yInt1, ")  and  (" , xInt2, " , ", yInt2, ")")
        return
    
    elif (intersectTest == 0):
        #in the case that there is a tangent line
        drawInt(xInt1, yInt1)
        print("Intercept at (" , xInt1, " , ", yInt1, ")")
        return
        
def DrawCircle(xc, yc, r): #function is used to draw the circle. 
    turtle.penup()
    turtle.goto(xc, yc - r) #turtle moves down r to adjust for drawing the circle. turtle draws circle above itself not around itself
    turtle.pendown()
    turtle.circle(r)
    turtle.penup()
    return
    
def DrawLine(x1, y1, x2, y2): #function is used to draw the line that may or may not intercert the circle.
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()
    turtle.goto(x1, y1 - 10)
    turtle.pendown()
    turtle.circle(10)
    turtle.penup()
    turtle.goto(x2, y2 - 10)
    turtle.pendown()
    turtle.circle(10)
    return

def main(xc, yc, r, x1, x2, y1, y2): #funtion is used to run all functions systemactically
    Turtle()
    DrawCircle(xc, yc, r)
    DrawLine(x1, y1, x2, y2)
    intersection(xc, yc, r, x1, y1, x2, y2)
    return
    

main(xc, yc, r, x1, x2, y1, y2)


turtle.mainloop() #https://docs.python.org/2/library/turtle.html was used for turtle.mainloop(). This allows the turtle function to end and not crash the program.
