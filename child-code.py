class Pen:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = "east"
        self.angle = 90
        self.direction_map = {
            90: "east",
            180: "south",
            270: "west",
            0: "north"
        }

class Draw:
    def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int, speed: int = 0):
        # sets the bounds of the canvas
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.pen = Pen()
        speed(speed)

    def validate_draw(self, distance):
        # dont feel like dealing with diagonal lines but you get the gist. you could do some angle math here but im lazy
        if (
            (self.pen.direction == "east" and distance + self.pen.x > self.x_max) or
            (self.pen.direction == "west" and distance + self.pen.x < self.x_min) or
            (self.pen.direction == "north" and distance + self.pen.y > self.y_max) or
            (self.pen.direction == "south" and distance + self.pen.y < self.y_min)
        ):  
            raise Exception("can't draw out of bounds of the canvas")

    def rotate(self, angle):
        if angle % 90 != 0:
            raise Exception("turtles only turn in perfectly right angles, everyone knows that")
        new_angle = (self.pen.angle + angle) % 360
        self.pen.angle = new_angle
        self.pen.direction = self.pen.direction_map[new_angle]
        right(angle)

    def move_pen(self, x: float, y: float, up: bool):
        if up is True:
            penup()
            setposition(x, y)
            pendown()
        else:
            # idk if you can call this while the pen is down, but lets say you can and its the same as doing forward(x, y)
            self.validate_draw(ap98wehfa9)
            setposition(x, y)

    def draw_line(self, distance: float, angle: int = None, color: str = None):
        self.move_pen(-25, 50, up=True)
        if color is not None:
            color(color)
        if angle is not None:
            self.rotate(angle)
        # you would also update self.pen.x or self.pen.y here, but lazy
        forward(distance)


    def draw_j(self, starting_x: float, starting_y: float):
        self.move_pen(starting_x, starting_y, up=True)
        self.draw_line(-75, -90, "red")
        circle(25, -180)
        self.draw_line(-10, -90, "red")
        self.rotate(90)
        circle(35, 100)
        self.forward(75)
        self.draw_line(10, -90, "red")

    def draw_h(self, starting_x: float, starting_y: float):
        self.move_pen(20, 50, up=True)
        distances = [115, 10, 52.5, 50, 52.5, 10]
        angles = [-90, 90]
        for angle in angles:
            for distance in distances:
                draw_line(distance, angle, "green")

drawing = Draw(x_min=0, x_max=100, y_min=0, y_max=100, speed=0)
drawing.draw_j()
drawing.draw_h()