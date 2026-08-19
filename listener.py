
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import os
import tempfile
from faster_whisper import WhisperModel


# ============================================================
# JARVIS ENGLISH VOICE LISTENER
# ============================================================

print("🧠 Loading English Whisper model...")

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

print("✅ English Whisper model loaded.")


# ============================================================
# SETTINGS
# ============================================================

SAMPLE_RATE = 16000

# Minimum microphone level required.
# Lower = detects quieter voice.
ENERGY_THRESHOLD = 120

# Minimum valid transcription length.
MIN_TEXT_LENGTH = 2


# ============================================================
# CLEAN TRANSCRIPTION
# ============================================================

def clean_text(text):

    if not text:
        return None

    # Remove unnecessary spaces
    text = " ".join(text.split())

    # Remove immediate duplicate words
    words = text.split()

    cleaned_words = []

    for word in words:

        clean_word = word.strip(
            ".,!?;:"
        ).lower()

        if (
            cleaned_words
            and clean_word == cleaned_words[-1][0]
        ):
            continue

        cleaned_words.append(
            (
                clean_word,
                word
            )
        )

    text = " ".join(
        word
        for _, word in cleaned_words
    )

    return text.strip()


# ============================================================
# LISTEN FUNCTION
# ============================================================

def listen(duration=5):

    print("🎤 Listening...")

    temp_file = None

    try:

        # ====================================================
        # RECORD MICROPHONE
        # ====================================================

        recording = sd.rec(
            int(duration * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16"
        )

        sd.wait()


        # ====================================================
        # AUDIO LEVEL
        # ====================================================

        audio = recording.flatten()

        audio_float = audio.astype(
            np.float32
        )

        rms = np.sqrt(
            np.mean(
                audio_float ** 2
            )
        )

        print(
            f"🔊 Audio level: {rms:.0f}"
        )


        # ====================================================
        # SILENCE DETECTION
        # ====================================================

        if rms < ENERGY_THRESHOLD:

            print(
                "🔇 No voice detected."
            )

            return None


        # ====================================================
        # SAVE TEMPORARY AUDIO
        # ====================================================

        temp_file = os.path.join(
            tempfile.gettempdir(),
            "jarvis_command.wav"
        )

        wav.write(
            temp_file,
            SAMPLE_RATE,
            recording
        )


        # ====================================================
        # WHISPER PROCESSING
        # ====================================================

        print(
            "🧠 Processing..."
        )


        segments, info = model.transcribe(

            temp_file,

            # =================================================
            # IMPORTANT
            # =================================================
            # FORCE ENGLISH.
            #
            # Whisper will NOT automatically select Hindi,
            # Urdu, Marathi, Arabic, etc.
            # =================================================

            language="en",

            beam_size=5,

            # Prevent previous transcription context.
            condition_on_previous_text=False,

            # Deterministic output.
            temperature=0,

            # Voice Activity Detection.
            vad_filter=True,

            vad_parameters={
                "min_silence_duration_ms": 500,
                "speech_pad_ms": 300
            }
        )


        # ====================================================
        # COLLECT TRANSCRIPTION
        # ====================================================

        text_parts = []

        for segment in segments:

            segment_text = (
                segment.text.strip()
            )

            if segment_text:

                text_parts.append(
                    segment_text
                )


        text = " ".join(
            text_parts
        ).strip()


        # ====================================================
        # CLEAN TEXT
        # ====================================================

        text = clean_text(
            text
        )


        # ====================================================
        # DELETE TEMP FILE
        # ====================================================

        if temp_file:

            try:

                os.remove(
                    temp_file
                )

            except Exception:

                pass


        # ====================================================
        # EMPTY RESULT
        # ====================================================

        if not text:

            print(
                "🔇 No English speech recognized."
            )

            return None


        # ====================================================
        # MINIMUM TEXT CHECK
        # ====================================================

        if len(text) < MIN_TEXT_LENGTH:

            print(
                "⚠️ Speech too short."
            )

            return None


        # ====================================================
        # FINAL RESULT
        # ====================================================

        print(
            "You:",
            text
        )

        return text


    # ========================================================
    # ERROR HANDLING
    # ========================================================

    except Exception as e:

        print(
            "❌ Listener error:",
            e
        )

        return None


    # ========================================================
    # CLEANUP
    # ========================================================

    finally:

        if temp_file:

            try:

                if os.path.exists(
                    temp_file
                ):

                    os.remove(
                        temp_file
                    )

            except Exception:

                pass
