import os
import sys
import binascii
import cv2
import numpy as np 
import shutil
from numpy import argmax 
from PIL import Image

def check(byte):
    if len(byte) != 0:            
        return ord(byte)
    else:
        return 0
def Dataization(img_path): 
    image_w = 64
    image_h = 64
    img = cv2.imread(img_path) 
    img = cv2.resize(img, None, fx=image_w/img.shape[1], fy=image_h/img.shape[0]) 
    return (img/256) 

def getBinaryData(filename):
    binaryValues = []
    file = open(filename, "rb")
    data = file.read(1)  # read byte by byte
    while data !=b"":
        try:
            binaryValues.append(ord(data))  # store value to array
        except TypeError:
            pass
        data = file.read(1)  # get next byte value
    return binaryValues

def createGreyScaleImageSpecificWith(dataSet,outputfilename):
    image = Image.new('L', (64,64))
    image.putdata(dataSet)
    imagename = outputfilename+".png"
    image.save(imagename)
    print (imagename+" Greyscale image created")

HEX_LIST = ['0x02', '0x03', '0xFF', '0xEF', '0xF7', '0x00', '0x10', '0x49',
            '0x92', '0x20', '0x01', '0xA4', '0x55', '0x95', '0x6D', '0x48',
            '0xD4', '0xA9', '0xE8', '0xA5', '0xAA', '0x55', '0x2F', '0xA7',
            '0x52', '0x4A', '0x54', '0xA8', '0x52', '0x29', '0x17', '0x20',
            '0x24', '0x26', '0x42', '0x21', '0x24', '0x84', '0xF3', '0xD3',
            '0x15', '0xD0', '0xD7', '0xE8', '0xB5', '0xB0', '0x1D', '0xBD',
            '0x08', '0x18', '0x04', '0x0C', '0x2D', '0xAD', '0x0D', '0xE7',
            '0xD7', '0xD8', '0xFC', '0xBF', '0x7F', '0xFD', '0xFE', '0xFB'
            '0XFF&0x0','0x20&0x20','0x61&0x34','0x48&0x24','0x55&0x55','0xAA&0xAA','0x59&0x96','0x51&0x14'
            '0x69&0x9A','0xA6&0x69','0x6D&0xDB','0x9A&0xA6','0x5D&0x57','0xD3&0x34','0x65&0x59','0x4D&0xD3'
            '0x2C&0xA2','0x']
#training set
#dir_list = ['h264_fragment_trainingset', 'jpg_fragment_trainingset', 'png_fragment_trainingset', 'h265_fragment_trainingset', 'wav_fragment_trainingset']

#test set
dir_list = ['png_fragment_testset', 'h264_fragment_testset', 'h265_fragment_testset', 'jpg_fragment_testset', 'wav_fragment_testset']
#dir_list = ['png_fragment_testset']
#dir_list = ['png_fragment_trainingset']
for xxe in dir_list:
    path = r"C:\Users\yoon\Desktop\dataset\{0}".format(xxe)
    #save_path = r"C:\Users\yoon\Desktop\CNNtest\trainingset_output\{0}_feature".format(xxe)
    save_path = r"C:\Users\yoon\Desktop\CNNtest\test_output\{0}_feature".format(xxe)
    total_lst = [0 for _ in range(256)]
    file_lst = []
    file_num = 1000 #파일 개수 설정
    file_cnt = 0
    byte_lst= []
    print("파일 탐색중..")
    filenames = os.listdir(path)
    print("디렉토리 내의 파일갯수 : {0}".format(len(filenames)))

    if len(filenames) < file_num:
        sys.exit()

    for filename in filenames:
        file_lst.append(filename)
        file_cnt+=1
        if file_cnt == file_num:
            break
    print("파일 탐색완료!")
    name_index = 0
    hex_cnt = 0
    for x in file_lst:
                      test_filename = path+r"\%s"%(x)
                       #파일의 1바이트 씩 읽어서 갯수 체크
                      lst = [0 for _ in range(256)]

                      with open(test_filename, "rb") as f:
                                   byte = f.read(1) 
                                   while byte :
                                           lst[check(byte)] += 1 
                                           byte_lst.append(hex(check(byte))) 

                                           byte = f.read(1)
                                #    for index in range(256):
                                #         total_lst[index] += lst[index]    
                      name_index += 1      
                      fn2 = r'\{0}_{1}'.format(path[30:],name_index)
                      save_file = save_path + fn2
                      with open(save_file, 'wb') as fb:
                                    for xxe2 in HEX_LIST:
                                                    hex_value = int('{0}'.format(xxe2),16)
                                                    input_value = lst[hex_value]
  
                                                    if input_value >= 255 :
                                                        input_value = 255
                                    
                                                    # if hex_cnt >= 71 : #있으면 255 없으면 0
                                                   

                                                        
                                                    for yy in range(81):
                                                        fb.write(input_value.to_bytes(1,byteorder='big'))
                                                    hex_cnt += 1
    print("{0}피쳐 추출완료".format(xxe))


for xxe in dir_list:
    if __name__=="__main__":
        src = [] 
        name = [] 
        test = []
        print("start")

        image_dir = r'C:\Users\yoon\Desktop\CNNtest\test_output\{0}_feature'.format(xxe) #test file path
        #image_dir = r'C:\Users\yoon\Desktop\dataset\gray_output\{0}_gray'.format(xxe) #test file path
    
        #grayscale 변화
        for i in os.listdir(image_dir):
            file_full_path=image_dir + "/" + i
            path=os.path.dirname(file_full_path)
            base_name=os.path.splitext(os.path.basename(file_full_path))[0]
            outputFilename=os.path.join(path,base_name)

            binaryData=getBinaryData(file_full_path)
            createGreyScaleImageSpecificWith(binaryData, outputFilename)

            src.append(image_dir + "/" + i) 
            name.append(i)
            test.append(Dataization(image_dir + "/" + i + ".png"))

        print("파일 생성 완료")
        print("파일 변환")




