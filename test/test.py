import numpy as np 
from PIL import Image

# with np.zeros(x,y,z) an array is created where x = the height y = the length z is the depth
data = np.zeros((5, 8, 3), dtype=np.uint8)
# [:] replaces all the values in array with the after mentioned values
data[:] = [0, 0, 255]

# accessing the data works in a similar fashion so you do the [] again where the x, y, z values can be accessed individually and given a new value 
# data[0,0, 0:2] = [0, 0]

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')
