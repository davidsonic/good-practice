import os

datapath='/data4/jiali/data/iso_test_depth/'

# ori_count=0
# count=0
# dirs=os.listdir(datapath)
# dir_num=len(dirs)
# for dir in dirs:
#     files=os.listdir(os.path.join(datapath,dir))
#     ori_count+=1
#     if len(files)==0:
#         os.rmdir(os.path.join(datapath,dir))
#         count+=1
#         print('dir {} deleted '.format(dir))
#
#     if ori_count%1000==0:
#         print '{} files processed'.format(ori_count)
#
# print("{} dirs deleted".format(count))
# print ("{} dirs remained".format(dir_num-count))


# count=1
# with open('./train_rgb_list.txt','r') as fo:
#     with open('./train_rgb_list2.txt','w') as f:
#         lo=fo.readlines()
#         for i in range(len(lo)):
#             count+=1
#             tmp=lo[i].strip().split(' ')[0]
#             dir=tmp.split('/')[-1].split('.')[0]
#             if os.path.exists(os.path.join(datapath,dir)):
#                 f.write(lo[i])
#             if count%1000==0:
#                 print '{} files processed'.format(count)

