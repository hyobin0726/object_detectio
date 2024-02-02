def main():
    """Synthesizes speech from the input string of text or ssml."""

    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text='원하는 제품을 말씀해주세요')
    voice = texttospeech.VoiceSelectionParams(
        language_code="ko-KR", name="ko-KR-Wavenet-A"
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    with open("wantpr.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "wantpr.mp3"')

if __name__ == "__main__":
    main()
