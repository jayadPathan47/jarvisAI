import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


def analyze_screen(image_path, question="What is on my screen?"):

    try:

        print("👁️ JARVIS is analyzing the screen...")

        with open(image_path, "rb") as f:
            image_data = f.read()

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=[
                types.Part.from_bytes(
                    data=image_data,
                    mime_type="image/png"
                ),
                question
            ]
        )

        answer = response.text.strip()

        print("👁️ Vision:", answer)

        return answer

    except Exception as e:

        print("❌ Vision error:", e)

        return ""