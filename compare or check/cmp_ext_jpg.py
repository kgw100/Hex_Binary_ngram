import os
import sys

#byte의 값이 0인지 체크 ord의 매개변수가 0이면 에러남
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

file_num = 5624 # 전체 파일의 개수 
file_cnt = 0 # jpg 파일 개수 구분
h264s_file_cnt = 0
file_lst = []
h264s_file_lst = []
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
# std1 = 22 #기준 1
# std2 = 18 # 기준 2
# std3 = 19 # 기준 3
# std4 = 18 # 기준 4
# std5 = 18 # 기준 5
jpg_stdup_cnt = 0 #기준이상인 0파일의 개수 
h264s_stdup_cnt = 0 #기준 미만인 0파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 
#path = [r"D:\h264s_fragment_datasets",r"D:\jpg_fragment_datasets"]
h264s_path = r"D:\h264s_fragment_datasets"
jpg_path = r"D:\jpg_h264"
hex_number = 0
jpg_acc_cnt = 0 # jpg정확도 판단을 위한 count
h264_acc_cnt = 0 
jpg_acc_lst = []
h264_acc_lst = []
file_acc_lst = []
h264_number = 3386
jpg_number = 2238

for x in range(file_num*20): 
                    jpg_filename = jpg_path+r"\%d"% (x)
                    
                    try:       
                        with open(jpg_filename, "rb") as f:                                               
                                        if file_cnt >= file_num: break
                                        file_lst.append(x)
                                        file_cnt+=1
                    except:
                            continue
print(len(file_lst))
printProgressBar(0, file_num, prefix = 'Progress:', suffix = 'Complete', length = 50)
for x in range(file_num):
                jpg_filename = jpg_path+r"\%d"%(file_lst[x])
                #파일의 1바이트 씩 읽어서 갯수 체크
                lst = [0 for _ in range(256)]

                with open(jpg_filename, "rb") as f:
                    byte = f.read(1) 
                    while byte :
                            lst[check(byte)] += 1  
                            byte = f.read(1)
                if ((5 <= lst[0] <= 29)and (5 <= lst[23] <= 33) and (3 <= lst[32] <= 30) and (lst[41] >= 4 and lst[41] <= 26) and 
                            (lst[42] >= 3 and lst[42] <= 28) and (lst[47] >= 5 and lst[47] <= 33) and lst[73] <= 28 and lst[74] <= 27 and (lst[82] >= 5 and lst[82] <= 29) and 
                            (lst[84] >= 3 and lst[84] <= 29) and (lst[85] >= 3 and lst[85] <= 27) and (lst[94] >= 5 and lst[94] <= 33)and (lst[95] >= 5 and lst[95] <= 33) and 
                            (lst[103] >= 4 and lst[103] <= 30) and (lst[131] >= 5 and lst[131] <= 33) and (lst[132] >= 5 and lst[132] <= 33) and (lst[135] >= 3 and lst[135] <= 33) and 
                            (lst[146] >= 3 and lst[146] <= 27) and (lst[149] >= 4 and lst[149] <= 27) and (lst[164] >= 3 and lst[164] <= 28) and (lst[165] >= 2 and lst[165] <= 29) and 
                            (lst[169] >= 2 and lst[169] <= 27) and (lst[170] >= 3 and lst[170] <= 27) and (lst[188] >= 2 and lst[188] <= 32) and (lst[236] >= 2 and lst[236] <= 30) and 
                            (lst[248] >= 3 and lst[248] <= 32) and (lst[232] >= 2 and lst[232] <= 32) and (lst[255] >= 6 and lst[255] <= 33)):
                                h264s_stdup_cnt += 1
                                h264_acc_lst.append(x)
                                print(x)
                                #file_acc_lst.append(x)
                else:
                                jpg_stdup_cnt += 1
                                jpg_acc_lst.append(x)
                                #file_acc_lst.append(x)
                                                                          
                #jpg라고 판단하는 기준 
                # if lst[0] >= std1: #and lst[20] >= std2 and lst[92] >= std3 : #and lst[52] >= std4 and lst[169] >= std5:
                #          jpg_stdup_cnt += 1   
                #기준을 만족하는 실제 jpg 파일              
              
        
                printProgressBar(x+1, file_num, prefix = 'Progress:', suffix = 'Complete', length = 50)
for x in range(file_num):
                
                try:
                    if h264_acc_lst[x] >= (file_num/2): 
                            # if lst[0] >= std1 :#and lst[20] >= std2 and lst[92] >= std3 :
                                h264_acc_cnt += 1
                    if jpg_acc_lst[x] <= (file_num/2):
                            # if lst[0] < std1 :#and lst[20] >= std2 and lst[92] >= std3 :                    
                                jpg_acc_cnt += 1
                except:
                    print("")

print("jpg: %d개, h264:%d개 총 합 %d개 "%(jpg_number,h264_number,file_num))
print("판단) jpg 파일의 개수: %d"% (jpg_stdup_cnt))
print("판단) h264 파일의 개수: %d"% (h264s_stdup_cnt))
print("실제 기준에 속한 h264파일 수 :%d"% h264_acc_cnt)
print("실제 기준에 속한 jpg파일 수 : %d"%jpg_acc_cnt)
print("jpg 실 정확도: %.4f"% (jpg_acc_cnt/(jpg_number) * 100))
print("h264 실 정확도: %.4f"% (h264_acc_cnt/(h264_number)* 100))
