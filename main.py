from rectangle import Rectangle 
from canvas import Canvas 
from generate_image import GenerateImage

colors = {"black":[0,0,0],
          "white":[255,255,255]}

canvas_width = int(input('What width would you like your canvas to be?: '))
canvas_height = int(input('What height would you like your canvas to be?: '))
canvas_color = input('What color would you like your object to be? choose [black]/[white]: ')

canvas = Canvas(canvas_height, canvas_width, color=colors[canvas_color])

while True:
    add_rectangle = input("Would you like to add a rectangle to the canvas? [yes/no]: ")
    if add_rectangle.upper() == 'YES':
        rectangle_width_start = int(input("where would you like your rectangle to start in width?: "))
        rectangle_height_start = int(input("where would you like your rectangle to start in height?: "))
        rectangle_width = int(input("Which width would you like your rectangle to have?: "))
        rectangle_height = int(input("Which height would you like your rectangle to have?: "))
        rectangle_R = int(input("So we're working with the RGB system how much Red would you like in your Rectangle?: ")) 
        rectangle_G = int(input(f"Okay we have {rectangle_R} in the rectangle how much Green would you like?: "))
        rectangle_B = int(input("Alright and finally how much Blue should we add?: "))

        rectangle = Rectangle(height=rectangle_height, width=rectangle_width, height_start=rectangle_height_start, width_start=rectangle_width_start)
        rectangle.set_color(red=rectangle_R, green=rectangle_G, blue=rectangle_B)
        rectangle.draw(canvas)
    else:
        break


print("Okay your image has been generated! Take a look")

image = GenerateImage(canvas)
image.generate_image()