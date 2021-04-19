import numpy as np
from util import *
from maskop import *
from gradient import calGradSize_ab

def calGrad_mask(img, maskR, maskC):
    gX=mask_op(img, maskR)
    gY=mask_op(img, maskC)
    result=calGradSize_ab(gX,gY)
    return result


def robots(img):
    maskR=np.array([[0,0,-1],
                    [0,1,0],
                    [0,0,0]],dtype=np.int)
    maskC=np.array([[-1,0,0],
                    [0,1,0],
                    [0,0,0]],dtype=np.int)
    return calGrad_mask(img, maskR, maskC)

def prewit(img):
    maskR=np.array([[1,0,-1],
                    [1,0,-1],
                    [1,0,-1]],dtype=np.int)
    maskC=np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]],dtype=np.int)
    return calGrad_mask(img, maskR, maskC)

def sobel(img):
    maskR=np.array([[1,0,-1],
                    [2,0,-2],
                    [1,0,-1]],dtype=np.int)
    maskC=np.array([[-1,-2,-1],
                    [0,0,0],
                    [1,2,1]],dtype=np.int)
    return calGrad_mask(img, maskR, maskC)

def freichen(img):
    maskR=np.array([[1,0,-1],
                    [np.sqrt(2),0,-np.sqrt(2)],
                    [1,0,-1]],dtype=np.float)
    maskC=np.array([[-1,-np.sqrt(2),-1],
                    [0,0,0],
                    [1,np.sqrt(2),1]],dtype=np.int)
    return calGrad_mask(img, maskR, maskC)
                     
if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out_robots=robots(Image)
    out_prewit=prewit(Image)
    out_sobel=sobel(Image)
    out_freichen=freichen(Image)
    showNImage(Image, out_robots, out_prewit, out_sobel, out_freichen)
