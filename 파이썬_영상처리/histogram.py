import numpy as np
from util import *
import matplotlib.pyplot as plt

def histogram(img):
    #1. loop를 이용한 히스토그램 
    #hist=[0]*256 #0-255의 index를 가지는 배열을 만듬
    #image_size=img.shape[0]
    #for i in range(image_size):
        #for j in range(image_size):
            #p=img[i,j]
            #hist[p]+=1

    #2. numpy를 이용한 히스토그램
    value, counts=np.unique(img, return_counts=True)
    hist=np.zeros(256, dtype=np.int)
    hist[value]=counts
    return hist

def showhist(img,hist):
    x=np.arange(0,256,1)
    f=plt.figure()
    f.add_subplot(2,1,1)
    f.gca().xaxis.set_major_locator(plt.NullLocator())
    f.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.imshow(img,cmap='gray',vmin=0, vmax= 255, interpolation ='none')
    f.add_subplot(2,1,2)
    plt.bar(x,hist,color='black')
    plt.xlim(0,255)
    plt.ylim(0,np.max(hist))
    plt.show()
    
if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    hist=histogram(Image)
    showhist(Image,hist)
