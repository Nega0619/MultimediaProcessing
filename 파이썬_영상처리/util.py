import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog
import tkinter

def readImage(path):
    image=np.fromfile(path,dtype=np.uint8)
    image=image.reshape(256,256)
    image=image.astype(np.int16)
    return image

def showImage(image):
    result=image.copy()
    result=result.astype(np.uint8)
    plt.imshow(result, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    plt.show()

def show2Image(image1, image2):
    i1=image1.astype(np.uint8)
    i2=image2.astype(np.uint8)
    f = plt.figure()
    f.add_subplot(1,2, 1)
    plt.imshow(i1, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    f.add_subplot(1,2, 2)
    plt.imshow(i2, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    plt.show(block=True)
    
def show3Image(image1, image2, image3):
    i1=image1.astype(np.uint8)
    i2=image2.astype(np.uint8)
    i3=image3.astype(np.uint8)
    f = plt.figure()
    f.add_subplot(1,3, 1)
    plt.imshow(i1, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    f.add_subplot(1,3, 2)
    plt.imshow(i2, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    f.add_subplot(1,3, 3)
    plt.imshow(i3, cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    plt.show(block=True)

def showNImage(*imgs):
    n=len(imgs)
    f=plt.figure()
    f.gca().set_axis_off()
    f.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    
    for i in range(n):
        if(not np.any(imgs[i])):
            continue
        if(n<4):
            f.add_subplot(1,n,i+1)
        else:
            g_w=int(np.math.ceil(n/2))
            f.add_subplot(2,g_w,i+1)
        f.gca().xaxis.set_major_locator(plt.NullLocator())
        f.gca().yaxis.set_major_locator(plt.NullLocator())
        img=imgs[i].astype(np.uint8)
        plt.imshow(img, cmap='gray',vmin=0, vmax=255, interpolation='none')
    plt.show(block=True)
    
def load_gui():
    window=tkinter.Tk()
    window.withdraw()
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("raw image files", "*.raw"),))
    return filename
    
if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    showImage(Image)
