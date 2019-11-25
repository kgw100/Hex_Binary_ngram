import os 
import sys 
from collections import Counter

#byte의 값이 0인지pi 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0
def check_file_num(start):
    ch_file_num = start//4097
    if ch_file_num == 0:
        return 1
    else :
        return ch_file_num+1
    
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
file_num = 3000 # 전체 파일의 개수  
result_lst = [0 for _ in range(256)] #결과 값 리스트 
file_lst = []
file_cnt =0
byte_lst = []
ngram_lst = []
ngram_cnt = 0
n = 2 #n-gram 그룹의 숫자
#input_path = r'D:\h264s_fragment_datasets' #읽어올 파일 경로 
input_path = r'D:\real_jpg_h264_wav'
output_path = r'C:\Users\rlaru\Desktop\BOB프로젝트\nram'
file_extension = input_path[3:7]
file_ext_num = 3
jpg_cnt = 0
h264_cnt = 0
wav_cnt = 0
bns_h264_cnt = 0 # h264의 개수를 의미하지 않고 추가적 
acc_jpg_cnt = 0 #실 정확도를 위해 걸러낸
acc_bns_h264_cnt = 0 #실 정확도를 위해 걸러낸
acc_wav_cnt = 0
acc_jpg_tst = []
print(file_extension)
save_file = open(output_path+r'\%s_%d_%d.txt'%(file_extension,file_num,n),'w') # 아웃풋 파일 경로 , 실행결과를 저장하고싶다면 출력문에 file=save_file로 해서 쓰길
print("파일 탐색중..")
for x in range(file_num * 10):
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
                lst = [0 for _ in range(256)]

                #파일의 1바이트 씩 읽어서 갯수 
                with open(filename, "rb") as f:
                    byte = f.read(1)
                    while byte :
                        byte_lst.append(str(check(byte))) #2차원을 만들지 않고, lst에 헥사값을 다 넣었음 
                        byte = f.read(1)
                byte_lst.append('end')   #파일 하나 하나를 구부해주는 구분자                          
                printProgressBar(x+1, file_num, prefix = 'Progress1:', suffix = 'Complete', length = 50)

start = 0
find = 0 # n gram 두 개 피쳐 활용시 하나 피쳐 발견해서 동시에 엮기 위해
jpg_acc_lst = []
h264_acc_lst = []
wav_acc_lst = []

printProgressBar(0, len(byte_lst), prefix = 'Progress2:', suffix = 'Complete', length = 50)

while(start < len(byte_lst)):
    breaker = False
    for x in range(start, len(byte_lst),1):
                byte="&".join(byte_lst[x:x+n])
                # 가장 확실한 피처 순으로 배치해 속도를 높였음       
                if byte == '255&0':
                            jpg_acc_lst.append(check_file_num(start))
                            jpg_cnt+= 1
                            start += 4097
                            break
                if byte == '61&34':
                    find = x+start
                    # print("find = %d"% (find/4096))
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='255&0':
                            jpg_acc_lst.append(check_file_num(start))
                            jpg_cnt+= 1
                            start += 4097                                      
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break
                if byte == '189&0':
                    find = x+start
                    # print("find = %d"% (find/4096))
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='61&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '57&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '255&253':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '56&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '61&128':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '185&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte == '0&128':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break
                
                if byte == '61&0':
                    find = x+start
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='189&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break 
                       
                
                if byte == '60&0':
                    find = x+start
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='184&0':
                            wav_acc_lst.append(check_file_num(start))
                            wav_cnt+= 1
                            start += 4097
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break
                # if byte == '184&0':
                #     wav_acc_lst.append(check_file_num(start))
                #     wav_cnt+= 1
                #     start += 4097
                #     break
                if byte == '62&0':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                    break
                if byte == '59&0':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                    break    
                if byte == '189&128':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                if byte == '189&192':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                if byte == '186&0':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                if byte == '188&0':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                    break
                if byte == '0&64':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                    break
                if byte == '249&255':
                    wav_acc_lst.append(check_file_num(start))
                    wav_cnt+= 1
                    start += 4097
                    break
                if byte == '0&3':
                    find = x+start
                    # print("find = %d"% (find/4096))
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='3&0':
                            h264_acc_lst.append(check_file_num(start))
                            bns_h264_cnt+= 1
                            start += 4097                          
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break
                if byte == '3&0':
                    find = x+start
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='0&3':
                            h264_acc_lst.append(check_file_num(start))
                            bns_h264_cnt+= 1
                            start += 4097
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break 
                    
                if byte == '61&34':
                    find = x+start
                    for x in range(find,len(byte_lst),1):
                        byte="&".join(byte_lst[x:x+n])
                        if byte =='0&0':
                            jpg_acc_lst.append(check_file_num(start))
                            jpg_cnt+= 1
                            start += 4097
                            break
                        if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                            start += 4097
                            breaker = True
                            break
               
                       
                
               

                # if byte == '0&0': ##넣으면 jpg는 내려가고 h264의 정확도는 올라갑니다
                #     find = x+start
                #     for x in range(find,len(byte_lst),1):
                #         byte="&".join(byte_lst[x:x+n])
                #         if byte =='61&34':
                #             jpg_cnt+= 1
                #             start += 4097
                #             break
                #         if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                #             start += 4097
                #             breaker = True
                #             break
                if breaker == True :
                    break
                if byte_lst[x] == 'end' or byte_lst[x+1] == 'end':
                    start += 4097
                if start >= len(byte_lst):
                    break
    printProgressBar(x+2, len(byte_lst), prefix = 'Progress2:', suffix = 'Complete', length = 50)
print("")
for x in range(file_num): # JPG
        try: 
            if jpg_acc_lst[x] <= 1000:
                acc_jpg_cnt += 1
                acc_jpg_tst.append(jpg_acc_lst[x])
            if jpg_acc_lst[x] > 1000 and jpg_acc_lst[x] <= 2000:
                acc_bns_h264_cnt += 1   
        except:
            print("",end="")
for x in range(file_num): # H264
            try:
                if h264_acc_lst[x] > 1000 and h264_acc_lst[x]<= 2000:
                    acc_bns_h264_cnt -= 1
            except:
                print("",end="")
for x in range(file_num): # WAV
            try:
                if wav_acc_lst[x] > 2000:
                    acc_wav_cnt += 1
                if wav_acc_lst[x] > 1000 and wav_acc_lst[x] <= 2000 :
                    acc_bns_h264_cnt += 1
                if wav_acc_lst[x] <= 1000:
                    acc_jpg_cnt -= 1
            except:
                print("",end="")

print(start//4097)
print(jpg_acc_lst)
print(h264_acc_lst)
print(wav_acc_lst)
# if file_extension == 'h264':
# print("트레이닝 결과 :%.4f "%((file_num-jpg_cnt+bns_h264_cnt)/file_num*100)) 
# else : # jpg
# print("트레이닝 결과 :%.4f "%(jpg_cnt/file_num*100)) 
# print("트레이닝 결과 :%.4f "%(((file_num/2)-jpg_cnt+bns_h264_cnt)/(file_num/2)*100))
# print("트레이닝 결과 :%.4f "%(jpg_cnt/(file_num/2)*100)) 
# print(jpg_acc_lst)
# print(h264_acc_lst)
# print(acc_jpg_tst)
print("파일 JPG 1000개 ,H264 1000개 , WAV 1000개 총 파일 3000개") 
print("테스트 결과 JPG 정확도:%.3f %%"%((acc_jpg_cnt)/(file_num/file_ext_num) *100))
print("테스트 결과 H264 정확도:%.3f %%"%(((file_num/file_ext_num)-acc_bns_h264_cnt)/ \
    (file_num/file_ext_num) *100))
print("테스트 결과 WAV 정확도: %.3f %%"%(acc_wav_cnt/(file_num/file_ext_num)*100))