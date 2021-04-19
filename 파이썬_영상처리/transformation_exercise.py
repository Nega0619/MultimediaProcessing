import numpy as np
from util import *

def rotation(img, theta):
    #numpy 함수는 radian을 입력받으므로
    #degree로 입력된 회전각을 변환 
    rad=np.deg2rad(theta)
    result=np.full(img.shape,255,dtype=np.int)
    image_size=img.shape[0]
    #영상의 중심 좌표
    cx=image_size//2
    cy=image_size//2
    for i in range(image_size):
        for j in range(image_size):
            #영상 중앙으로 좌표계 이동
            #x축은 수학적 좌표계의 방향과 다르기 때문에 방향을 일치시켜줌
            X=image_size-i-cx
            Y=j-cy
            x=cx-X*np.cos(rad)+((Y)*np.sin(rad))
            y=(Y)*np.cos(rad)+X*np.sin(rad)+cy
            x=int(x)
            y=int(y)
            if(x<0 or y<0 or x>=image_size or y>=image_size):
                continue
            result[i,j]=img[x,y]
    return result

def rotation_adaptive(img, theta):
    rad=np.deg2rad(theta)    
    image_size=img.shape[0]
    #변환 후 이미지 크기 계산
    nW=image_size*np.cos(np.deg2rad(90-theta))+image_size*np.cos(rad)
    nH=image_size*np.cos(rad)+image_size*np.cos(np.deg2rad(90-theta))
    nW=int(nW)
    nH=int(nH)
    result=np.full((nH,nW),255,dtype=np.int)
    #변환된 이미지 크기의 중앙
    cX=nH//2
    cY=nW//2
    cx=image_size//2
    cy=image_size//2
    for i in range(nH):
        for j in range(nW):
            X=i-cX
            Y=(nW-j)-cY
            x=X*np.cos(270-rad)+((Y)*np.sin(270-rad))+cx
            y=-(Y)*np.cos(270-rad)+X*np.sin(270-rad)+cy
            x=int(x)
            y=int(y)
            if(x<0 or y<0 or x>=image_size or y>=image_size):
                continue
            result[i,j]=img[x,y]
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    midImage=rotation(Image,30)
    out=rotation_adaptive(Image,30)
    
    showNImage(Image, midImage, out)
    #out=translation(Image,(100,0))
    #out=rotation(Image,60)
    #out2=rotation2(Image,60)
    #out=mirror(Image,'d')

    #out=scaling_for(Image,2)
    #out2=scaling_back(Image,2)
    #showNImage(Image, out, out2)

