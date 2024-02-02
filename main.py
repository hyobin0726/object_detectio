#최종 메인코드
from __future__ import division
import os, sys
from playsound import playsound
import re
from google.cloud import speech
import pyaudio
from six.moves import queue
import removefile
from playsound import playsound

sys.path.append('/home/pi/detectron2')

import subprocess
import final_expirationdate as date
import final_expirationdate as camera
import final_expirationdate as ocr
import final_expirationdate as quickstart3

import final_main as start
global transcript

start.main()
#기능 선택
playsound("want.mp3")

RATE = 16000
CHUNK = int(RATE / 10)

class MicrophoneStream(object):
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk
        self._buff = queue.Queue()
        self.closed = True

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self._rate,
            input=True,
            frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        self._buff.put(in_data)
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b"".join(data)

def listen_print_loop(responses):
    global transcript
    num_chars_printed = 0
    for response in responses:
        if response.speech_event_type:
            text = transcript + overwrite_chars
            print('',format(text))
            return text
        if not response.results:
            continue
        result = response.results[0]
        if not result.alternatives:
            continue

        transcript = result.alternatives[0].transcript
        overwrite_chars = " " * (num_chars_printed - len(transcript))

        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + "\r")
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)
            if re.search(r"\b(exit|quit)\b", transcript, re.I):
                print("Exiting..")
                break

            num_chars_printed = 0
language_code = "ko-KR"  

client = speech.SpeechClient()
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=RATE,
    language_code=language_code,
)

streaming_config = speech.StreamingRecognitionConfig(
    config=config, single_utterance=True, interim_results=True
)

with MicrophoneStream(RATE, CHUNK) as stream:
    audio_generator = stream.generator()
    requests = (
        speech.StreamingRecognizeRequest(audio_content=content)
        for content in audio_generator
    )

    responses = client.streaming_recognize(streaming_config, requests)
    listen_print_loop(responses)

if(transcript == "유통기한"):
    #5초간 촬영 시작
    playsound("cam.mp3")
    playsound("beep.mp3")
    camera.main()
    #유통기한 탐색 시작합니다
    playsound("date.mp3")
    date.main()
    
    ocr.main()
    #최종 '{}년{}월{}일입니다' 형식으로 음성 출력
    quickstart3.main()
    
    playsound("final.mp3")
    removefile.removefile('/home/pi/video/cropped_images')
    

elif transcript == "알약":
    #알약 촬영 후 인식
    playsound("cam1.mp3")
    playsound("beep.mp3")
    #최종 의약품명, 복용법 음성으로 출력
    alyac_script = os.path.join("/home/pi/detectron2", "alyac.py")
    subprocess.run(["python3", alyac_script])
