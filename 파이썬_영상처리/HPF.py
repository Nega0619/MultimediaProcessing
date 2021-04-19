import numpy as np
from util import *
from equalization import *

def HPF(img, fsize):
    img_eq=meanFilter(img, fsize)
    diff=img-img_eq
    diff=np.absolute(diff)
    result=np.clip(diff,0,255)
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    fsize=int(input('input filter size : '))
    out=HPF(Image, fsize)
    showNImage(Image, out)
