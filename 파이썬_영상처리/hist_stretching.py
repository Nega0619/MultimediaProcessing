import numpy as np
from util import *
from histogram import *

def hist_stretching(img):
    img2=img.astype(np.float)
    low=np.min(img)
    high=np.max(img)
    result=(img2-low)*255/(high-low)
    result=result.astype(np.int)
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    hist=histogram(Image)
    out=hist_stretching(Image)
    out_hist=histogram(out)
    showhist(Image,hist)
    showhist(out,out_hist)
    
    
