# object-detection : 시각장애인을 위한 AI 제품인식 멀티 디바이스
![image](https://github.com/hyobin0726/object_detection/assets/140376727/8ee7e75f-bc12-4b2e-8010-649361507d2b)

❓Problem : 다수의 시각장애인들은 본인이 섭취하는 음식의 유통기한을 알지 못하는 불편함을 드러냄, 더 나아가 알약과 같은 의약품의 경우 생김새가 비슷한 경우가 많아 촉감으로는 구별하기 어렵다.😮<br/>
![image](https://github.com/hyobin0726/object_detection/assets/140376727/26a36441-28ec-4f54-9bc5-a8638bd9b30b)

<br/>
‼ Idea : AI기술인 객체인식을 이용해 사용자가 원하는 정보(상품명, 유통기한, 복용법)을 음성으로 알려주는 기기는 어떨까? 🤔<br/>
<br/>
💯 Solution : YOLOv5, OCR, dectron2을 이용해 사용자가 원하는 정보를 알려주자.😁<br/>

## 구현 영상
https://youtu.be/v_KV7fvceWY?si=LRud7svx71RzoqtO
(영상추가하기)
## 주요 기능과 로직
1. ### 유통기한
   : 유통기한 위치를 AI 기술로 인식하여 전처리 및 후처리를 거쳐 자세한 정보를 알려준다. 
2. ### 제품명
   : 바코드의 위치를 AI 기술로 인식하여 OCR을 통해 바코드 정보를 불러와 제품명을 알려준다.
3. ### 의약품 정보
   : 의약품명, 복용법의 자세한 정보를 알려준다.

## 메인 로직 :
![image](https://github.com/hyobin0726/object_detection/assets/140376727/9014f363-ed69-47cc-9ca3-7b8921632c97)
![image](https://github.com/hyobin0726/object_detection/assets/140376727/089c12d1-c42f-424a-b809-27076b5e3d25)
![image](https://github.com/hyobin0726/object_detection/assets/140376727/e25679b7-f839-4b48-86f2-778985a6eca3)

## 서비스 구조 :
<img src="https://github.com/hyobin0726/object_detection/assets/140376727/68cb2168-1b9d-45a9-abfa-33c13de3dc06" width="500" height="400"/>

## 기술 스택
* 언어 : Python
* 딥러닝 모델 : Yolov5, detectron2, OCR, google cloud flatform stt/tts, Pyzbar
* 의약품 정보 데이터: 식약처 데이터(OpenApi)
  
## 개발 기간
* 2022년 9월 ~ 2023년 6월 <br/>

## 기획 & 설계
![image](https://github.com/hyobin0726/object_detection/assets/140376727/1ed2609a-6503-4263-8a97-62cd07acf88a)
![image](https://github.com/hyobin0726/object_detection/assets/140376727/24f069e4-4fee-49b3-9c1a-98933dba6eb6)
![KakaoTalk_20240202_144412436](https://github.com/hyobin0726/object_detection/assets/140376727/48ae92aa-83e2-4726-ae46-db6d89deedbf)

