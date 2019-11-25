import os
import sys
from tqdm import tqdm
from time import sleep

#byte의 값이 0인지pi 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0
# 진행 상황 알려줌 
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

## main

file_num = 1000 # 전체 파일의 개수 
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
std = 24 #기준 
stdup_cnt = 0 #기준이상인 파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 
total_lst = [0 for _ in range(256)] #헥사 빈도 총합 리스트 
result_lst = [0 for _ in range(256)] #결과 값 리스트 
file_lst = []
file_cnt =0
path = r"D:\wav_fragment_testset"
save_file_name = "result.txt"
save_file = open(save_file_name,'w') # 결과파일 절대경로로 적을 것 
lst= []

print("파일 탐색중..")
for x in range(file_num*5): 
                filename = path+r"\%d"% (x)            
                try:     
                        with open(filename, "rb") as f:                                                                                                                      
                                        if file_cnt >= file_num: 
                                                break
                                        file_lst.append(x)
                                        file_cnt+=1
                except:
                        print("",end='') 
                        continue

print("파일 탐색완료!")
printProgressBar(0, file_num, prefix = 'Progress:', suffix = 'Complete', length = 50)
for x in range(file_num):
                filename = path+r"\%d"% (file_lst[x])
                lst = [0 for _ in range(256)]
                
                #파일의 1바이트 씩 읽어서 갯수 체크
                with open(filename, "rb") as f:
                    byte = f.read(1)
                    lst[check(byte)] += 1  
                    while byte :
                    # print("%2X" % check(byte),end=' ')
                        byte = f.read(1)
                        lst[check(byte)] += 1
                for index in range(256):
                        total_lst[index] += lst[index] 
                #value.append(lst[0])
                ##기준 
                # if lst[0] >= std :
                #     stdup_cnt += 1
                printProgressBar(x+1, file_num, prefix = 'Progress:', suffix = 'Complete', length = 50)
                #print("file %d count 0 : %d"%(x,lst[0]))

#MaxValue = malx(value)
#MinValue = min(value)
for index in range(256):
        result_lst[index] = float(total_lst[index] / file_num) 
print("파일 %d개 기준"% file_num)
for x in range(256):
    print("헥사 값 %02X의 평균 개수: %.4f입니다."% (x, result_lst[x]))
    #print("헥사 값 %02X의 평균 개수: %.4f입니다."% (x, result_lst[x]),file=save_file)
# print("파일이 완료되어 지정하신 경로에 %s 파일이 저장되었습니다."%save_file_name)

