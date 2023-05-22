class Rectangle:
    """ This is the ractangle that will be drawn """
    def __init__(self, height, width, width_start, height_start):
        self.height = height
        self.width = width
        self.width_start = width_start
        self.height_start = height_start

    def set_color(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def draw(self, canvas):
        canvas.data[self.height_start:self.height, self.width_start:self.width] = [self.red,self.green,self.blue]
