# ftrain=open('test_depth.txt','r')
#
# train=ftrain.readlines()
# save_path='/data4/jiali/data/new-data-test'
#
# import os
# import shutil
#
# if not os.path.exists(save_path):
#     os.makedirs(save_path)
#
# count=0
# for file in train:
#     file_path=file.split(' ')[0]
#     tmp=file_path.split('/')
#     if not os.path.exists(os.path.join(save_path,tmp[-2])):
#         os.makedirs(os.path.join(save_path,tmp[-2]))
#     shutil.copyfile(file[:-1],os.path.join(save_path,tmp[-2],tmp[-1]))
#     count+=1
#     if count %200==0:
#         print '{} files done'.format(count)



# ftrain=open('test.txt','r')
# ftrain2=open('test2.txt','w')
#
# for line in ftrain:
#     depth=line.replace('img','depth')
#     ftrain2.write(line)
#     ftrain2.write(depth)
#
# ftrain2.close()
# ftrain.close()


# import re
#
# ftrain_img=open('train_depth_label.txt','w')
# ftrain=open('train_with_label.txt','r')
#
# lines = ftrain.readlines()
# for line in lines:
#     if re.findall(r'depth',line):
#         ftrain_img.write(line)
#
# ftrain_img.close()
# ftrain.close()


fout=open('HuDa_depth_output.txt','w')

for i in range(1,494):
    path='data/32f_depth_test_fc8/%05d' % i
    fout.write(path+'\n')

