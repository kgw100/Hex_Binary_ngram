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
path = [r"D:\h264s_fragment_datasets",r"D:\jpg_fragment_datasets",r"D:\wav_fragment_testset"]
h264s_path = r"D:\h264s_fragment_datasets"
jpg_path = r"D:\wav_fragment_testset"
hex_number = 0
hex_cnt1 = []
hex_cnt2 = []
hex_cnt3 = []
ext_lst =[[0 for i in range(3)] for j in range(file_num)]

for dir_path in path:
    for x in range(file_num*5): 
                        filename = dir_path+r"\%d"% (x)
                        try:       
                            with open(filename, "rb") as f:                                               
                                            if file_cnt >= file_num: break
                                            #print("file_Cnt %d"% file_cnt)
                                            file_lst.append(x)
                                            file_cnt+=1
                        except:
                                continue
    print("진행중",end=" ")                     
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
                    if dir_path == r"D:\h264s_fragment_datasets":
                        if len(hex_cnt1) < 242:
                            hex_cnt1.append(lst[0])
                    elif dir_path == r"D:\jpg_fragment_datasets":
                        if len(hex_cnt2) < 242:    
                            hex_cnt2.append(lst[0])
                    elif dir_path == r"D:\wav_fragment_testset":
                        if(40<=lst[0]<= 100):
                            hex_cnt3.append(lst[0])
                    # if lst[0] > std :
                    #          stdup_cnt += 1

                    
                    #print("file %d count 0 : %d"%(x,lst[0]))

    #print("file 개수 %d"% file_cnt)
    # MaxValue = max(value)
    # MinValue = min(value)
    # result = float(total / file_num) 
    # print("File %d개 기준, 0의 평균 개수는 %3f입니다."% (file_num ,result))
    # print("최고 개수: %d"% MaxValue)
    # print("최저 개수: %d"% MinValue)
    # print("기준 %d 개 이상의 파일의 개수: %d"% (std+1,file_num-stdup_cnt))
    # print("전체의 %.5f %%를 차지합니다."% (stdup_cnt/file_num * 100))
    
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
# fig,ax = plt.subplots()
# ax.legend(fontzise=12,loc='uper left' )
plt.title('Compare Hex Count',fontsize=20)
plt.xlabel('File Num',fontsize=14)
plt.ylabel('Hex Count',fontsize=14)
plt.scatter(hex_cnt3,range(len(hex_cnt3)),color='0.15')
plt.scatter(hex_cnt2,range(len(hex_cnt3)),color='orange')
plt.scatter(hex_cnt1,range(len(hex_cnt3)),color='blue')



# legend('Location','northeastoutside')
# color =['D', 'D', 'D', 'E', 'E', 'E', 'F', 'F', 'F', 'G', 'G', 'G',]
# df = pd.DataFrame(dict(h264 =hex_cnt1, jpg=hex_cnt2, wav=hex_cnt3,color=color))
# flg, ax = plt.subplots()
# colors = {'D':'black', 'E':'blue', 'F':'green', 'G':'black'}

# ax.scatter(df['h264'],df['jpg'],df['wav'],c=df['color'].apply(lambda x: colors[x]))
# plt.show()
# fig, ax = plt.subplots()

# colors = {'D':'red', 'E':'blue', 'F':'green', 'G':'black'}

# grouped = df.groupby('color')
# for key, group in grouped:
#     group.plot(ax=ax, kind='scatter', x='carat', y='price', label=key, color=colors[key])

plt.show()

    # plt.figure()
    # plt.scatter(range(file_num),hex_cnt)
    # plt.show()
    # hex_cnt =[]

# sns.title("TEST")
# sns.show()
# plt.figure(figsize=(7,6))

# fontdict={'fontsize': 18,
#           'weight' : 'bold',
#          'horizontalalignment': 'center'}

# sns.set_context('paper', font_scale=2) #this makes the font and scatterpoints much smaller, hence the need for size adjustemnts
# sns.set_style('white')

# sns.scatterplot(x='temp', y='cnt', hue='Season', data=lst[0], style='Season', 
#                     palette=['green'], legend='full', size='Season', sizes=[100,100,100,100])

# plt.legend(scatterpoints=1,
#            bbox_to_anchor=(1, 0.7), loc=2, borderaxespad=1.,
#            ncol=1,
#            fontsize=14)

# plt.xlabel('Normalized Temperature', fontsize=16, fontweight='bold')
# plt.ylabel('Count of Total Bike Rentals', fontsize=16, fontweight='bold')
# plt.title('Bike Rentals at Different Temperatures\nBy Season', fontdict=fontdict, color="black",position=(0.5,1))
                
