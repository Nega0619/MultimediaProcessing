import numpy as np
from util import *
from binarization import *

def erosion(image, kernel):
    ##0,1을 가지는 이진영상으로 변환
    bimg=image.astype(np.bool)
    result=np.zeros(image.shape,dtype=np.uint8)
    image_size=image.shape[0]
    ksize=kernel.shape[0]
    t=ksize//2
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=bimg[i-t:i+t+1,j-t:j+t+1]
            r=block*kernel
            if(np.array_equal(r,kernel)):
                result[i,j]=255
    return result

def dilation(image, kernel):
    ##0,1을 가지는 이진영상으로 변환
    bimg=image.astype(np.bool)
    result=np.zeros(image.shape,dtype=np.uint8)
    image_size=image.shape[0]
    ksize=kernel.shape[0]
    t=ksize//2
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=bimg[i-t:i+t+1,j-t:j+t+1]
            r=block*kernel
            if(np.any(r)):
                result[i,j]=255
    return result
def morp_open(image,kernel):
    ero=erosion(image,kernel)
    result=dilation(ero,kernel)
    return result
def morp_close(image,kernel):
    dil=dilation(image,kernel)
    result=erosion(dil,kernel)
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    #영상 이진화
    bimg=binarization(Image,80)
    kernel_4=np.array([[0,1,0],
                       [1,1,1],
                       [0,1,0]])
    kernel_8=np.full((3,3),1)
    out_ero_4=erosion(bimg,kernel_4)
    out_ero_8=erosion(bimg,kernel_8)
    out_dil_4=dilation(bimg,kernel_4)
    out_dil_8=dilation(bimg,kernel_8)
    showNImage(bimg, out_ero_4, out_ero_8,
                 out_dil_4, out_dil_8)
    
