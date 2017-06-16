import os
import re

data_path='/data4/szhou/HuDaAct/data/'
all_list='./all.txt'
img_list='./img_all.txt'
depth_list='./depth_all.txt'


file_all=open(all_list,'w')
file_img=open(img_list,'w')
file_depth=open(depth_list,'w')

dirs= os.listdir(data_path)

regimg=re.compile(r'img.avi')
regdepth=re.compile(r'depth.avi')

for dir in dirs:
    files=os.listdir(os.path.join(data_path,dir))
    for file in files:
        file_all.write(os.path.join(data_path,dir,file))
        file_all.write('\n')
        if re.findall(regimg,file):
            file_img.write(os.path.join(data_path,dir,file))
            file_img.write('\n')
        if re.findall(regdepth,file):
            file_depth.write(os.path.join(data_path,dir,file))
            file_depth.write('\n')


file_all.close()
file_img.close()
file_depth.close()

