from PIL import Image #importing libraries
color = (46, 0, 253) #What color u want to use
width, height = 500, 500 #Defining the images structure
image = Image.new("RGB", (width, height), color) #Creating the image
image.save("colored_image.png") #Saving the image as "colored_image.png"
image.show() #Opens a window to show the image *OPTIONAL*
Image_path = r"C:\Users\hp\AppData\Local\Temp\wct1E64.tmp" #To show where the image is stored
