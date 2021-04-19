import numpy as np
from util import *
    
def binarization_step(image):
    result=image.copy()
    result[image<100]=0
    result[(image>=100) & (image>150)]=50
    result[(image>=150) & (image>200)]=150
    result[image>=200]=255
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out=binarization_step(Image)
    show2Image(Image, out)
    
