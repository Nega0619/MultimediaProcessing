import numpy as np
from util import *
from histogram import *

def hist_equalization(img, hist):
    result=np.zeros(img.shape,dtype=np.float)
    cumsum_hist=np.cumsum(hist,dtype=np.float) #누적합 계산
    G_max=255 #최대 화소 값
    N_t=img.size #전체 화소 개수
    hist_norm=cumsum_hist*(G_max/N_t)
    hist_norm=np.round(hist_norm).astype(np.int)
    result=hist_norm[img]
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    hist=histogram(Image)
    showhist(Image,hist)
    out=hist_equalization(Image,hist)
    outhist=histogram(out)
    showhist(out,outhist)
    
