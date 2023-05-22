import numpy as np
from PIL import Image


class Canvas:
    """" Here we will set up a canvas which will be drawn"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color 

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

        #     data = np.zeros((self.canvas.height, self.canvas.width, 3), dtype=np.uint8)
        # if self.canvas.color == 'black':
        #     data[:] = [0, 0, 0]
        # elif self.canvas.color == 'white':
        #     data[:] = [255, 255, 255]
        # else:
        #     print("since you didn't choose 'black' or 'white' we'll make it white :)")
        #     data[:] = [0, 0, 0]
        
        # data[self.rectangle.height_start:self.rectangle.height, self.rectangle.width_start:self.rectangle.width] = [self.rectangle.red, self.rectangle.blue, self.rectangle.green]


    # def set_canvas_color(self, canvas_color):
    #     if canvas_color == 'white':
    #         self.color = 
