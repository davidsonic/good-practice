import numpy as np
import time
import os
from skimage import io
import sys
sys.path.insert(0,'/data4/jiali/good-practice/lib/caffe-action/python')

from caffe.io import array_to_blobproto

datapath='/data4/jiali/data/iso_train_depth/'

mean=np.zeros((1,3,240,320))

N=0
exts=["jpg","png"]

beginTime=time.time()

for subdir,dirs,files in os.walk(datapath):
    for dir in dirs:
        files=os.listdir(os.path.join(subdir,dir))
        for file in files:
            if file.startswith('img',0,len(file)):
                img = io.imread(os.path.join(subdir, dir,file))
                # print img.shape  ## shape is height*widht*3
                mean[0][0] += img[:, :, 0]  #R
                mean[0][1] += img[:, :, 1]  #G
                mean[0][2] += img[:, :, 2]  #B
                N += 1
                if N % 1000 == 0:
                    elapsed = time.time() - beginTime
                    print(
                    "Processed {} images in {:.2f} seconds." "{:.2f} images/second".format(N, elapsed, N / elapsed))

mean[0]/=N
print mean[0]

blob=array_to_blobproto(mean)
with open("{}.binaryproto".format('gesture'),'wb') as f:
    f.write(blob.SerializeToString())

np.save("{}.npy".format('gesture'),mean[0])


