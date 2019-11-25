import os
import sys

#byte의 값이 0인지 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0

file_num = 10000 # 전체 파일의 개수 
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
std = 23 #기준 
stdup_cnt = 0 #기준이상인 파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 

for x in range(file_num+1):
                filename = r"D:\h264_fragment_testset\%d"% (x+1)

                lst = [0 for _ in range(256)]

                #파일의 1바이트 씩 읽어서 갯수 체크
                with open(filename, "rb") as f:
                    byte = f.read(1)                    
                    while byte :
                    # print("%2X" % check(byte),end=' ')
                        lst[check(byte)] += 1
                        byte = f.read(1)
                        
                #total += lst[0] 
                #value.append(lst[0])
                if lst[0] >= std :
                    stdup_cnt += 1

                
                #print("file %d count 0 : %d"%(x,lst[0]))

#MaxValue = max(value)
#MinValue = min(value)
#result = float(total / file_num) 
#print("File %d개 기준, 0의 평균 개수는 %3f입니다."% (file_num ,result))
#print("최고 개수: %d"% MaxValue)
#print("최저 개수: %d"% MinValue)
print("기준 %d 개 이상의 파일의 개수: %d"% (std,stdup_cnt))
print("전체의 %d %%를 차지합니다."% (stdup_cnt/file_num * 100))
                # #몇개 인지 최종적으로 보여줌
                # for x in range(256):
                #     if lst[x] != 0:
                #         print("%02X : %d" %(x,lst[x]))
