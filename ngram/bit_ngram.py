import os 
import sys 
from collections import Counter

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

#main 
file_num = 100 # 전체 파일의 개수  
result_lst = [0 for _ in range(256)] #결과 값 리스트 
file_lst = []
file_cnt = 0
byte_lst = []
ngram_lst = []
ngram_cnt = 0
bit_cnt = 5 # 1gram의 bit 개수
n = 3 # ngram 수 
check_num = 0
input_path = r'D:\h264_fragment_testset' #읽어올 파일 경로 
output_path = r'C:\Users\rlaru\Desktop\BOB프로젝트\output' 
total_byte = ''

file_extension = input_path[3:9] 
print(file_extension)
save_file = open(output_path+r'\%s_%d_%d_%dgram_tst.txt'%(file_extension,file_num,bit_cnt,n),'w') # 아웃풋 파일 경로 
print("파일 탐색중..")
for x in range(file_num * 100):
                filename = input_path+r"\%d"% (x)            
                try:     
                        with open(filename, "rb") as f:                                                                                                                      
                                        if file_cnt >= file_num: 
                                                break
                                        file_lst.append(x)
                                        file_cnt+=1
                except: 
                        continue
print("파일 탐색완료!")
printProgressBar(0, file_num, prefix = 'Progress1:', suffix = 'Complete', length = 50)     
for x in range(file_num):

                filename = input_path+r"\%d"% (file_lst[x])
                #파일의 1바이트 씩 읽어서 갯수 체크
                with open(filename, "rb") as f:
                    byte = f.read(1)
                    while byte :
                        res_byte = bin(check(byte))[2:].zfill(8)
                        total_byte = "".join([total_byte,res_byte])
                        byte = f.read(1)                             
                printProgressBar(x+1, file_num, prefix = 'Progress1:', suffix = 'Complete', length = 50)
#print(byte_lst)
#print(len(byte_lst))
# print(byte_lst)
# total_bin_byte = "".join(byte_lst[:])


## ngram 피처 추출 부분 
printProgressBar(0, len(total_byte), prefix = 'Progress2:', suffix = 'Complete', length = 50)
for x in range(0,len(total_byte),1):
        
        if n== 2:
        #2gram
            byte="&".join([total_byte[x:x+bit_cnt],total_byte[x+bit_cnt:x+2*bit_cnt]])
        elif n== 3:
        #3gram
            byte="&".join([total_byte[x:x+bit_cnt],total_byte[x+bit_cnt:x+2*bit_cnt],\
                total_byte[x+2*bit_cnt:x+3*bit_cnt]])
        #print(byte)
        ngram_lst.append(byte)
        printProgressBar(x+1, len(total_byte), prefix = 'Progress2:', suffix = 'Complete', length = 50)
# print(ngram_lst)
# print(len(byte_lst))
ngram_cnt = Counter(ngram_lst)
print(ngram_cnt.most_common(),file=save_file)


