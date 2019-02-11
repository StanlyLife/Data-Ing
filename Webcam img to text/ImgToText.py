#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 15:48:00 2018

@author: Stian
"""
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
#from tkinter import Tk, Label
from tkinter import *

global cap
width, height = 400, 400
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    
    
def go_second():
    global root
    global lmain
    global l2
    root = Tk()
    root.bind('<Escape>', lambda e: root.quit())
    lmain = Label(root)
    lmain.pack()
    l2 = Label(root)
    l2.pack()
    
    
    
    
    show_frame()

def show_frame():
    global frame
    global test
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

def bilde():
    print('writing')
    a = cap.read()[1]
    b = cv2.imwrite('pic.png', a)
    print(str(b))
    
    
    
def read():
    print('reading image')
    img = 'pic.png'
    i2s = pytesseract.image_to_string(img)
    print(i2s)

go_second()
bildeBtn = Button(l2, text='Snap',command=bilde)   
bildeBtn.config(fg='black',height=4,width=7)
bildeBtn.grid(row=1,column=1)

readBtn = Button(l2, text='read',command=read)   
readBtn.config(fg='black',height=4,width=7)
readBtn.grid(row=1,column=2)

root.mainloop()

'''
img = cv2.imread('img.png')

#Rearrang the color channel
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))

# A root window for displaying objects
root = Tkinter.Tk()  

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im) 

# Put it in the display window
Tkinter.Label(root, image=imgtk).pack() 

root.mainloop() # Start the GUI
'''   
    
'''    
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")

# Simple image to string
print(pytesseract.image_to_string(Image.open('lorem.jpeg')))

# French text image to string
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Get bounding box estimates
#print(pytesseract.image_to_boxes(Image.open('lorem.jpeg')))

# Get verbose data including boxes, confidences, line and page numbers
#print(pytesseract.image_to_data(Image.open('lorem.jpeg')))

# Get information about orientation and script detection
#print(pytesseract.image_to_osd(Image.open('lorem.jpeg')))

# In order to bypass the internal image conversions, just use relative or absolute image path
# NOTE: If you don't use supported images, tesseract will return error
print(pytesseract.image_to_string('lorem.jpeg'))
'''