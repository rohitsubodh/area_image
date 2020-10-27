import numpy as np
from PIL import Image
width=5
height=4
array=np.zeros([height,width,3],dtype=np.uint8)# here 3 represent byte value for rgb and 3 also known as blue factor
#dtype is used to create matrix dimension(dtype=datatype,uint=unsigned int )
#each pixel contain 3 byte values for rgb
#each byte represent color
img=Image.fromarray(array)
img.save('image1.png')
array1=np.ones([100,200,3],dtype=np.uint8)
array1[:,:100]=[255,198,100] #orange color
array1[:,100:]=[0,110,255]   #blue color
img=Image.fromarray(array1)
img.save('image2.png')



#np.zeros?