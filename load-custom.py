from PIL import Image 
import struct 

def load_custom(custom_image):
    with open(custom_image,'rb') as file:
        header = file.read(8)

        if len(header)!=8:
            print("Unsupported file")
        width,height = struct.unpack('II',header)

        total_pixel_size = width*height*3 # rgb
        pixel_data = file.read(total_pixel_size)

        if total_pixel_size!=len(pixel_data):
            raise ValueError("pixel data mismatch")
        pixels = list(struct.iter_unpack('BBB',pixel_data)) # binary pixel data to rgb values

        image = Image.new("RGB",(width,height))
        image.putdata(pixels)
        return image




file_path = "testingforvideo.kumaresan"
image = load_custom(file_path)

if image:
    image.show()