import numpy as np
from util import *
    
def binarization(image, threshold):
    result=image.copy()
    result[image<threshold]=0
    result[image>=threshold]=255
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    value=int(input('Input Threshold value to binarization : '))
    out=binarization(Image, value)

    showNImage(Image, out)
    
