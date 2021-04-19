import numpy as np
from util import *
from max_min_medi import *

#침식과 팽창 연산은 각각 최소, 최대 필터 연산과 같음
def erosion_gray(img, ksize):
    return minFilter(img, ksize)

def dilation_gray(img, ksize):
    return maxFilter(img, ksize)

def open_gray(img, ksize):
    after=dilation_gray(erosion_gray(img,ksize),ksize)
    return after

def close_gray(img, ksize):
    after=erosion_gray(dilation_gray(img,ksize),ksize)
    return after

def smoothing_morphology(img, ksize):
    result=open_gray(img, ksize)
    result=close_gray(result, ksize)
    return result

def detection_edge_morphology(img, ksize, n):
    img_dil=dilation_gray(img,ksize)
    img_ero=img.copy()
    #n번의 침식 수행
    for i in range(n):
        img_ero=erosion_gray(img_ero, ksize)
    diff=img_dil-img_ero
    #클리핑
    diff=np.clip(diff,0,255)
    return diff

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out1=detection_edge_morphology(Image, 3, 1)
    out2=detection_edge_morphology(Image, 3, 3)
    showNImage(Image, out1, out2)
