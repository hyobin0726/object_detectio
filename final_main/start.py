import cv2
import mediapipe as mp
import pygame
from dynamikontrol import Module
import os, sys

ANGLE_STEP = 1

module = Module()
angle = 0 

mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
frame_count = 0
start_time = 0
elapsed_time = 0

pygame.mixer.init()
#안녕하세요 무엇이든 도와드리겠습니다.
audio_file = "first1.mp3"
pygame.mixer.music.load(audio_file)
audio_played = False 

# 얼굴 감지 및 동작 제어 루프
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.flip(img, 1) 
    results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if results.detections:
        frame_count += 1
        if frame_count == 1:
            start_time = cv2.getTickCount()
        for detection in results.detections:
            mp_drawing.draw_detection(img, detection)
            x1 = detection.location_data.relative_bounding_box.xmin
            x2 = x1 + detection.location_data.relative_bounding_box.width
            cx = (x1 + x2) / 2 
            if cx < 0.4: 
                angle += ANGLE_STEP
                module.motor.angle(angle)
            elif cx > 0.6: 
                angle -= ANGLE_STEP
                module.motor.angle(angle)
            if not audio_played:
                pygame.mixer.music.play()
                audio_played = True
            cv2.putText(img, '%d deg' % (angle), org=(10, 30), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=255, thickness=2)
            break
    else:
        frame_count = 0
        start_time = cv2.getTickCount()

    cv2.imshow('Face Cam', img)
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    if elapsed_time > 5 and frame_count > 0:
        cap.release()
        break
    if cv2.waitKey(1) == ord('q'):
        break
    
pygame.mixer.music.stop()
pygame.mixer.quit()
face_detection.close()
module.disconnect()
cv2.destroyAllWindows()
