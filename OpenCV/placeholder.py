import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Editor")
root.geometry("850x650")

img = None
org_img = None
display_img = None

def show_image(image):
    global display_img
    display_img = image
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image), (500, 350)
    
    img_pil = Image.fromarray(image)
    img_tk = ImageTk.PhotoImage(img_pil)
    
    panel.config(image=img_tk)
    panel.image = img_tk
    
def load_image(path):
    global img, img_tk
    
    img = cv2.imread(path)
    org_img = img.copy()
    
    show_image(img)

def grayscale():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    show_image(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR))
    
def blur():
    blurred = cv2.GaussianBlur(img, (15, 15), 0)
    show_image(blurred)
    
def edge():
    edges = cv2.Canny(img, 100, 200)
    show_image(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR))

def cartoon():
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    
    edges = cv2.adaptiveThreshold(
        gray, 255
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9, 9
    )
    
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon_img = cv2.bitwise_and(color, color, ask = edges)