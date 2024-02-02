#텍스트를 음성으로 변환
from gtts import gTTS

text = "원하는 제품을 말씀해주세요"  
tts = gTTS(text, lang='ko')
tts.save("wantpr.mp3")
