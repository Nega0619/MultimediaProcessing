import numpy as np
from util import *
from scipy import signal

#no padding
def mask_op(image, mask):
    result=np.zeros(image.shape,dtype=np.float)
    image_size=image.shape[0]
    mask_size=mask.shape[0]
    t=mask_size//2
    if(mask.sum()!=0):
        w=mask.sum()
    else:
        w=1
    for i in range(t,image_size-t):
        for j in range(t,image_size-t):
            block=image[i-t:i+t+1,j-t:j+t+1]
            r=np.sum(block*mask)//w
            result[i,j]=r
    result=np.clip(result,0,255)
    return result

def mask_scipy(image, mask, weight=1):
    result=np.zeros(image.shape,dtype=np.float)
    mask_size=mask.shape[0]
    t=mask_size//2
    if(mask.sum!=0):
        w=mask.sum
    else:
        w=1
    mask = np.flipud(np.fliplr(mask))
    tmp=signal.convolve2d(image, mask, mode='valid')
    tmp=tmp/w
    result[t:-t,t:-t]=tmp
    result=np.clip(result,0,255)
    return result


if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    mask=np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1]],dtype=np.int16)
    out=mask_op(Image,mask)
    showNImage(Image, out)
    
