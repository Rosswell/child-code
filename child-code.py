def move_no_pen(x, y):
    penup()
    setposition(x,y)
    pendown()
    
def draw_line(distance, angle):
    move_no_pen(-25, 50)
    color("red")
    right(angle)
    forward(distance)
    
def draw_j():
    draw_line(-75, -90)
    circle(25, -180)
    draw_line(-10, -90)
    right(90)
    circle(35, 100)
    forward(75)
    draw_line(10, -90)
    
def draw_h():
    move_no_pen(20, 50)
    color("green")
    distances = [115, 10, 52.5, 50, 52.5, 10]
    angles = [-90, 90]
    for angle in angles:
        for distance in distances:
            draw_line(distance, angle)

speed(0)
draw_j()
draw_h()