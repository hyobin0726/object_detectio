#유통기한을 텍스트로 변환
import os,sys
import cv2
import pytesseract
global text1

if os.path.exists('/home/pi/runs/detect/exp/crops/capture_1.jpg'):
	img=cv2.imread('/home/pi/runs/detect/exp/crops/capture_1.jpg')
	rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
	text1= text.replace(" ", "")
	print(text1)
	
elif os.path.exists('/home/pi/runs/detect/exp/crops/capture_2.jpg'):
	img=cv2.imread('/home/pi/runs/detect/exp/crops/capture_2.jpg')
	rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
	text1= text.replace(" ", "")
	print(text1)
	
elif os.path.exists('/home/pi/runs/detect/exp/crops/capture_3.jpg'):
	img=cv2.imread('/home/pi/runs/detect/exp/crops/capture_3.jpg')
	rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
	text1= text.replace(" ", "")
	print(text1)
	
elif os.path.exists('/home/pi/runs/detect/exp/crops/capture_4.jpg'):
	img=cv2.imread('/home/pi/runs/detect/exp/crops/capture_4.jpg')
	rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	text = pytesseract.image_to_string(rgb_image, lang='kor+eng')
	text1= text.replace(" ", "")
	print(text1)

		