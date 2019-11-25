import os
import sys

#byte의 값이 0인지 체크 ord의 매개변수가 0이면 에러남
def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()


total = 0 # 특정 바이트 값의 빈도수 총합 (전체 파일) 
value = [] # 최고 , 최저 비교에 쓰이는 수 
hex_number = 0
file_num = 1000
num = 0
num2 = 0
#test_dir_list = ['JPG_11000', 'H264_11000']
test_dir_list = ['jpg_fragment_datasets','h264s_fragment_datasets']
print("파일 탐색중..")
for xxe in test_dir_list:
    test_file_cnt = 0 # test 파일 개수 구분
    h264s_file_cnt = 0
    jpg_stdup_cnt = 0 #기준이상인 0파일의 개수 
    h264_stdup_cnt = 0 #기준 미만인 0파일의 개수 
    test_file_lst = []
    h264_file_lst = []
    jpg_file_lst = []
    test_path = r"D:\{0}".format(xxe)
    for x in os.listdir(r"D:\{0}".format(xxe)): 
                        test_filename = test_path + r"\%s"% (x)
                    
                        try:       
                            with open(test_filename, "rb") as f:                                               
                                            if test_file_cnt >= file_num: break
                                            #print("file_Cnt %d"% file_cnt)
                                            test_file_lst.append(x)
                                            test_file_cnt+=1
                                        
                        except:
                                continue
    save_path = r"C:\Users\rlaru\Desktop\BOB프로젝트\output"
    fn2 = r'\jpg_h264.txt'
    save_file = save_path + fn2

    for x in test_file_lst:
                        
                        #print(".",end=" ")
                        #print("x:%d"%x)
                        test_filename = test_path+r"\%s"%(x)
                        #파일의 1바이트 씩 읽어서 갯수 체크
                        lst = [0 for _ in range(256)]

                        with open(test_filename, "rb") as f:
                            byte = f.read(1) 
                            while byte :
                                    # print("%2X" % check(byte),end=' ')
                                    lst[check(byte)] += 1  
                                    byte = f.read(1)                       
                        #total += lst[hex_number] 
                        #value.append(lst[hex_number])                     
                        if lst[21]>=18 and (lst[49]>= 18)and lst[52]>= 18 and lst[92] >= 18:
                                jpg_stdup_cnt += 1
                        else:
                                h264_stdup_cnt += 1
                        if lst[0]>= 26  :
                                jpg_stdup_cnt += 1  
                                h264_stdup_cnt -= 1
                        if lst[21]<= 9 and lst[49]<= 9 and lst[52]<= 9 and lst[92] <= 9:
                                jpg_stdup_cnt -= 1  
                                h264_stdup_cnt += 1
                        if lst[50] >= 20 and lst[169]>= 20:
                                jpg_stdup_cnt += 1
                                h264_stdup_cnt -= 1
                        
            
    print("\n{0}\n".format(xxe))
    if xxe == test_dir_list[0]:
        print("JPG 정확도: %.4f"%(jpg_stdup_cnt/file_num*100))
    elif xxe == test_dir_list[1]:
        print("h264 정확도: %.4f"%(h264_stdup_cnt/file_num*100))
    print("")