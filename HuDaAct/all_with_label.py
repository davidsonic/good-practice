import os
import re

all_list='./all.txt'
img_list='./img_all.txt'
depth_list='./depth_all.txt'
train_list='./train.txt'
test_list='./test.txt'
train_depth='./train_depth.txt'
test_depth='./test_depth.txt'

file_all=open('test.txt','r')
file_all_label=open('test_with_label.txt','w')

lines=file_all.readlines()

for line in lines:
    flag=line.split('-')[0][-1]
    if flag=='G' or flag=='B':
        file_all_label.write(line[:-1] + ' ' + str(12) + '\n')
    else:
        tmp=line.split('-')[0][-2]
        if tmp =='E':
            file_all_label.write(line[:-1]+' '+str(0)+'\n')
        elif tmp=='P':
            file_all_label.write(line[:-1]+' '+str(1)+'\n')
        elif tmp=='G':
            file_all_label.write(line[:-1]+' '+str(2)+'\n')
        elif tmp=='B':
            file_all_label.write(line[:-1]+' '+str(3)+'\n')
        elif tmp=='I':
            file_all_label.write(line[:-1]+' '+str(4)+'\n')
        elif tmp=='O':
            file_all_label.write(line[:-1]+' '+str(5)+'\n')
        elif tmp=='T':
            file_all_label.write(line[:-1]+' '+str(6)+'\n')
        elif tmp == 'M':
            file_all_label.write(line[:-1] + ' ' + str(7) + '\n')
        elif tmp == 'D':
            file_all_label.write(line[:-1] + ' ' + str(8) + '\n')
        elif tmp == 'K':
            file_all_label.write(line[:-1] + ' ' + str(9) + '\n')
        elif tmp == 'L':
            file_all_label.write(line[:-1] + ' ' + str(10) + '\n')
        elif tmp == 'N':
            file_all_label.write(line[:-1] + ' ' + str(11) + '\n')
