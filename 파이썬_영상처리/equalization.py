import numpy as np
from util import *
from maskop import *
import scipy.stats as st

def meanFilter(img, fsize):
    mask=np.full((fsize,fsize),1,dtype=np.int)
    out=mask_op(img, mask)
    return out

def gaussianFilter3x3(img):
    mask=np.array([[1,2,1],
                   [2,4,2],
                   [1,2,1]],dtype=np.int)
    out=mask_op(img, mask)
    return out

def gaussianMGen(kernlen, nsig=3):
    """Returns a 2D Gaussian kernel."""

    x = np.linspace(-nsig, nsig, kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d, kern1d)
    return kern2d/kern2d.sum()

def gaussianFilter(img, fsize):
    mask=gaussianMGen(fsize)
    out=mask_op(img, mask)
    return out

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    fsize=int(input('input filter size : '))
    out=gaussianFilter(Image, fsize)
    showNImage(Image, out)
