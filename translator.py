from abc import abstractmethod
from deep_translator import GoogleTranslator


class Translator:
    @abstractmethod
    def translate(text: str, source_language: str, target_language: str) -> str:
        text = GoogleTranslator(source_language[:-3], target_language[:-3]).translate(text)
        if text:
            return text

        else:
            return '...'


