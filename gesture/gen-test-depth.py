with open('test_rgb_list.txt') as f:
    f1=open('test_depth_list.txt','w')
    lists=f.readlines()

    for line in lists:
        arr=line.split('/')
        file=arr[2].replace('M','K')
        newline=arr[0]+'/'+arr[1]+'/'+file
        f1.write(newline)


    f1.close()

