import struct
from PIL import Image

def convert_jpg_to_kumaresan(input_jpg, output_kumaresan):
    try:
        # Open the JPEG image
        image = Image.open(input_jpg)
        
        # Ensure the image is in RGB mode
        image = image.convert('RGB')
        
        # Get image dimensions
        width, height = image.size
        
        # Get pixel data
        pixel_data = list(image.getdata())
        
        # Store packed data in a variable
        packed_pixels = bytearray()
        for pixel in pixel_data:
            r, g, b = pixel  # Unpack pixel RGB values
            packed_pixels.extend(struct.pack('BBB', r, g, b))

        # Open the file in binary write mode
        with open(output_kumaresan, 'wb') as file:
            # Write the header (width and height as unsigned integers)
            file.write(struct.pack('II', width, height))
            
            # Write pixel data from the packed variable
            file.write(packed_pixels)
        
        print(f"Converted {input_jpg} to {output_kumaresan} successfully!")
    except Exception as e:
        print(f"Failed to convert JPG to .kumaresan: {e}")

# Example Usage
if __name__ == "__main__":
    input_jpg = "image-testing.jpeg"  # Replace with your JPG file
    output_kumaresan = "image.kumaresan"  # Output file name
    convert_jpg_to_kumaresan(input_jpg, output_kumaresan)
