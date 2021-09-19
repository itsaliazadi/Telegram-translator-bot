from deep_translator import GoogleTranslator

class Language:

    def __init__(self) -> None:
        pass

    def translate_text(self, text, to_):
        translated = GoogleTranslator(source='auto', target=to_).translate(text)
        return translated