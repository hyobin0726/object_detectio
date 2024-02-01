#유통기한 형식 변환
import os, io
import pandas as pd
import cv2
from datetime import datetime

global model
model = 0

def result_word(str_input):  
    
    data= []
    number=[]
    
    try:  
    
        for i in range(0,len(str_input),1):        
            
                 if ( str_input[i]=='0' or
                     str_input[i]=='1' or 
                     str_input[i]=='2' or 
                     str_input[i]=='3' or 
                     str_input[i]=='4' or 
                     str_input[i]=='5' or
                     str_input[i]=='6' or
                     str_input[i]=='7' or
                     str_input[i]=='8' or
                     str_input[i]=='9'):
                
                        number.append(str_input[i]) 
        if len(number)>8:
           number="".join(number[0:8])                    
                        
        if len(number)==8: # yyyy mm dd일 경우
                year="".join(number[0:4])
                month="".join(number[4:6])
                day="".join(number[6:8])
                
                return "{0}년{1}월{2}일".format(year,month,day) # yyyy-mm-dd 형식에 맞춰서 반환
             
        elif len(number)==6: # yy mm dd일 경우
                year="".join(number[0:2])
                month="".join(number[2:4])
                day="".join(number[4:6])
                
                return "20{0}년{1}월{2}일".format(year,month,day) # yyyy-mm-dd 형식에 맞춰서 반환

        elif len(number)==4: # mm dd일 경우
                month="".join(number[0:2])
                day="".join(number[2:4])
                return "{0}년{1}월{2}일".format(datetime.today().year,month,day) # yyyy-mm-dd 형식에 맞춰서 반환

        else:
                return "다시입력하세요"

    except:
        return "Text 인식오류" # 오류가 있을 경우 반환
          

def main(): # main 함수
  import practice
  global result
  global year
  global month
  global day
  
  data=practice.text1
  ocr_text_list= data
  result = result_word(ocr_text_list)
  year=result[0:4]
  month=result[5:7]
  day=result[8:10]
  

if __name__ == "__main__":
    main()
