from PIL import Image
import struct 

def convert_jpg_custom(image,output_name):
    image = Image.open(image)

    rgb_image = image.convert('RGB')
    width,height = image.size 

    pixel = list(rgb_image.getdata())
    binary_pixel = bytearray()

    for pixel_data in pixel:
        r,g,b = pixel_data
        binary_pixel.extend(struct.pack('BBB',r,g,b))
    
    with open(output_name,'wb') as file:
        file.write(struct.pack('II',width,height))
        file.write(binary_pixel)


    print("Succesfully convert to the custom image format")


input_jpg = "image2.jpeg"
output_name = "testingforvideo.kumaresan"

convert_jpg_custom(input_jpg,output_name)