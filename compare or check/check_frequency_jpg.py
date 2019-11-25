import os 
import sys 
import operator
from collections import Counter

def check(test):
    if len(byte) != 0:
        return ord(byte)
    else:
        return 0

file_num = 1000 # 전체 파일의 개수 
total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
std = 29 #기준 
stdup_cnt = 0 #기준이상인 파일의 개수 
value = [] # 최고 , 최저 비교에 쓰이는 수 
index = 0 # 상위 3개 헥사 값 인덱스 
index_number = 0 # 상위 3개 헥사 값 
index_number_cnt = [] #상위 3개 헥사값 세기
i = 1 # 반복문 제어 
save_file = "result.txt" #아웃풋 파일 절대 경로로 적어 줄 것 

for x in range(file_num):
            filename = r"C:\Users\rlaru\Downloads\jpg_fragment_datasets\%d"% (x+1)
            lst = [0 for _ in range (256)]
            with open(filename, "rb") as f:
                byte = f.read(1)
                while byte :
                    lst[check(byte)] += 1
                    byte = f.read(1)
            index, index_number = max(enumerate(lst), key = operator.itemgetter(1))
            print("file %d번째 "% (x+1))
            print("헥사값 1등:%02X 빈도수: %d "%(index, index_number),end='')
            index_number_cnt.append(index)
            del lst[index]
            index, index_number = max(enumerate(lst), key = operator.itemgetter(1))
            print("헥사값 2등:%02X 빈도수: %d "%(index, index_number),end='')
            index_number_cnt.append(index)
            del lst[index] 
            index, index_number = max(enumerate(lst), key = operator.itemgetter(1))
            print("헥사값 3등:%02X 빈도수: %d "%(index, index_number))   
            index_number_cnt.append(index)
            i *= 3 
          
# print("헥사 리스트 file %d개 기준"%file_num)
# for y in range(len(index_number_cnt)) :
#     print("%02X"%(index_number_cnt[y]),end=' ') 
# print("")  
#각 헥사 값 상위 3개 빈도수 체크 
result = Counter(index_number_cnt)
for x in range(len(result)):
    print(result[x])
      
     