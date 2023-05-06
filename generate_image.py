from PIL import Image 
import numpy as np 

class GenerateImage:
    """" Here the image will be generated"""
    def __init__(self, canvas, rectangle):
        self.canvas = canvas 
        self.rectangle = rectangle 


    def generate_image(self):
        data = np.zeros((self.canvas.height, self.canvas.width, 3), dtype=np.uint8)
        if self.canvas.color == 'black':
            data[:] = [0, 0, 0]
        elif self.canvas.color == 'white':
            data[:] = [255, 255, 255]
        else:
            print("since you didn't choose 'black' or 'white' we'll make it white :)")
            data[:] = [0, 0, 0]
        
        data[self.rectangle.height_start:self.rectangle.height, self.rectangle.width_start:self.rectangle.width] = [self.rectangle.red, self.rectangle.blue, self.rectangle.green]

        img = Image.fromarray(data, 'RGB')
        img.save('canvas.png')       