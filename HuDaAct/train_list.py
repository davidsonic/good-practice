import os
import re

data_path='/data4/szhou/HuDaAct/data/'
all_list='./all.txt'
img_list='./img_all.txt'
depth_list='./depth_all.txt'

file_img=open(img_list,'r')

files=file_img.readlines()

dic=['E','P','G','B','I','O','T','M','D','K','L','N','BG']

# user=open('USER18.txt','w')
#
# for file in files:
#     for i in range(1,31):
#         regex=r'USER_'+str(i)+'/'
#         for j in dic:
#             if re.findall(regex+'.*'+j+'1',file):
#                 user.write(file)

# mE=open('E.txt','w')
# mP=open('P.txt','w')
# mG=open('G.txt','w')
# mB=open('B.txt','w')
# mI=open('I.txt','w')
# mP=open('O.txt','w')
# mP=open('T.txt','w')
# mP=open('M.txt','w')
# mP=open('D.txt','w')
# mP=open('K.txt','w')
# mP=open('L.txt','w')
# mP=open('N.txt','w')

mE=[]
mP=[]
mG=[]
mB=[]
mI=[]
mO=[]
mT=[]
mM=[]
mD=[]
mK=[]
mL=[]
mN=[]
mBG=[]

for file in files:
    if re.findall(r'_E\d?',file):
        mE.append(file)
    elif re.findall(r'_P\d?',file):
        mP.append(file)
    elif re.findall(r'_G\d?',file):
        mG.append(file)
    elif re.findall(r'_B\d?',file):
        mB.append(file)
    elif re.findall(r'_I\d?',file):
        mI.append(file)
    elif re.findall(r'_O\d?',file):
        mO.append(file)
    elif re.findall(r'_T\d?',file):
        mT.append(file)
    elif re.findall(r'_M\d?',file):
        mM.append(file)
    elif re.findall(r'_D\d?',file):
        mD.append(file)
    elif re.findall(r'_K\d?',file):
        mK.append(file)
    elif re.findall(r'_L\d?',file):
        mL.append(file)
    elif re.findall(r'_N\d?',file):
        mN.append(file)
    else:
        mBG.append(file)


lenE=len(mE)
lenP=len(mP)
lenG=len(mG)
lenB=len(mB)
lenI=len(mI)
lenO=len(mO)
lenT=len(mT)
lenM=len(mM)
lenD=len(mD)
lenK=len(mK)
lenL=len(mL)
lenN=len(mN)
lenBG=len(mBG)

import random
E=[i for i in range(0,lenE)]
random.shuffle(E)
trainE=[mE[E[i]] for i in range(54,lenE)]
testE=[mE[E[i]] for i in range(0,54)]

P=[i for i in range(0,lenP)]
random.shuffle(P)
trainP=[mP[P[i]] for i in range(54,lenP)]
testP=[mP[P[i]] for i in range(0,54)]

G=[i for i in range(0,lenG)]
random.shuffle(G)
trainG=[mG[G[i]] for i in range(54,lenG)]
testG=[mG[G[i]] for i in range(0,54)]

B=[i for i in range(0,lenB)]
random.shuffle(B)
trainB=[mB[B[i]] for i in range(54,lenB)]
testB=[mB[B[i]] for i in range(0,54)]

I=[i for i in range(0,lenI)]
random.shuffle(I)
trainI=[mI[I[i]] for i in range(54,lenI)]
testI=[mI[I[i]] for i in range(0,54)]

O=[i for i in range(0,lenO)]
random.shuffle(O)
trainO=[mO[O[i]] for i in range(54,lenO)]
testO=[mO[O[i]] for i in range(0,54)]

T=[i for i in range(0,lenT)]
random.shuffle(T)
trainT=[mT[T[i]] for i in range(54,lenT)]
testT=[mT[T[i]] for i in range(0,54)]

M=[i for i in range(0,lenM)]
random.shuffle(M)
trainM=[mM[M[i]] for i in range(54,lenM)]
testM=[mM[M[i]] for i in range(0,54)]

D=[i for i in range(0,lenD)]
random.shuffle(D)
trainD=[mD[D[i]] for i in range(54,lenD)]
testD=[mD[D[i]] for i in range(0,54)]

K=[i for i in range(0,lenK)]
random.shuffle(K)
trainK=[mK[K[i]] for i in range(54,lenK)]
testK=[mK[K[i]] for i in range(0,54)]

L=[i for i in range(0,lenL)]
random.shuffle(L)
trainL=[mL[L[i]] for i in range(54,lenL)]
testL=[mL[L[i]] for i in range(0,54)]

N=[i for i in range(0,lenN)]
random.shuffle(N)
trainN=[mN[N[i]] for i in range(54,lenN)]
testN=[mN[N[i]] for i in range(0,54)]


BG=[i for i in range(0,lenBG)]
random.shuffle(BG)
trainBG=[mBG[BG[i]] for i in range(54,lenBG)]
testBG=[mBG[BG[i]] for i in range(0,40)]

fileTrain=open('test.txt','w')
fileTrain.writelines(trainE)
fileTrain.writelines(trainP)
fileTrain.writelines(trainB)
fileTrain.writelines(trainG)
fileTrain.writelines(trainI)
fileTrain.writelines(trainO)
fileTrain.writelines(trainT)
fileTrain.writelines(trainM)
fileTrain.writelines(trainD)
fileTrain.writelines(trainK)
fileTrain.writelines(trainL)
fileTrain.writelines(trainN)
fileTrain.writelines(trainBG)

fileTest=open('train.txt','w')
fileTest.writelines(testE)
fileTest.writelines(testP)
fileTest.writelines(testB)
fileTest.writelines(testG)
fileTest.writelines(testI)
fileTest.writelines(testO)
fileTest.writelines(testT)
fileTest.writelines(testM)
fileTest.writelines(testD)
fileTest.writelines(testK)
fileTest.writelines(testL)
fileTest.writelines(testN)
fileTest.writelines(testBG)