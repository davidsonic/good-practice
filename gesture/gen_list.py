import os

work_root='/data3/gesture/IsoGD_files/IsoGD/'
train_list='train_list.txt'
test_list ='test_list_with_label.txt'

# val_list='valid_list_with_label.txt'
#
# work_root='/data3/gesture/IsoGD_files/IsoGD_phase_2/'
# test_list='test_list.txt'

# work_root='./'
# test_list='iso_phase2_test_gt.txt'

# with open(os.path.join(work_root,test_list)) as f:
#     test_file=f.readlines()
#     num_samples3=len(test_file)
#     test=[]
#     for i in range(num_samples3):
#         line=test_file[i].split(' ')
#         file_name=line[0]
#         test.append(file_name)
#     print 'test_file {} generated'.format('rgb')

with open(os.path.join(work_root,test_list)) as f:
    train_file=f.readlines()
    num_samples4=len(train_file)
    test=[]
    for i in range(num_samples4):
        line=train_file[i].split(' ')
        file_name=line[1]
        label=line[2]
        test.append(file_name+' '+label)
    print 'test_file {} generated'.format('rgb')


with open(os.path.join(work_root,train_list)) as f:
    train_file=f.readlines()
    num_samples1=len(train_file)
    train=[]
    for i in range(num_samples1):
        line=train_file[i].split(' ')
        file_name=line[1]
        label=line[2]
        train.append(file_name+' '+label)
    print 'train_file {} generated'.format('rgb')
#
#
# with open(os.path.join(work_root,val_list)) as f:
#     val_file=f.readlines()
#     num_samples2=len(val_file)
#     val=[]
#     for i in range(num_samples2):
#         line=val_file[i].split(' ')
#         file_name=line[0]
#         label=line[2]
#         val.append(file_name+' '+label)
#     print 'val_file {} generated'.format('rgb')


store_root='./'


with open(os.path.join(store_root,'train_depth_list.txt'),'w') as f:
    for i in range(num_samples1):
        f.write(train[i])
#
# with open(os.path.join(store_root,'iso_phase_2_test_rgb_list.txt'),'w') as f:
#     for i in range(num_samples3):
#         f.write(test[i])
#         f.write('\n')

with open(os.path.join(store_root,'test_depth_list.txt'),'w') as f:
    for i in range(num_samples4):
        f.write(test[i])

