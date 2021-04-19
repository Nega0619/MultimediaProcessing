import numpy as np
from util import *

def inter_avg(block):
    b2=block.astype(float)
    #빈 공간을 계산하지 않기 위해
    b2[b2==0]=np.nan
    return np.nanmean(b2)

def inter_median(block):
    b2=block.astype(float)
    b2[b2==0]=np.nan
    return np.nanmedian(b2)    

#해당 화소를 둘러싼 2x2 블록, 소수점 좌표를 함수의 인자로 받아들임
def inter_bilinear(block, subPxPos):
    alphaX=subPxPos[0]
    alphaY=subPxPos[1]
    p=block[0,0]*(1-alphaX)*(1-alphaY)+
      block[0,1]*(1-alphaX)*alphaY+
      block[1,0]*alphaX*(1-alphaY)+
      block[1,1]*alphaX*alphaY
    return p

def scaling_back(img, s):
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    for i in range(image_size):
        for j in range(image_size):
            x=i/s
            y=j/s
            if(x<0 or y<0 or x>=image_size or y>=image_size):
                continue
            if(x>=image_size-1 or y>=image_size-1):
                result[i,j]=img[i//s,y//s]
            else:
                i,j
                p=inter_bilinear(img[int(x):int(x)+2,int(y):int(y)+2])
            
    return result
