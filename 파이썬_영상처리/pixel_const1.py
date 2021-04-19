import numpy as np
from util import *
    
def constAdd(image, value):
    result=image.copy()
    for i in range(256):
        for j in range(256):
            t=int(image[i,j])+value
            if (t>255): t=255
            if (t<0): t=0
            result[i,j]=t
    return result

def constSub(image,value):
    result=image.copy()
    for i in range(256):
        for j in range(256):
            t=int(image[i,j])-value
            if (t>255): t=255
            if (t<0): t=0
            result[i,j]=t
    return result

def constMul(image,value):
    result=image.copy()
    for i in range(256):
        for j in range(256):
            t=int(image[i,j])*value
            if (t>255): t=255
            if (t<0): t=0
            result[i,j]=t
    return result

def constDiv(image,value):
    result=image.copy()
    for i in range(256):
        for j in range(256):
            t=int(image[i,j])/value
            if (t>255): t=255
            if (t<0): t=0
            result[i,j]=t
    return result    


if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    t=int(input('choose one number, 1.add, 2.subtract, 3.multiple, 4.division : '))
    value=int(input('Input Value : '))
    if(t==1):
        out=constAdd(Image, value)
    elif(t==2):
        out=constSub(Image, value)
    elif(t==3):
        out=constMul(Image, value)
    elif(t==4):
        out=constDiv(Image, value)

    show2Image(Image, out)
    
