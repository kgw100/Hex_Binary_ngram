import os
import sys
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from IPython.display import display
#byte의 값이 0인지 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0

file_num = 800 # 전체 파일의 개수 
file_cnt = 0 # 파일 개수 구분
file_lst = []
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
std = 28 #기준 
stdup_cnt = 0 #기준이상인 파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 
path = [r"D:\wav_fragment_testset",r"D:\h264s_fragment_datasets",r"D:\jpg_fragment_datasets"]
h264s_path = r"D:\h264s_fragment_datasets"
jpg_path = r"D:\wav_fragment_testset"
hex_number = 0
hex_cnt1 = []
hex_cnt2 = []
hex_cnt3 = []
ext_lst =[[0 for i in range(3)] for j in range(file_num)]
ctrl_var = 0

for dir_path in path:
    for x in range(file_num*5): 
                        print("dir_path 1 : %s "%dir_path)
                        filename = dir_path+r"\%d"% (x)
                        try:       
                            with open(filename, "rb") as f:                                               
                                            if file_cnt >= file_num: break
                                            #print("file_Cnt %d"% file_cnt)
                                            file_lst.append(x)
                                            file_cnt+=1
                        except:
                                continue
    print("file_lst : %d"%len(file_lst))                   
    for x in range(file_num):
                    print(".",end=" ")
                    #print("x:%d"%x)
                    filename = dir_path+r"\%d"%(file_lst[x])
                    #파일의 1바이트 씩 읽어서 갯수 체크
                    lst = [0 for _ in range(256)]

                    with open(filename, "rb") as f:
                        byte = f.read(1) 
                        while byte :
                                # print("%2X" % check(byte),end=' ')
                                lst[check(byte)] += 1  
                                byte = f.read(1)                       
                    # total += lst[hex_number] 
                    # value.append(lst[hex_number])
                    if dir_path == r"D:\wav_fragment_testset":
                        if(40<=lst[0]<= 100):
                            hex_cnt3.append(lst[0])
                    elif  dir_path == r"D:\jpg_fragment_datasets":
                        if len(hex_cnt2) < len(hex_cnt3):    
                            hex_cnt2.append(lst[0])
                   
                    elif  dir_path == r"D:\h264s_fragment_datasets":
                        if len(hex_cnt1) < len(hex_cnt3):
                            hex_cnt1.append(lst[0])
            
    print("dir_path: %s"%dir_path)
    ctrl_var += 1
    file_lst = []
    file_cnt = 0
    if dir_path == r"D:\h264s_fragment_datasets":
                        ext_lst.append(hex_cnt1)
    elif dir_path == r"D:\jpg_fragment_datasets":
                        ext_lst.append(hex_cnt2)
    elif dir_path == r"D:\wav_fragment_testset":
                        ext_lst.append(hex_cnt3)
    # print(len(hex_cnt))

# sns.pairplot(pd.DataFrame(ext_lst))
# gscatter(range(file_num),range(3000),pd.DataFrame(ext_lst),'rkgb','o*',8,'on','Age','Weight')
# plt.scatter(range(file_num), hex_cnt3,color='0.3')
# plt.scatter(range(file_num), hex_cnt1,color='red')
# plt.scatter(range(file_num), hex_cnt2,color='yellow')
print(len(hex_cnt3))
print(len(hex_cnt1))
print(len(hex_cnt2))

plt.title('Compare Hex Count',fontsize=20)
plt.xlabel('0 Hex Count',fontsize=14)
plt.ylabel('File Count',fontsize=14)
plt.scatter(hex_cnt3,range(len(hex_cnt3)),color='0.15')
plt.scatter(hex_cnt2,range(len(hex_cnt3)),color='orange')
plt.scatter(hex_cnt1,range(len(hex_cnt3)),color='blue')


plt.show()
