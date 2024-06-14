import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import pyperclip

# Function to process the image
def process_image(file_path):
    # Read the image using OpenCV
    img = cv2.imread(file_path, 0)

    # Resize the image
    img = cv2.resize(img, (128, 64), interpolation=cv2.INTER_AREA)

    # Apply thresholding
    ret, img = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

    # Make a copy of the processed image
    new_img = img.copy()

    # Convert image to binary (0 and 1)
    img[img > 125] = 1

    # Create array string representation
    array_str = "{\n"
    n = 0
    for row in img:
        array_str += "{"
        array_str += ",".join(map(str, row))
        if n != 127:
            array_str += "},\n"
        else:
            array_str += "}\n"
        n += 1
    array_str += "}"

    return new_img, array_str

# Function to copy array to clipboard
def copy_to_clipboard(array_str):
    pyperclip.copy(array_str)
    messagebox.showinfo("Success", "Array copied to clipboard!")

# Function to handle file selection and image processing
def select_image():
    file_path = filedialog.askopenfilename(title="Select an image file",
                                           filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Process the selected image
        processed_img, array_str = process_image(file_path)

        # Display the processed image using Tkinter
        display_image(processed_img)

        # Copy the array to clipboard
        copy_to_clipboard(array_str)

# Function to display image using Tkinter
def display_image(image_array):
    # Resize the image for display purposes (enlarging)
    display_img = cv2.resize(image_array, (512, 256), interpolation=cv2.INTER_NEAREST)  # Enlarging the image

    # Convert numpy array to PIL Image
    img = Image.fromarray(display_img)

    # Convert PIL Image to Tkinter PhotoImage
    img_tk = ImageTk.PhotoImage(image=img)

    # Display image on a label
    label.config(image=img_tk)
    label.image = img_tk

# Create Tkinter window
root = tk.Tk()
root.title("Image Processor")
root.geometry("800x600")  # Set the window size to be larger

# Create a frame to hold the button and image
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

# Create a button to select image
select_button = tk.Button(frame, text="Select Image", command=select_image, font=("Helvetica", 16))
select_button.grid(row=0, column=0, pady=20, padx=20)

# Create a label to display processed image
label = tk.Label(frame)
label.grid(row=1, column=0, padx=20, pady=20)

# Configure grid to resize properly
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)

# Start the Tkinter main loop
root.mainloop()
