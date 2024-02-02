#중간 발표 메인 코드
from playsound import playsound
import product.AdapterTestDemo as AdapterTestDemo
import middle_mian.stt as stt
import product.quickstart as quickstart
import quickstart2
import os,sys
import video
import practice
import retext
import removefile
import middle_mian.sensor as sensor
import datetime 
import know.enter as enter

global fooddate 
global food

def main():
    
    while(1):
        #제품을 넣어주세요
        playsound("first.mp3")
        stt.main()   
        if(stt.transcript == "넣었어"):
            #원하는 기능을 말해주세요
            playsound("want.mp3")
            break
        else:
            continue
        
    stt.main()
    if(stt.transcript == "제품명"):
        #4방면 카메라 촬영
        AdapterTestDemo.main()
        #제품명을 위한 바코드 인식
        video.main()
        #최종 '%s입니다' 형식으로 제품명 음성 출력
        quickstart.main()
        playsound("output.mp3")
        
    #기능2 유통기한    
    if(stt.transcript == "유통기한"):
        #yolov5모델 객체탐지
        A="python3 detect.py --source capture --weights best0.pt --conf 0.25  --project runs/detect/exp --save-crop"
        #탐지된 이미지를 텍스트파일로 변환 
        B="python3 practice.py"
        os.system(A)
        os.system(B)
        
        #제품명을 위한 바코드 인식
        video.main()
        #유통기한 형식 변환
        retext.main()
        exec(open("dicti.py").read())
        
        #최종 '%s의 유통기한은 %s입니다' 형식으로 음성 출력
        quickstart2.main()
        playsound("output.mp3")
        
        removefile.removefile('/home/pi/runs/detect/exp/crops')
    
    #기능3 저장된 정보에서 묻고 답하기    
    if(stt.transcript == "알려 줘"):
        #원하는 제품을 말씀해주세요.
        playsound("wantpro.mp3")
        enter.main()
        playsound("output.mp3")
    
    
if __name__ == "__main__":
    while(True):
        if (sensor.soundlevel == 1):        
            main()
