import numpy as np
from util import *
    
def imgAdd(image1,image2):
    result=image1.copy()
    result=image1+image2
    result=np.clip(result,0,255)
    return result

def imgSub(image1, image2):
    result=image1.copy()
    result=image1-value
    result=np.clip(result,0,255)
    return result

def imgMul(image1, image2):
    result=image2.copy()
    #float로 자료형 변경
    result=result.astype(np.float)
    #결과 범위를 0~255로 일치시키기 위해
    result=image1*(result/255)
    #result=result/255
    result=np.clip(result,0,255)
    return result

def imgDiv(image1, image2):
    result=image2.copy()
    #float로 자료형 변경
    result=result.astype(np.float)
    #0으로 나누는거 방지
    result[image2==0]=1
    result=image1/result
    #나뉘는 값이 0이면 255로 설정
    result[image2==0]=1
    #결과 범위를 0~255로 일치시키기 위해
    result=result*255
    #원래 자료형으로 변경
    result=result.astype(np.int16)
    result=np.clip(result,0,255)
    return result

if __name__ == '__main__':
    path=load_gui()
    Image1=readImage(path)
    path=load_gui()
    Image2=readImage(path)
    t=int(input('choose one number, 1.add, 2.subtract, 3.multiple, 4.division : '))
    if(t==1):
        out=imgAdd(Image1, Image2)
    elif(t==2):
        out=imgSub(Image1, Image2)
    elif(t==3):
        out=imgMul(Image1, Image2)
    elif(t==4):
        out=imgDiv(Image1, Image2)

    show3Image(Image1, Image2, out)
    
