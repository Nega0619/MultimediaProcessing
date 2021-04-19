import numpy as np
from util import *
from histogram import *
from binarization import *

def otsu_binarization(img):
    #입력 영상의 히스토그램 계산
    hist=histogram(Image)
    tmp=np.arange(0,256,1)
    #0-255의 임계치 범위에서의 두 그룹의 분산 합을
    #저장함 (초기 값은 무한대로 설정)
    wvar=np.full(256,np.inf,dtype=np.float)
    #영상 내 0~255의 화소 값에 대해 빈도와 화소 값을 곱함
    wp=hist*tmp
    #영상 내 0~255의 화소 값에 대해 빈도와 화소 값의 제곱을 곱함
    wp2=hist*np.power(tmp,2)
    #1~254의 임계치를 탐색
    for i in range(1,255):
        s1=np.sum(hist[:i])
        s2=np.sum(hist[i:])
        #배경이 검출되지 않았을 경우
        #다음 임계치를 탐색
        if(s1==0): continue
        #객체가 검출되지 않았을 경우
        #for문 종료
        if(s2==0): break
        #각 그룹에서의 표본값의 평균
        m1=np.sum(wp[:i])/s1
        m2=np.sum(wp[i:])/s2
        #각 그룹에서의 표본값의 제곱의 평균
        sm1=np.sum(wp2[:i])/s1
        sm2=np.sum(wp2[i:])/s2
        #분산 계산
        var1=sm1-np.power(m1,2)
        var2=sm2-np.power(m2,2)
        #각 그룹의 분산에 각 그룹에 속한 화소수로
        #가중치를 주어 더함으로써 해당 임계치의 분산을
        #계산
        wvar[i]=var1*s1+var2*s2
    #argmin : wvar 배열의 값이 최소가 될때의 index를 구함
    T=np.argmin(wvar)
    print("임계치 : "+str(T))
    #계산된 임계치로 이진화
    return binarization(img, T)

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    out=otsu_binarization(Image)
    showNImage(Image, out)
    
