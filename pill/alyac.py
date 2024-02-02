import os
import numpy as np
import json
import random
import matplotlib.pyplot as plt


from detectron2.structures import BoxMode
from detectron2.data import DatasetCatalog, MetadataCatalog
from detectron2 import model_zoo
from detectron2.engine import DefaultTrainer, DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer
from matplotlib.patches import Rectangle

classes = ['타이레놀','이지엔']

from detectron2.config import get_cfg
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-Detection/faster_rcnn_R_101_FPN_3x.yaml")) #Yapılandırma Dosyası
cfg.DATASETS.TRAIN = ("my_train",)
cfg.DATASETS.TEST = ()
cfg.DATALOADER.NUM_WORKERS = 2
cfg.SOLVER.IMS_PER_BATCH = 2
cfg.SOLVER.BASE_LR = 0.001
cfg.SOLVER.GAMMA = 0.05
cfg.SOLVER.STEPS = [500]
cfg.TEST.EVAL_PERIOD = 200
cfg.SOLVER.MAX_ITER = 2000
cfg.MODEL.ROI_HEADS.NUM_CLASSES = 2
cfg.MODEL.DEVICE = "cpu"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.3

cfg.merge_from_list(["MODEL.WEIGHTS", "weights.pth"])   
with open("output.yaml", "w") as f:
  f.write(cfg.dump())  

import torch
import torchvision
import cv2

cfg.MODEL.WEIGHTS = "/home/pi/detectron2/output/model_final.pth"
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.3 
cfg.DATASETS.TEST = ("my_test", ) 
predictor = DefaultPredictor(cfg) 
test_metadata = MetadataCatalog.get("my_test")

from detectron2.utils.visualizer import ColorMode
import glob


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    outputs = predictor(image)


    pred_classes = outputs["instances"].pred_classes
    alyac_class_name = [classes[i] for i in pred_classes]
    real_alyac_name = alyac_class_name[0]
    print(real_alyac_name)

    v = Visualizer(image[:, :, ::-1], metadata=test_metadata, scale=0.8)
    out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    cv2.imshow("Detectron2", out.get_image()[:, :, ::-1])
    
    if len(real_alyac_name) > 0:
        cv2.imwrite("/home/pi/detectron2/detected_image.jpg", out.get_image()[:, :, ::-1])
        break
        
cap.release()
cv2.destroyAllWindows()

import pandas as pd

df1 = pd.read_csv("/home/pi/detectron2/alyac.csv", encoding='utf-8')
filtered_data = df1.loc[df1["alyac_name"] == real_alyac_name, ["alyac_name", "method"]]

column_list = sum(filtered_data[["alyac_name", "method"]].values.tolist(), [])
alyac_name = column_list[0]
alyac_method = column_list[1]

print(alyac_method)

with open("/home/pi/detectron2/output.txt", "w") as file: 
    file.write(real_alyac_name + '\n')
    file.write(alyac_method + '\n')

from google.cloud import texttospeech
from playsound import playsound

# 텍스트 파일에서 내용을 읽어옴
with open("/home/pi/detectron2/output.txt", "r") as file:
    text = file.read()

# Google Cloud Text-to-Speech 클라이언트 생성
client = texttospeech.TextToSpeechClient()

# 합성할 텍스트 설정
synthesis_input = texttospeech.SynthesisInput(text=text)

# 음성 설정
voice = texttospeech.VoiceSelectionParams(language_code="ko-KR", name="ko-KR-Wavenet-A")
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# 텍스트를 음성으로 합성
response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# 음성 파일 저장
with open("/home/pi/detectron2/pill.mp3", "wb") as file:
    file.write(response.audio_content)

# 음성 파일 재생
playsound("/home/pi/detectron2/pill.mp3")
