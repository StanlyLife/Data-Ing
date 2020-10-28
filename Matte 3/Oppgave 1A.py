import random
import math
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()


label1 = tk.Label(root, text="x-coordinate")
canvas1.create_window(150, 5, window=label1)
label2 = tk.Label(root, text="y-coordinate")
canvas1.create_window(250, 5, window=label2)


def CreateGrid ():  
    xArray = np.array([range(0,10)])
    yArray = np.array([range(0,10)])
    xx,yy = np.meshgrid(xArray,yArray)
    plt.plot(xx,yy, marker='.', color = 'b' , linestyle='none')
    plt.show()
    
    
button1 = tk.Button(text='Plot', command=CreateGrid)
canvas1.create_window(200, 180, window=button1)
root.mainloop()



