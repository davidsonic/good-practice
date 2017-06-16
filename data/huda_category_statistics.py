import numpy as np

file='huda_rgb_train_split_1.txt'
file=open(file)

lines=file.readlines()

category_count={}
for line in  lines:
    line=line.strip().split(' ')
    category=line[-1]
    count=int(line[1])
    if category not in category_count:
        vec=[]
        vec.append(count)
        category_count[category]=vec
    else:
        category_count[category].append(count)


for k,v in category_count.items():
    category_count[k]=(
        max(category_count[k]),
        min(category_count[k]),
        np.mean(category_count[k]),
        np.std(category_count[k])
    )



import matplotlib as mpl
import matplotlib.pyplot as plt

names=('max','min','mean','std')
new_dict=[category_count[k] for k in sorted(category_count.keys(),cmp=lambda x,y: cmp(int(x),int(y) ))]
print new_dict

max_val=[item[0] for item in new_dict]
min_val=[item[1] for item in new_dict]
mean_val=[item[2] for item in new_dict]
std_val=[item[3] for item in new_dict]

bar_width=0.35

index=np.arange(13)
rects1=plt.bar(index,max_val,bar_width, color='#0072BC',label='max')
rects2=plt.bar(index+bar_width,min_val,bar_width,color='#ED12C4',label='min')
rects3=plt.bar(index+bar_width*2,mean_val,bar_width,color='green',label='mean')
# rects4=plt.bar(index+bar_width*3,std_val,bar_width,color='yellow',label='std')

# def add_labels(rects):
#     for rect in rects:
#         height=rect.get_height()
#         # plt.text(rect.get_x()+rect.get_width()/2,height,height,ha='center',va='bottom')
#         rect.set_edgecolor('white')
#
# add_labels(rects1)
# add_labels(rects2)
# add_labels(rects3)
# add_labels(rects4)


plt.xticks(index,index)
plt.ylim(ymax=2000,ymin=0)
plt.title('Variration statistics for 13 action categories in RGB-D HuDaAct')
plt.legend(loc='upper center',ncol=4)

plt.savefig('Statistics for 13 action categories in RGB-D HuDaAct.png')
# plt.show()


