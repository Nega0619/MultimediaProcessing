import numpy as np
from util import *
from binarization import *
from scipy.ndimage import label as scipy_label

def label_grassfire(img):
    image_size=img.shape[0]
    label=np.zeros(img.shape,dtype=int)
    bimg=img.astype(np.bool)
    labelNo=0
    for i in range(image_size):
        for j in range(image_size):
            #만약 라벨링이 안된 이웃한 화소가 발견되면
            if(bimg[i,j]==True and label[i,j]==0):
                labelNo+=1
                label[i,j]=labelNo
                #grassfire 수행
                grassfire(bimg,label,labelNo,i,j)
    return label

def grassfire(img,label,labelNo, posX,posY):
    #8방향
    # 3 4 5
    # 2 X 6
    # 1 8 7
    #순서로 탐색을 수행
    image_size=img.shape[0]
    findX=[1,0,-1,-1,-1,0,1,1]
    findY=[-1,-1,-1,0,1,1,1,0]
    #큐를 통해 구현
    #(재귀 함수를 통해 구현하면 stack over flow 발생)
    queue=[(posX,posY)]
    while(len(queue)!=0):
        #맨 마지막 원소를 꺼냄
        x,y=queue.pop(-1)
        for fx, fy in zip(findX, findY):
            X=x+fx
            Y=y+fy
            #좌표 범위 체크
            if(X<0 or Y<0 or X>=image_size or Y>image_size):
                continue
            #만약 라벨링이 안된 이웃한 화소가 발견되면
            if(img[X,Y]==True and label[X,Y]==0):
                #번호를 붙여줌
                label[X,Y]=labelNo
                #큐에 추가
                queue.append((X,Y))
                #아래를 통해 구현할수도 있지만,
                #객체의 크기가 크면 overflow 발생
                #grassfire(img,label,labelNo,X,Y)

def label_twopass(img):
    bimg=img.astype(np.bool)
    #첫번째 탐색
    label, labtab=twopass_first(bimg)
    #두번째 탐색
    for i in range(1,len(labtab)):
        labidx=i
        while(labidx!=labtab[labidx]):
            labidx=labtab[labidx]
        labtab[i]=labidx
    #새로운 테이블 생성
    #목적 : 순차적인 라벨링 번호 붙이기
    labNo={}
    labNoCount=0
    for i in range(1,len(labtab)):
        if(i==labtab[i]):
            labNoCount+=1
            labNo[i]=labNoCount
    for i in range(1,len(labtab)):
        label[label==i]=labNo[labtab[i]]
    return label      
        
def twopass_first(img):
    label=np.zeros(img.shape,dtype=int)
    image_size=img.shape[0]
    #8방향일 때
    # 2 3 4
    # 1 X -
    # - - -
    #순서로 탐색을 수행
    labelNo=0
    findX=[0,-1,-1,-1]
    findY=[-1,-1,0,1]
    labTab=[-1]
    for i in range(image_size):
        for j in range(image_size):
            if img[i,j]==True:
                #집합자료형
                findLabel=set()
                for fx, fy in zip(findX, findY):
                    X=i+fx
                    Y=j+fy
                    #좌표 범위 체크
                    if(X<0 or Y<0 or X>=image_size or Y>image_size):
                        continue
                    #주위의 라벨을 찾으면
                    if (label[X,Y]!=0):
                        findLabel.add(label[X,Y])
                #주변에 라벨이 없으면
                if(len(findLabel)==0):
                    labelNo+=1
                    #라벨링
                    label[i,j]=labelNo
                    #라벨링테이블 추가
                    labTab.append(labelNo)
                    continue
                minLab=min(findLabel)
                label[i,j]=minLab
                for labno in findLabel:
                    labTab[labno]=min(labTab[labno],minLab)
    return label, labTab

def label_scipy(bimg):
    kernel=np.full((3,3),True,dtype=np.bool)
    label,num_label=scipy_label(bimg,kernel)
    return label

def showLabel(oriImg, bImg, labelimg, *imgs):
    showL=labelimg.copy()
    num_label=labelimg.max()
    step=255//num_label
    showL=showL*step
    showNImage(oriImg,bimg,showL, *imgs)

def selectObject(oriImg, labelimg, selectNo):
    objImg=oriImg.copy()
    objImg[labelimg!=selectNo]=0
    return objImg

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    bimg=binarization(Image,80)
    labelimg=label_scipy(bimg)
    showLabel(Image, bimg, labelimg)
    
