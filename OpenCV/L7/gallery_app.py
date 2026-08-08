import os
from pathlib import Path
import cv2
from tkinter import *
from PIL import Image, ImageTk

path= Path.home() / "Documents" / "Stuff" / "Coding" / "Visual Studio Code" / "Jet_Learn" / "OpenCV" / "L7" / "images"

image_files = []

for file in os.listdir(path):
    if file.endswith(".jpg") or file.endswith("png") or file.endswith(".jpeg"):
        image_files.append(file)
        
print(image_files)

curr_image = 0
root = Tk()
root.title("Photo Gallery with OpenCV")

def load_image():
    global photo
    img_path = os.path.join(path,image_files[curr_image])
    img = cv2.imread(img_path)
    print(img)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    img = Image.fromarray(img)
    img = img.resize((500,400))
    
    photo = ImageTk.PhotoImage(img)
    
    label.config(image=photo)
    label.image = photo

def next_image():
    global curr_image
    curr_image += 1
    
    if curr_image >= len(image_files):
        curr_image = 0
    load_image()
    
def prev_image():
    global curr_image
    
    curr_image -= 1
    if curr_image < 0:
        curr_image = len(image_files) - 1
    load_image()
    
def grayscale():
    global photo
    img_path = os.path.join(path,image_files[curr_image])
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        
    img = Image.fromarray(gray)
    img = img.resize((500,400))
        
    label.config(image = photo)
    label.image = photo
    
label=Label(root)
Label.pack()
load_image()

prev_btn = Button(root, text = "Previous", command = prev_image)
prev_btn.pack(side=LEFT, padx=10, pady=10)

next_btn = Button(root, text = "Next", command = next_image)
next_btn.pack(side=LEFT, padx=10, pady=10)

gray_btn = Button(root, text = "Grayscale Filter", command=grayscale)
gray_btn.pack(side=LEFT, padx=10, pady=10)

root.mainloop()