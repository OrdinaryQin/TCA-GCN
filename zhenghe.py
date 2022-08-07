import argparse
import pickle
import os

import numpy as np
from tqdm import tqdm
if __name__ == "__main__":
    npz_data = np.load(r'E:\ntuu\NTU60_CS.npz')
    label = np.where(npz_data['y_test'] > 0)[1]
    
    with open(os.path.join(r'C:\Users\lenovo\Desktop\affview10\1', 'epoch1_test_score.pkl'), 'rb') as r1:
        r1 = list(pickle.load(r1).items())

    with open(os.path.join(r'C:\Users\lenovo\Desktop\affview10\2', 'epoch1_test_score.pkl'), 'rb') as r2:
        r2 = list(pickle.load(r2).items())

   
    with open(os.path.join(r'C:\Users\lenovo\Desktop\affview10\3', 'epoch1_test_score.pkl'), 'rb') as r3:
        r3 = list(pickle.load(r3).items())
    
    with open(os.path.join(r'C:\Users\lenovo\Desktop\affview10\4', 'epoch1_test_score.pkl'), 'rb') as r4:
        r4 = list(pickle.load(r4).items())

    right_num = total_num = right_num_5 = 0
    acc=[]


    
 #   for alpha in np.arange(0,2.1,0.1):
    acc=[]        
    alpha1=0.6
    alpha2=0.6
    alpha3=0.4
    alpha4=0.4
 #   for alpha in np.arange(0.0,2.1,0.1):
#        for alpha1 in np.arange(0.0,2.1,0.1):
   # Ageshu=np.zeros((120,120)
    for i in tqdm(range(len(label))):
        l = label[i]
      #  print('l',l)
#        a=np.argmax(r11,r22,r33,r44)
        _, r11 = r1[i]
        _, r22 = r2[i]
        _, r33 = r3[i]
        _, r44 = r4[i]
      #  arr=[r11,r22,r33,r44]
#        print(np.max(arr))
 #       r11= (r11 - np.min(arr))/(np.max(arr)- np.min(arr))
#        r22= (r22 - np.min(arr))/(np.max(arr)- np.min(arr))
 #       r33= (r33 - np.min(arr))/(np.max(arr)- np.min(arr))
 #       r44= (r44 - np.min(arr))/(np.max(arr)- np.min(arr))
 #       print(np.max(r11))#,r22,r33,r44)
        r = r11 * alpha1 + r22 * alpha2 + r33 * alpha3 + r44 * alpha4
        rank_5 = r.argsort()[-5:]
        right_num_5 += int(int(l) in rank_5)
        r = np.argmax(r)
        right_num += int(r == int(l))
        total_num += 1
    acc1 = right_num / total_num
    acc5 = right_num_5 / total_num
    acc.append(acc1)
    #            if acc < acc1:
    #                acc=acc1
    a=max(acc) 
    print('Top1 Acc: {:.4f}%'.format(acc1 * 100),format(acc5 * 100))  
