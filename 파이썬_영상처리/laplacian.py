import numpy as np
from util import *
from maskop import *

def laplacian_4(img):
    mask=np.array([[0,1,0],
                   [1,-4,1],
                   [0,1,0]],dtype=np.int)
    return mask_op(img, mask)

def laplacian_8(img):
    mask=np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]],dtype=np.int)
    return mask_op(img, mask)

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out_4=laplacian_4(Image)
    out_8=laplacian_8(Image)
    showNImage(Image, out_4, out_8)
