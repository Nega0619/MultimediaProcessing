import numpy as np
from util import *
    
def binarization_highlow(image, low, high):
    result=image.copy()
    result[image<low]=0
    # 조건 인덱싱에서 조건의 결합은 각 조건문을 괄호로 감싸고
    # & 이나 | 를 써서 결합함
    result[(image>=low) & (image>high)]=255
    result[image>=high]=0
    return result

if __name__ == '__main__':
    path=load_gui()
    Image=readImage(path)
    low=int(input('Input Low threshold : '))
    high=int(input('Input High threshold : '))
    out=binarization_highlow(Image, low, high)

    show2Image(Image, out)
    
