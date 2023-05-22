from PIL import Image 
import numpy as np 

class GenerateImage:
    """" Here the image will be generated"""
    def __init__(self, canvas):
        self.canvas = canvas 


    def generate_image(self):

        img = Image.fromarray(self.canvas.data, 'RGB')
        img.save('canvas.png')