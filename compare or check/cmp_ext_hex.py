import os
import sys

#byte의 값이 0인지 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0

file_num = 100000 # 전체 파일의 개수 
jpg_file_cnt = 0 # jpg 파일 개수 구분
h264s_file_cnt = 0
jpg_file_lst = []
h264s_file_lst = []
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
std1 = 23 #기준 1
std2 = 18 #기준 2
std3 = 19 #기준 3
std4 = 18 #기준 4
std5 = 18 #기준 5
jpg_stdup_cnt = 0 #기준이상인 0파일의 개수 
h264s_stdup_cnt = 0 #기준 미만인 0파일의 개수 
# jpg_stdup_20cnt = 0 #기준이상인 20파일의 개수 
# h264s_stdup_20cnt = 0 #기준 미만인 20파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 
#path = [r"D:\h264s_fragment_datasets",r"D:\jpg_fragment_datasets"]
h264s_path = r"D:\h264s_fragment_datasets"
jpg_path = r"D:\jpg_fragment_datasets"
hex_number = 0

for x in range(file_num*5): 
                    h264s_filename = h264s_path+r"\%d"% (x)
                    
                    try:       
                        with open( h264s_filename, "rb") as f:                                               
                                        if h264s_file_cnt >= file_num: break
                                        #print("file_Cnt %d"% file_cnt)
                                        h264s_file_lst.append(x)
                                        h264s_file_cnt+=1
                    except:
                            continue
print("진행중",end=" ")                     
for x in range(file_num):
                print(".",end=" ")
                #print("x:%d"%x)
                h264s_filename = h264s_path+r"\%d"%(h264s_file_lst[x])
                #파일의 1바이트 씩 읽어서 갯수 체크
                lst = [0 for _ in range(256)]

                with open(h264s_filename, "rb") as f:
                    byte = f.read(1) 
                    while byte :
                            # print("%2X" % check(byte),end=' ')
                            lst[check(byte)] += 1  
                            byte = f.read(1)                       
                #total += lst[hex_number] 
                #value.append(lst[hex_number])
                if lst[0] < std1 or lst[20] < std2 or lst[92] < std3 or lst[52] < std4 or lst[169] <std5:
                         h264s_stdup_cnt += 1     
   
                
                #print("file %d count 0 : %d"%(x,lst[0]))

print("h264 기준을 통과한 파일의 개수: %d"% (h264s_stdup_cnt))
print("h264 정확도: %.4f"% (h264s_stdup_cnt/file_num * 100))