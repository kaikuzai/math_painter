from canvas import Canvas 

class Rectangle(Canvas):
    """ This is the ractangle that will be drawn """
    def __init__(self, height, width, width_start, height_start):
        super().__init__(height, width)
        self.width_start = width_start
        self.height_start = height_start

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
