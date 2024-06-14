import openai
import speech_recognition as sr
import pyaudio
import pyttsx3

class VoiceAssistant:

    def __init__(self, engine):
        self.recognizer=sr.Recognizer()
        self.engine=pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('Volume', 0.9)

    def record_audio(self):
        with sr.Microphone() as source:
            print('Listening...\n')
            print('Say Something...\n')
            audio=self.recognizer.listen(source)
        return audio

    def recognize_speech(self, audio):
        try:
            text=self.recognizer.recognize_google_cloud(audio)
            print(f'You said: {text}')

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")

        except sr.RequestError as er:
            print(f"Sorry, there is an error processing your request: {er}")

if __name__ == "__main__":
    engine=pyttsx3.init()
    voice=VoiceAssistant(engine)
    audio=voice.record_audio()
    voice.recognize_speech(audio)