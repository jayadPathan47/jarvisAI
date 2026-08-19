from PIL import ImageGrab
from datetime import datetime
import os


def take_screenshot():

    # Screenshot folder
    folder = "screenshots"

    os.makedirs(folder, exist_ok=True)

    # Current time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(
        folder,
        f"screenshot_{timestamp}.png"
    )

    # Capture screen
    screenshot = ImageGrab.grab()

    # Save screenshot
    screenshot.save(filename)

    print(f"📸 Screenshot saved: {filename}")

    return filename


if __name__ == "__main__":

    take_screenshot()