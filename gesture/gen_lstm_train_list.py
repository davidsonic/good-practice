data_path='/data4/jiali/data/iso_train'

import os



count=1
lstm1=0
lstm2=1

if lstm1:

    dirs=os.listdir(data_path)
    fimg=open('lstm_rgb_list.txt','w')
    # fflow=open('lstm_flow.list.txt','w')

    for dir in dirs:
        files=os.listdir(os.path.join(data_path,dir))
        for file in files:
            count+=1
            if count %10000==0:
                print '{} files processed'.format(count)

            if file.startswith('img'):
                fimg.write(os.path.join(data_path,dir,file))


if lstm2:
    with open('test_rgb_list.txt','r') as fr:
        with open('test_lstm_rgb_list.txt','w') as fw:
            lines=fr.readlines()
            for line in lines:
                count+=1
                label=line.split(' ')[1]
                # path=line.split(' ')[0].split('/')[-1]
                tmp=os.path.join('/home/duanjiali/data/IsoGD/',line.split(' ')[0])
                fw.write(tmp+' '+str(label))
                if count %1000==0:
                    print '{} files procesed'.format(count)

