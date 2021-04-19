import numpy as np
from util import *

def translation(img, transPos):
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    for i in range(image_size):
        for j in range(image_size):
            X=i+transPos[0]
            Y=j+transPos[1]
            #처리 후 좌표 검사
            if(X<0 or Y<0 or X>=image_size or Y>=image_size):
                continue
            result[X, Y]=img[i,j]
    return result

def scaling_forward(img, s):
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    for i in range(image_size):
        for j in range(image_size):
            X=int(i*s)
            Y=int(j*s)
            if(X<0 or Y<0 or X>=image_size or Y>=image_size):
                continue
            result[X, Y]=img[i,j]
    return result
def scaling_backward(img, s):
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    for i in range(image_size):
        for j in range(image_size):
            x=i//s
            y=j//s
            if(x<0 or y<0 or x>=image_size or y>=image_size):
                continue
            result[i,j]=img[x,y]
    return result

def scaling_bilinear(img, s):
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    for i in range(image_size):
        for j in range(image_size):
            #실수 좌표
            x_f=i/s
            y_f=j/s
            #범위 검사식 수정
            if(x_f<0 or y_f<0 or x_f>=image_size-1 or y_f>=image_size-1):
                continue
            #정수 좌표
            x_i=i//s
            y_i=j//s
            #좌표 소수부 
            x_alpha=x_f-x_i
            y_alpha=y_f-y_i
            #보간된 화소값 계산 
            p = img[x_i, y_i]*(1-x_alpha)*(1-y_alpha)
            p += img[x_i+1, y_i]*x_alpha*(1-y_alpha)
            p += img[x_i, y_i+1]*(1-x_alpha)*y_alpha
            p += img[x_i, y_i+1]*x_alpha*y_alpha
            #반올림
            p=np.round(p)
            #계산된 화소값을 출력 영상에 저장
            result[i,j]=int(p)
    return result


def rotation(img, theta):
    #numpy 함수는 radian을 입력받으므로
    #degree로 입력된 회전각을 변환 
    rad=np.deg2rad(theta)
    result=np.zeros(img.shape,dtype=np.int)
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
    result=np.zeros((nH,nW),dtype=np.int)
    #변환된 이미지 크기의 중앙
    cX=nH//2
    cY=nW//2
    cx=image_size//2
    cy=image_size//2
    for i in range(nH):
        for j in range(nW):
            X=i-cX
            Y=(nW-j)-cY
            x=X*np.cos(rad)+((Y)*np.sin(rad))+cx
            y=-(Y)*np.cos(rad)+X*np.sin(rad)+cy
            x=int(x)
            y=int(y)
            if(x<0 or y<0 or x>=image_size or y>=image_size):
                continue
            result[i,j]=img[x,y]
    return result

def mirror(img, types):
    mir_x=False
    mir_y=False
    mir_d=False
    types=types.lower()
    if types=='x':
        mir_x=True
    elif types=='y':
        mir_y=True
    elif types=='o':
        mir_x=True
        mir_y=True
    elif types=='d':
        mir_d=True
        
    result=np.zeros(img.shape,dtype=np.int)
    image_size=img.shape[0]
    cx=image_size//2
    cy=image_size//2 
    for i in range(image_size):
        for j in range(image_size):
            x=i-cx
            y=(image_size-j)-cy
            X=i
            Y=j
            if(mir_x):
                X=-x+cx
            if(mir_y):
                Y=y+cy
            if(mir_d):
                X=y+cx
                Y=x+cy
            #처리 후 좌표 검사
            if(X<0 or Y<0 or X>=image_size or Y>=image_size):
                continue
            result[X, Y]=img[i,j]
    return result

            
if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out=scaling_forward(Image,2)
    out2=scaling_backward(Image,2)
    out3=scaling_bilinear(Image,2)
    showNImage(Image,None,None,out,out2,out3)

    #out=translation(Image,(100,0))
    #out=rotation(Image,60)
    #out2=rotation2(Image,60)
    #out=mirror(Image,'d')

    #out=scaling_for(Image,2)
    #out2=scaling_back(Image,2)
    #showNImage(Image, out, out2)
