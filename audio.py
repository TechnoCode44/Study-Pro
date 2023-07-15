from gtts import gTTS as audio

async def save_audio(text: str, location: str, file_name: str):
    speach = audio(text)
    speach.save(f"Audio/{location}/{file_name}.mp3")