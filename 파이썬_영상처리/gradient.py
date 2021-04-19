import numpy as np
from util import *

def calGrad(img):
    gX=np.zeros(img.shape,dtype=np.float)
    gY=np.zeros(img.shape,dtype=np.float)
    image_size=img.shape[0]
    for i in range(1,image_size-1):
        for j in range(1,image_size-1):    
            gX[i,j]=img[i+1,j]-img[i,j]
            gY[i,j]=img[i,j+1]-img[i,j]
    return gX,gY

def calGradSize_sq(gX,gY):
    return np.sqrt(np.power(gX,2)+np.power(gY,2))

def calGradSize_ab(gX,gY):
    return np.absolute(gX)+np.absolute(gY)

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    gX,gY=calGrad(Image)
    gSize_sq=calGradSize_sq(gX,gY)
    gSize_ab=calGradSize_ab(gX,gY)
    agX=np.absolute(gX)
    agY=np.absolute(gY)
    showNImage(Image, agX, agY,gSize_sq, gSize_ab)
