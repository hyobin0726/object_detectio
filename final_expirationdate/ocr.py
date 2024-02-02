import os
import re
import pytesseract
from PIL import Image
from collections import Counter

image_dir = '/home/pi/video/cropped_images'

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

year = []
month = []
day = []

for filename in os.listdir(image_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_dir, filename)
        image = Image.open(image_path)
        ocr_text = pytesseract.image_to_string(image)
        ocr_text1 = re.sub(r'[a-zA-Z\s.]', '', ocr_text)
        extracted_numbers = re.findall(r'20\d{6}', re.sub(r'[^0-9]', '', ocr_text1))
        print(extracted_numbers)
        for number in extracted_numbers:
            year.append(number[:4])
            month.append(number[4:6])
            day.append(number[6:8])
            
most_frequent_year = Counter(year).most_common(1)[0][0]
most_frequent_month = Counter(month).most_common(1)[0][0]
most_frequent_day = Counter(day).most_common(1)[0][0]

final_year = most_frequent_year
final_month = most_frequent_month
final_day = most_frequent_day

print(final_year,final_month,final_day)

