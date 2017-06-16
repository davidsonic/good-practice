


with open('predict_result.txt','r') as fr:
    with open('predict_result_origin.txt','w') as fo:
        lines=fr.readlines()
        num=len(lines)

        count=0

        for line in lines:
            vid=line.split(' ')[0]
            label=line.split(' ')[1]

            count+=1

            if count%200==0:
                tmp=count/200-1
            else:
                tmp=count/200

            dir_num='%03d' % (tmp+1)
            form = 'test/' + str(dir_num)+'/'

            fo.write('{} {} {}'.format(form+'M_'+vid+'.avi',form+'K_'+vid+'.avi',label))
