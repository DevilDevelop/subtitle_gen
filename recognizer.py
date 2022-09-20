from abc import abstractmethod
import speech_recognition as sr


class Recognizer:
    @abstractmethod
    def transcribe(audio_file: str, language: str) -> str:
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)
                return recognizer.recognize_google(audio)

        except sr.UnknownValueError:
            return '...'
        

        