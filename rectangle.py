from canvas import Canvas 

class Rectangle(Canvas):
    """ This is the ractangle that will be drawn """
    def __init__(self, height, width, color='white'):
        super().__init__(height, width, color)

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
