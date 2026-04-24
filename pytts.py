import pyttsx3

def init_engine(rate=180, volume=1.0, voice_gender=None):
    """
    Initialize TTS engine with custom settings
    """
    engine = pyttsx3.init()

    # Set speaking rate (speed)
    engine.setProperty('rate', rate)

    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', volume)

    # Select voice (male/female if available)
    voices = engine.getProperty('voices')
    if voice_gender:
        for voice in voices:
            if voice_gender.lower() in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

    return engine


def speak_text(engine, text):
    """
    Speak given text safely
    """
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"❌ Error while speaking: {e}")


def main():
    print("🔊 Text-to-Speech Program Started")

    engine = init_engine(rate=170, volume=1.0)

    while True:
        text = input("Enter text to speak (or 'exit' to quit): ")

        if text.lower() == "exit":
            print("👋 Exiting...")
            break

        speak_text(engine, text)


if __name__ == "__main__":
    main()