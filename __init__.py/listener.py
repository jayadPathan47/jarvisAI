import sounddevice as sd

def test_microphone():
    devices = sd.query_devices()

    print("\nAvailable Microphones:\n")

    for i, device in enumerate(devices):
        if device["max_input_channels"] > 0:
            print(f"{i}. {device['name']}")