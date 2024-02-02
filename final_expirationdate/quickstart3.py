def main():
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text='{}년{}월{}일입니다'.format(final_year,final_month,final_day))
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", name="ko-KR-Wavenet-A"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("final.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "final.mp3"')
        
if __name__ == "__main__":

    main()
