import os
import sys
import dis
import time

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
#0x값 선택적 제거를 위해
def replaceRight(original, old, new, count_right):
    repeat=0
    text = original
    
    count_find = original.count(old)
    if count_right > count_find : # 바꿀 횟수가 문자열에 포함된 old보다 많다면
        repeat = count_find # 문자열에 포함된 old의 모든 개수(count_find)만큼 교체한다
    else :
        repeat = count_right # 아니라면 입력받은 개수(count)만큼 교체한다

    for _ in range(repeat):
        find_index = text.rfind(old) # 오른쪽부터 index를 찾기위해 rfind 사용
        text = text[:find_index] + new + text[find_index+1:]
    
    return text

## main
byte_lst = []
byte = 1
two_byte = []
re_two_byte = []
op_code = []
filename = r"D:\jpg_fragment_datasets\1"
with open(filename, "rb") as f:  
                    byte = f.read(1)          
                    while byte :
                    # print("%2X" % check(byte),end=' ')
                        byte_lst.append(hex(check(byte)))
                        byte = f.read(1)
print(byte_lst)
print(len(byte_lst))
for x in range(0,len(byte_lst),2):
        byte="".join(byte_lst[x:x+2])
        print(byte)
        two_byte.append(byte)

printProgressBar(0, len(two_byte), prefix = 'Progress:', suffix = 'Complete', length = 50)
for x in range(len(two_byte)):
        
        re_two_byte.append(replaceRight(two_byte[x],"0x",'',1))
        re_two_byte[x]=replaceRight(re_two_byte[x],"x",'',1) 
        printProgressBar(x+1, len(two_byte), prefix = 'Progress:', suffix = 'Complete', length = 50)
        #re_two_byte[x]=re_two_byte.append(replaceRight(two_byte[x],'x','',1))    
        # re_two_byte[x]=replaceRight(re_two_byte[x],'0x','',1)
        # re_two_byte[x]=replaceRight(re_two_byte[x],'x','',2)
print(re_two_byte)
#print(len(two_byte))


# print(all_byte)
# print(dis.dis(all_byte))
# for x in range(len(two_byte)):
#         try:
#             #print(dis.get_instructions(all_byte))
#             op_code= dis.disco(re_two_byte[x]))
        
#         except:
#                 print("???",end=" ")


#dis.get_instructions(all_byte)
# for x in range(len(op_code)):
#         #time.sleep(0.1)
#         print(op_code[x])
