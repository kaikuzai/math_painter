import numpy as np
from PIL import Image


class Canvas:
    """" Here we will set up a canvas which will be drawn"""

    def __init__(self, height, width, color='white'):
        self.height = height
        self.width = width
        self.color = color 

    # def set_canvas_color(self, canvas_color):
    #     if canvas_color == 'white':
    #         self.color = 
