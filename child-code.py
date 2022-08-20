def moveNoPen(x,y):
    penup()
    setposition(x,y)
    pendown()
    
def drawLine(distance,angle1):
    right(angle1)
    forward(distance)
    
def drawJ():
    drawLine(-75,-90)
    circle(25,-180)
    drawLine(-10,-90)
    right(90)
    circle(35,100)
    forward(75)
    drawLine(10,-90)
    
arguments = ((115,-90),(10,-90),(52.5,-90),(50,90),(52.5,90),(10,-90))
def drawH():
    for i in range(2):
        for v in range(6):
            drawLine(arguments[v][0],arguments[v][1])
            
speed(0)
moveNoPen(-25,50)
color("red")
drawJ()
moveNoPwn(20,50)
color("green")
drawH()