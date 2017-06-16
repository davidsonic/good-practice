import numpy as np



count=0
with open('test_ground_truth.txt','r') as fg:
    with open('predict_result.txt','r') as fr:
        gts=fg.readlines()
        rs=fr.readlines()
        total=len(gts)
        i=0
        for gt in gts:
            gt=gt.split(' ')[1]
            r=rs[i].split(' ')[1]
            print 'gt:{}  result:{}'.format(gt,r)

            if r==gt:
                count+=1
            i+=1
        print count
        print count/(1.0*total)



