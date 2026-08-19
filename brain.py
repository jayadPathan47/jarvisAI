
import os
from dotenv import load_dotenv
from google import genai

from memory import get_memory, add_memory


# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("❌ GOOGLE_API_KEY not found in .env")


# ==========================================
# GEMINI CLIENT
# ==========================================

client = genai.Client(
    api_key=api_key
)


# ==========================================
# AI BRAIN
# ==========================================

def ask_ai(question):

    try:

        print("🧠 JARVIS AI is thinking...")

        # Load previous conversations
        memory = get_memory()

        # Create conversation context
        conversation = ""

        for item in memory[-10:]:

            conversation += (
                f"User: {item['user']}\n"
                f"JARVIS: {item['jarvis']}\n"
            )

        prompt = f"""
You are JARVIS, a helpful AI assistant.

Previous conversation:
{conversation}

Current user question:
{question}

Answer naturally and clearly.
Keep the answer reasonably concise unless the user asks for details.
"""

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        answer = response.text.strip()

        # Save current conversation
        add_memory(
            question,
            answer
        )

        return answer


    except Exception as e:

        print("❌ AI Error:", e)

        return (
            "Sorry sir, I am having trouble "
            "connecting to my AI brain."
        )
