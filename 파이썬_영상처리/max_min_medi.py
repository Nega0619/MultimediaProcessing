import numpy as np
from util import *
from scipy import signal

def maxFilter(image, msize):
    result=np.zeros(image.shape,dtype=np.float)
    image_size=image.shape[0]
    t=msize//2
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=image[i-t:i+t+1,j-t:j+t+1]
            
            result[i,j]=np.max(block)
    result=np.clip(result,0,255)
    return result

def minFilter(image, msize):
    result=np.zeros(image.shape,dtype=np.float)
    image_size=image.shape[0]
    t=msize//2
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=image[i-t:i+t+1,j-t:j+t+1]
            
            result[i,j]=np.min(block)
    result=np.clip(result,0,255)
    return result

def medianFilter(image, msize):
    result=np.zeros(image.shape,dtype=np.float)
    image_size=image.shape[0]
    t=msize//2
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=image[i-t:i+t+1,j-t:j+t+1]
            
            result[i,j]=np.median(block)
    result=np.clip(result,0,255)
    return result


if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    fsize=int(input('input filter size : '))
    maxImg=maxFilter(Image,fsize)
    minImg=minFilter(Image,fsize)
    mediImg=medianFilter(Image,fsize)
    showNImage(Image,None,None,maxImg,minImg,mediImg)   
