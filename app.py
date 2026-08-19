
import re

from listener import listen
from speaker import speak_text
from commands import execute_command
from wakeword import wait_for_wake_word
from brain import ask_ai

print("Starting JARVIS...")


# ==========================================
# MAIN JARVIS LOOP
# ==========================================

while True:

    try:

        # ==========================================
        # WAIT FOR WAKE WORD
        # ==========================================

        wait_for_wake_word()


        # ==========================================
        # CONFIRM
        # ==========================================

        speak_text(
            "Yes sir, I am listening"
        )


        # ==========================================
        # CONTINUOUS CONVERSATION
        # ==========================================

        while True:

            # --------------------------------------
            # LISTEN
            # --------------------------------------

            text = listen(
                duration=5
            )


            if not text:

                print(
                    "⚠️ No command received."
                )

                continue


            command = text.lower().strip()


            # ==========================================
            # CLEAN PUNCTUATION
            # ==========================================

            command = re.sub(
                r"[^\w\s]",
                "",
                command
            )

            command = " ".join(
                command.split()
            )


            print(
                "⚙️ Command:",
                command
            )


            # ==========================================
            # STOP JARVIS COMPLETELY
            # ==========================================

            stop_commands = [

                "stop jarvis",
                "exit jarvis",
                "exit",
                "goodbye jarvis",
                "good bye jarvis",
                "bye jarvis",
                "quit jarvis",
                "close jarvis",
                "shutdown jarvis",
                "shut down jarvis",
                "turn off jarvis",
                "terminate jarvis",
                "jarvis stop",
                "jarvis exit",
                "jarvis goodbye",
                "jarvis good bye"

            ]


            if any(
                phrase in command
                for phrase in stop_commands
            ):

                print(
                    "🛑 Stop command detected."
                )

                speak_text(
                    "Goodbye sir. JARVIS shutting down."
                )

                raise SystemExit


            # ==========================================
            # EXIT CONVERSATION
            # ==========================================

            if (
                "stop conversation" in command
                or "end conversation" in command
                or "go to sleep" in command
                or "sleep now" in command
            ):

                speak_text(
                    "Okay sir. I will wait for your wake word."
                )

                break


            # ==========================================
            # SYSTEM COMMAND
            # ==========================================

            handled = execute_command(
                command
            )


            # ==========================================
            # COMMAND WAS EXECUTED
            # ==========================================

            if handled:

                print(
                    "✅ Command handled."
                )

                continue


            # ==========================================
            # AI BRAIN
            # ==========================================

            print(
                "🧠 Sending to AI Brain..."
            )


            answer = ask_ai(
                command
            )


            # ==========================================
            # AI RESPONSE
            # ==========================================

            print(
                "🤖 JARVIS:",
                answer
            )


            # ==========================================
            # SPEAK RESPONSE
            # ==========================================

            speak_text(
                answer
            )


            # ==========================================
            # CONTINUE LISTENING
            # ==========================================

            print(
                "🎤 Ready for next command..."
            )


    # ==========================================
    # KEYBOARD INTERRUPT
    # ==========================================

    except KeyboardInterrupt:

        print(
            "\n🛑 JARVIS stopped."
        )

        break


    # ==========================================
    # GENERAL ERROR
    # ==========================================

    except SystemExit:

        print(
            "🛑 JARVIS stopped."
        )

        break


    except Exception as e:

        print(
            "❌ JARVIS Error:",
            e
        )