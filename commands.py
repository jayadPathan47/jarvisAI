import os
import subprocess
import pyautogui
import webbrowser
from datetime import datetime

from web_search import execute_web_command
from screenshot import take_screenshot
from vision import analyze_screen
from speaker import speak_text


def execute_command(command):

    command = command.lower().strip()

    print(f"⚙️ Command: {command}")

    # ==========================================
    # WEB SEARCH
    # ==========================================

    if execute_web_command(command):
        return


    # ==========================================
    # 👁️ VISION SYSTEM
    # ==========================================

    if any(phrase in command for phrase in [
        "what is on my screen",
        "what's on my screen",
        "describe my screen",
        "analyze my screen",
        "look at my screen",
        "read my screen",
        "what do you see"
    ]):

        print("👁️ Vision command detected")

        try:

            screenshot_path = take_screenshot()

            answer = analyze_screen(
                screenshot_path,
                "Describe everything important visible on this screen. "
                "Focus on applications, text, errors, buttons, and important information. "
                "Keep the answer concise."
            )

            if answer:

                print("👁️ JARVIS:", answer)
                speak_text(answer)

            else:

                speak_text(
                    "Sorry sir, I couldn't analyze the screen."
                )

        except Exception as e:

            print("❌ Vision system error:", e)

            speak_text(
                "Sorry sir, I couldn't analyze the screen."
            )

        return


    # ==========================================
    # OPEN CHROME
    # ==========================================

    if (
        "open chrome" in command
        or "open google chrome" in command
    ):

        print("🌐 Opening Chrome...")

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]

        chrome_opened = False

        for path in chrome_paths:

            if os.path.exists(path):

                subprocess.Popen([path])

                chrome_opened = True

                print("✅ Chrome opened")

                break

        if not chrome_opened:

            print("❌ Chrome executable not found")


    # ==========================================
    # OPEN NOTEPAD
    # ==========================================

    elif "open notepad" in command:

        print("📝 Opening Notepad...")

        subprocess.Popen("notepad.exe")


    # ==========================================
    # OPEN CALCULATOR
    # ==========================================

    elif (
        "open calculator" in command
        or "open calc" in command
    ):

        print("🧮 Opening Calculator...")

        subprocess.Popen("calc.exe")


    # ==========================================
    # OPEN FILE EXPLORER
    # ==========================================

    elif (
        "open file explorer" in command
        or "open explorer" in command
        or "open files" in command
    ):

        print("📁 Opening File Explorer...")

        subprocess.Popen("explorer.exe")


    # ==========================================
    # OPEN SETTINGS
    # ==========================================

    elif "open settings" in command:

        print("⚙️ Opening Windows Settings...")

        os.system("start ms-settings:")


    # ==========================================
    # YOUTUBE
    # ==========================================

    elif "open youtube" in command:

        print("🎬 Opening YouTube...")

        webbrowser.open("https://www.youtube.com")


    # ==========================================
    # GOOGLE
    # ==========================================

    elif "open google" in command:

        print("🌐 Opening Google...")

        webbrowser.open("https://www.google.com")


    # ==========================================
    # GITHUB
    # ==========================================

    elif "open github" in command:

        print("💻 Opening GitHub...")

        webbrowser.open("https://github.com")


    # ==========================================
    # SHUTDOWN
    # ==========================================

    elif (
        "shutdown" in command
        or "shut down" in command
    ):

        print("⏻ Shutting down laptop...")

        os.system("shutdown /s /t 5")


    # ==========================================
    # CANCEL SHUTDOWN
    # ==========================================

    elif (
        "cancel shutdown" in command
        or "abort shutdown" in command
    ):

        print("🛑 Cancelling shutdown...")

        os.system("shutdown /a")


    # ==========================================
    # RESTART
    # ==========================================

    elif "restart" in command:

        print("🔄 Restarting laptop...")

        os.system("shutdown /r /t 5")


    # ==========================================
    # LOCK COMPUTER
    # ==========================================

    elif (
        "lock computer" in command
        or "lock pc" in command
        or "lock laptop" in command
    ):

        print("🔒 Locking computer...")

        os.system(
            "rundll32.exe user32.dll,LockWorkStation"
        )


    # ==========================================
    # VOLUME UP
    # ==========================================

    elif (
        "volume up" in command
        or "increase volume" in command
        or "increase the volume" in command
    ):

        print("🔊 Increasing volume...")

        pyautogui.press("volumeup")


    # ==========================================
    # VOLUME DOWN
    # ==========================================

    elif (
        "volume down" in command
        or "decrease volume" in command
        or "decrease the volume" in command
    ):

        print("🔉 Decreasing volume...")

        pyautogui.press("volumedown")


    # ==========================================
    # MUTE
    # ==========================================

    elif (
        "mute" in command
        or "mute volume" in command
    ):

        print("🔇 Muting volume...")

        pyautogui.press("volumemute")


    # ==========================================
    # SCREENSHOT
    # ==========================================

    elif (
        "take screenshot" in command
        or "take a screenshot" in command
        or "screenshot" in command
    ):

        print("📸 Taking screenshot...")

        screenshot = pyautogui.screenshot()

        filename = "screenshot.png"

        screenshot.save(filename)

        print(f"✅ Screenshot saved as {filename}")


    # ==========================================
    # CLOSE CHROME
    # ==========================================

    elif (
        "close chrome" in command
        or "close google chrome" in command
    ):

        print("❌ Closing Chrome...")

        os.system("taskkill /f /im chrome.exe")


    # ==========================================
    # CLOSE NOTEPAD
    # ==========================================

    elif "close notepad" in command:

        print("❌ Closing Notepad...")

        os.system("taskkill /f /im notepad.exe")


    # ==========================================
    # CLOSE CALCULATOR
    # ==========================================

    elif "close calculator" in command:

        print("❌ Closing Calculator...")

        os.system("taskkill /f /im CalculatorApp.exe")


    # ==========================================
    # TIME
    # ==========================================

    elif (
        "what time is it" in command
        or command == "time"
    ):

        current_time = datetime.now().strftime("%I:%M %p")

        print(f"🕐 Current time: {current_time}")

        speak_text(f"Sir, the time is {current_time}")


    # ==========================================
    # DATE
    # ==========================================

    elif (
        "what is today's date" in command
        or "what is the date" in command
        or command == "date"
    ):

        current_date = datetime.now().strftime("%d %B %Y")

        print(f"📅 Today's date: {current_date}")

        speak_text(f"Sir, today's date is {current_date}")


    # ==========================================
    # OPEN COMMAND PROMPT
    # ==========================================

    elif (
        "open command prompt" in command
        or "open cmd" in command
    ):

        print("💻 Opening Command Prompt...")

        subprocess.Popen("cmd.exe")


    # ==========================================
    # OPEN POWERSHELL
    # ==========================================

    elif "open powershell" in command:

        print("💻 Opening PowerShell...")

        subprocess.Popen("powershell.exe")


            # ==========================================
    # 🖱️ KEYBOARD & MOUSE AUTOMATION
    # ==========================================

    elif "press enter" in command:

        print("⌨️ Pressing Enter...")
        pyautogui.press("enter")


    elif "press escape" in command or "press esc" in command:

        print("⌨️ Pressing Escape...")
        pyautogui.press("esc")


    elif "press tab" in command:

        print("⌨️ Pressing Tab...")
        pyautogui.press("tab")


    elif "press space" in command:

        print("⌨️ Pressing Space...")
        pyautogui.press("space")


    elif "go back" in command:

        print("↩️ Going back...")
        pyautogui.hotkey("alt", "left")


    elif "go forward" in command:

        print("↪️ Going forward...")
        pyautogui.hotkey("alt", "right")


    elif "switch window" in command or "switch windows" in command:

        print("🔄 Switching window...")
        pyautogui.hotkey("alt", "tab")


    elif "minimize window" in command:

        print("➖ Minimizing window...")
        pyautogui.hotkey("alt", "space")
        pyautogui.press("n")


    elif "maximize window" in command:

        print("⬆️ Maximizing window...")
        pyautogui.hotkey("alt", "space")
        pyautogui.press("x")


    elif "close window" in command:

        print("❌ Closing current window...")
        pyautogui.hotkey("alt", "f4")


    elif "copy" in command:

        print("📋 Copying...")
        pyautogui.hotkey("ctrl", "c")


    elif "paste" in command:

        print("📋 Pasting...")
        pyautogui.hotkey("ctrl", "v")


    elif "select all" in command:

        print("☑️ Selecting all...")
        pyautogui.hotkey("ctrl", "a")


    elif "save" in command:

        print("💾 Saving...")
        pyautogui.hotkey("ctrl", "s")


    elif "undo" in command:

        print("↩️ Undo...")
        pyautogui.hotkey("ctrl", "z")


    elif "redo" in command:

        print("↪️ Redo...")
        pyautogui.hotkey("ctrl", "y")


    elif "scroll up" in command:

        print("⬆️ Scrolling up...")
        pyautogui.scroll(5)


    elif "scroll down" in command:

        print("⬇️ Scrolling down...")
        pyautogui.scroll(-5)


    elif "home key" in command:

        print("🏠 Pressing Home...")
        pyautogui.press("home")


    elif "end key" in command:

        print("🏁 Pressing End...")
        pyautogui.press("end")


    elif "refresh page" in command or "refresh" in command:

        print("🔄 Refreshing...")
        pyautogui.press("f5")


    elif "zoom in" in command:

        print("🔍 Zooming in...")
        pyautogui.hotkey("ctrl", "+")


    elif "zoom out" in command:

        print("🔎 Zooming out...")
        pyautogui.hotkey("ctrl", "-")


    elif "open new tab" in command:

        print("➕ Opening new tab...")
        pyautogui.hotkey("ctrl", "t")


    elif "close tab" in command:

        print("❌ Closing tab...")
        pyautogui.hotkey("ctrl", "w")


    elif "next tab" in command:

        print("➡️ Next tab...")
        pyautogui.hotkey("ctrl", "tab")


    elif "previous tab" in command:

        print("⬅️ Previous tab...")
        pyautogui.hotkey("ctrl", "shift", "tab")


    # ==========================================
    # UNKNOWN COMMAND
    # ==========================================

    else:

        print("❓ Command not found")