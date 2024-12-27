import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import struct

def load_kumaresan(filename):
    try:
        with open(filename, 'rb') as file:
            # Read and validate the file header
            header = file.read(8)
            if len(header) != 8:
                raise ValueError("Invalid header size")
            
            width, height = struct.unpack('II', header)
            
            # Read pixel data
            pixel_data_size = width * height * 3
            pixel_data = file.read(pixel_data_size)
            if len(pixel_data) != pixel_data_size:
                raise ValueError("Pixel data size mismatch")
            
            # Unpack pixel data
            pixels = list(struct.iter_unpack('BBB', pixel_data))
            
            # Create an image
            image = Image.new('RGB', (width, height))
            image.putdata(pixels)

            return image
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load .kumaresan file:\n{e}")
        return None

def open_kumaresan_file():
    # Open file dialog to select a .kumaresan file
    file_path = filedialog.askopenfilename(
        title="Open .kumaresan Image",
        filetypes=[("Kumaresan Images", "*.kumaresan")]
    )
    if file_path:
        # Load the .kumaresan file and display the image
        image = load_kumaresan(file_path)
        if image:
            display_image(image)

def display_image(image):
    # Resize the image for display
    max_size = (800, 600)
    image.thumbnail(max_size, Image.Resampling.LANCZOS)
    
    # Convert the image to Tkinter format
    tk_image = ImageTk.PhotoImage(image)

    # Clear the canvas
    canvas.delete("all")

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image  # Keep a reference to prevent garbage collection

# Create the Tkinter application
app = tk.Tk()
app.title("Kumaresan Image Viewer")
app.geometry("900x700")
app.resizable(True, True)

# Title Label
title_label = tk.Label(app, text="Custom Image Viewer", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

# Open File Button
open_button = tk.Button(
    button_frame, text="Open .kumaresan File", font=("Helvetica", 12),
    command=open_kumaresan_file, bg="#4CAF50", fg="white", padx=10, pady=5
)
open_button.grid(row=0, column=0, padx=10)

# Exit Button
exit_button = tk.Button(
    button_frame, text="Exit", font=("Helvetica", 12),
    command=app.quit, bg="#f44336", fg="white", padx=10, pady=5
)
exit_button.grid(row=0, column=1, padx=10)

# Canvas for Image Display
canvas = tk.Canvas(app, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Run the Tkinter event loop
app.mainloop()
