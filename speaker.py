import edge_tts
import asyncio
import os


VOICE = "en-US-JennyNeural"


async def create_voice(text):
    communicate = edge_tts.Communicate(
        text,
        VOICE
    )

    await communicate.save("output.mp3")


def speak_text(text):
    asyncio.run(create_voice(text))
    os.startfile("output.mp3")