
from listener import listen


WAKE_WORDS = [
    "hey jarvis",
    "hello jarvis",
    "yeah"
    "jarvis",
    "hey jaris",
    "hello jaris",
    "hi jarvis"
    "emu",
    "hi jarvis !",
    "hi jarvis"


]


def wait_for_wake_word():

    while True:

        text = listen(duration=2)

        if not text:
            continue

        text = text.lower().strip()

        for wake_word in WAKE_WORDS:

            if wake_word in text:

                print("✅ Wake word detected")

                return
